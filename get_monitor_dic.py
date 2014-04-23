import json,os,sys,threading
from conf import policy, hosts
import db_connector
from TriAquae.hosts.models import Group,IP

def get_monitor_host_list():
        host_dic = {}
        for n,p in  enumerate(policy.enabled_policy):
                if p.groups is not None:
                        for g in p.groups:
                          for h in IP.objects.filter(group__name = g):
                                if not host_dic.has_key(h):
                                        host_dic[h] = [n] #add policy order into dic 
                                else:
                                        host_dic[h].append(n)

                                #host_list.extend( IP.objects.filter(group__name = g) )
                if p.hosts is not None:
                        for h in p.hosts:
                                host = IP.objects.get(hostname= h)
                                if not host_dic.has_key(host):
                                        host_dic[host] = [n] #add policy order into dic
                                else:
                                        if n not in host_dic[host]: #will not add the duplicate policy name
                                                host_dic[host].append(n)
        return host_dic


#print get_monitor_host_list()
