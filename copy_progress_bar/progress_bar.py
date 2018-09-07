
def copy_with_pb():
    source_size = os.stat(SOURCE_FILENAME).st_size
    copied = 0
    source = open(SOURCE_FILENAME, 'rb')
    target = open(TARGET_FILENAME, 'wb')

    while True:
        chunk = source.read(32768)
        if not chunk:
            break
        #end if
        target.write(chunk)
        copied += len(chunk)
        print '\r%02d%%' % (copied * 100 / source_size),
    #end while

    source.close()
    target.close()
#end def

