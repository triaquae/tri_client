import sys,traceback



def pprint(msg,msg_type, exit=0):
    if sys.platform.startswith("win"):
        if msg_type == 'err':
            print  'Error:%s' % msg
        elif msg_type == 'success':
            print '%s' % msg
        else:
            pass
    else:
        if msg_type == 'err':
            traceback.print_exc(file=sys.stdout)
            print '\033[31;1mError:%s\033[0m' % msg
        elif msg_type == 'success':
            print '\033[32;1m%s\033[0m' % msg
        else:
            pass
    if exit == 1:sys.exit()
    
