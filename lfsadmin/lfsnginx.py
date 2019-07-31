#!/usr/bin/env python
# -*- coding: utf-8 -*-
import commands
from publicCommands import get_ps_count
import os

def nginx_check_process():
    if get_ps_count('nginx') > 0:
        print 'nginx is started...'
    else:
        print 'nginx process is dead...'


def nginx_stop():
    cmd = 'pkill nginx'
    commands.getoutput(cmd)
    nginx_check_process()


def nginx_start():
    if get_ps_count('nginx') > 0:
        print 'nginx already started...'
    else:
        cmd = '/usr/local/nginx/sbin/nginx'
        commands.getoutput(cmd)
        nginx_check_process()


def nginx_restart():
    if get_ps_count('nginx') > 0:
        nginx_stop()
        if get_ps_count('nginx') == 0:
            print 'stop nginx success,will start nginx shortly'
            nginx_start()


def nginx_config_check():
    path = '/usr/local/nginx/'
    if os.path.exists(path):
        cmd = '/usr/local/nginx/sbin/nginx -t'
        ret, msg = commands.getstatusoutput(cmd)
        if ret != 0 and msg.find('successful') == -1:
            print 'nginx配置有错误，请按日志提示修改！'
            print msg
            return True
        else:
            print 'nginx配置检查成功，配置ok!'
            print msg
    else:
        print 'nginx目录不存在，请检查nginx是否已安装！'
        return True
