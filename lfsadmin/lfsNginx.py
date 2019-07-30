#!/usr/bin/env python
# -*- coding: utf-8 -*-
import commands
from publicCommands import get_ps_count


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
