import global_setting
from conf.conf import triserver_master, port
import sync_master
print triserver_master,port 

sync_master.server_connector('syncdb data', triserver_master, port)
