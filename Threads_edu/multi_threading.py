import socket
import select
import sys
import errno
import time

from config import *

def ioloop(ip_source, request_source):
    '''јсинхронный цикл собственной персоной

    ip_source Ч бесконечный iterable, выдающий ip-адреса дл€ соединений ;
    request_source Ч iterable, генерирующий тела запросов;
    '''
    starttime = time.time()

    # открываем пул сокетов; словари, хран€щие соединени€ тела запросов и ответов
    epoll = select.epoll()
    connections = {}; responses = {}; requests = {}
    bytessent = 0.0
    bytesread = 0.0
    timeout = 0.3

    # выбираем первый запрос
    request = request_source.next()
    try:
        while True:
            # провер€ем число соединений, если их меньше минимально
            # возможного и остались запросы Ч добавл€ем еще одно.
            #
            connection_num = len(connections)

            if connection_num<CLIENT_NUM and request:
                ip = ip_source.next()
                print ЂOpening a connection to %s.ї % ip
                clientsocket = socket.socket(socket.AF_INET,
                                             socket.SOCK_STREAM)
                # Ќесколько нетривиально. Ќеблокирующий сокет выбрасывает
                # исключение-ошибку EINPROGRESS, если не может сразу соединитьс€ сразу.
                # »гнорируем ошибку и начинаем ждать событи€ на сокете.
                #
                clientsocket.setblocking(0)
                try:
                    res = clientsocket.connect((ip, 80))
                except socket.error, err:
                    #
                    if err.errno != errno.EINPROGRESS:
                        raise
                # ¬носим сокет в пул и словарь соединений
                epoll.register(clientsocket.fileno(), select.EPOLLOUT)
                connections[clientsocket.fileno()] = clientsocket
                requests[clientsocket.fileno()] = request
                responses[clientsocket.fileno()] = ""

            # Ђѕулингї Ч то есть сбор событий
            #
            events = epoll.poll(timeout)
            for fileno, event in events:
                if event & select.EPOLLOUT:
                    # ѕосылаем часть запроса...
                    #
                    try:
                        byteswritten = connections[fileno].send(requests[fileno])
                        requests[fileno] = requests[fileno][byteswritten:]
                        print byteswritten , Ђbytes sent.ї
                        bytessent += byteswritten
                        if len(requests[fileno]) == 0:
                            epoll.modify(fileno, select.EPOLLIN)
                            print Ђswitched to reading.ї
                    except socket.error, err:
                        print ЂSocket write error: Д, err
                    except Exception, err:
                        print УUnknown socket error: Д, err
                elif event & select.EPOLLIN:
                    # „итаем часть ответа...У
                    #
                    try:
                        bytes = connections[fileno].recv(1024)
                    except socket.error, err:
                        # ¬ылавливаем ошибку Дconnection reset by peerУ Ч
                        #случаетс€ при большом числе соединений
                        #
                        if err.errno == errno.ECONNRESET:
                            epoll.unregister(fileno)
                            connections[fileno].close()
                            del connections[fileno]
                            print "Connection reset by peer."
                            continue
                        else:
                            raise err

                    print len(bytes) , Ђbytes read.ї
                    bytesread += len(bytes)
                    responses[fileno] += bytes
                    if not bytes:
                        epoll.unregister(fileno)
                        connections[fileno].close();
                        del connections[fileno]
                        print ЂDone reading...Closed.ї

    # выбираем следующий запрос
            if request:
                request = request_source.next()

            print ЂConnections left: Д, len(connections)
            if not len(connections):
                break
    except KeyboardInterrupt:
        print УLooping interrupted by a signal.ї
        for fd, sock in connections.items():
            sock.close()
    epoll.close()

    endtime = time.time()
    timespent = endtime - starttime
    return responses, timespent, bytesread, bytessent

