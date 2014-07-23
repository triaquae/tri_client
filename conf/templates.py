#!/usr/bin/env python
from services import generic, linux

class BaseTemplate:
    name = None
    alert_policy = None
    groups = None
    hosts = None
    services = None

class LinuxGeneralServices(BaseTemplate):
    name = 'Linux General Services'
    groups = ['TestGroup',]
    #hosts = ['localhost','www.baidu.com']
    services = {
        'cpu': linux.cpu(),
        'memory':  linux.memory(),
        'load':  linux.load(),
        'upCheck': generic.upCheck(),
    }

class WindowsGeneralService(BaseTemplate):
    name = 'Windows General Services'
    #groups = ['BJ']
    hosts = ['localhost','www.baidu.com']
    services = {
        'load': linux.load(),
        'memory':  linux.memory(),
        'cpu': linux.cpu(),
    }

enabled_templates =( 
    LinuxGeneralServices(),
    #TestBaseTemplate(),
)
#print enabled_template[0].services['cpu'].triggers
#print enabled_policy[0].linux.[0].index_dic
