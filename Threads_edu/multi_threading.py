import socket
import select
import sys
import errno
import time

from config import *

def ioloop(ip_source, request_source):
    '''����������� ���� ����������� ��������

    ip_source � ����������� iterable, �������� ip-������ ��� ���������� ;
    request_source � iterable, ������������ ���� ��������;
    '''
    starttime = time.time()

    # ��������� ��� �������; �������, �������� ���������� ���� �������� � �������
    epoll = select.epoll()
    connections = {}; responses = {}; requests = {}
    bytessent = 0.0
    bytesread = 0.0
    timeout = 0.3

    # �������� ������ ������
    request = request_source.next()
    try:
        while True:
            # ��������� ����� ����������, ���� �� ������ ����������
            # ���������� � �������� ������� � ��������� ��� ����.
            #
            connection_num = len(connections)

            if connection_num<CLIENT_NUM and request:
                ip = ip_source.next()
                print �Opening a connection to %s.� % ip
                clientsocket = socket.socket(socket.AF_INET,
                                             socket.SOCK_STREAM)
                # ��������� ������������. ������������� ����� �����������
                # ����������-������ EINPROGRESS, ���� �� ����� ����� ����������� �����.
                # ���������� ������ � �������� ����� ������� �� ������.
                #
                clientsocket.setblocking(0)
                try:
                    res = clientsocket.connect((ip, 80))
                except socket.error, err:
                    #
                    if err.errno != errno.EINPROGRESS:
                        raise
                # ������ ����� � ��� � ������� ����������
                epoll.register(clientsocket.fileno(), select.EPOLLOUT)
                connections[clientsocket.fileno()] = clientsocket
                requests[clientsocket.fileno()] = request
                responses[clientsocket.fileno()] = ""

            # ������� � �� ���� ���� �������
            #
            events = epoll.poll(timeout)
            for fileno, event in events:
                if event & select.EPOLLOUT:
                    # �������� ����� �������...
                    #
                    try:
                        byteswritten = connections[fileno].send(requests[fileno])
                        requests[fileno] = requests[fileno][byteswritten:]
                        print byteswritten , �bytes sent.�
                        bytessent += byteswritten
                        if len(requests[fileno]) == 0:
                            epoll.modify(fileno, select.EPOLLIN)
                            print �switched to reading.�
                    except socket.error, err:
                        print �Socket write error: �, err
                    except Exception, err:
                        print �Unknown socket error: �, err
                elif event & select.EPOLLIN:
                    # ������ ����� ������...�
                    #
                    try:
                        bytes = connections[fileno].recv(1024)
                    except socket.error, err:
                        # ����������� ������ �connection reset by peer� �
                        #��������� ��� ������� ����� ����������
                        #
                        if err.errno == errno.ECONNRESET:
                            epoll.unregister(fileno)
                            connections[fileno].close()
                            del connections[fileno]
                            print "Connection reset by peer."
                            continue
                        else:
                            raise err

                    print len(bytes) , �bytes read.�
                    bytesread += len(bytes)
                    responses[fileno] += bytes
                    if not bytes:
                        epoll.unregister(fileno)
                        connections[fileno].close();
                        del connections[fileno]
                        print �Done reading...Closed.�

    # �������� ��������� ������
            if request:
                request = request_source.next()

            print �Connections left: �, len(connections)
            if not len(connections):
                break
    except KeyboardInterrupt:
        print �Looping interrupted by a signal.�
        for fd, sock in connections.items():
            sock.close()
    epoll.close()

    endtime = time.time()
    timespent = endtime - starttime
    return responses, timespent, bytesread, bytessent

