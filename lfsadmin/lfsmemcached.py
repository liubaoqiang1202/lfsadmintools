# -*- coding: utf-8 -*-
from publicCommands import get_ps_count, service_progress
import commands


def memcached_start():
    if get_ps_count('memcached') == 0:
        cmd = '/usr/bin/bash /etc/rc.local'
        commands.getoutput(cmd)
        service_progress(10)
        if get_ps_count('memcached') != 0:
            print 'start memcached Success!'
        else:
            print 'start memcached Failed'
    else:
        print 'memcached already started!'
    return True


def memcached_stop():
    if get_ps_count('memcached') == 0:
        print 'memcached not start'
    else:
        cmd = 'pkill memcached'
        commands.getoutput(cmd)
        if get_ps_count('memcached') == 0:
            print 'stop memcached Success!'
        else:
            print 'stop memcached failed!'
    return True


def memcached_restart():
    memcached_stop()
    if get_ps_count('memcached') == 0:
        # print 'stop memcached Success!'
        print 'starting memcached....'
        memcached_start()
    else:
        print 'stop memcached Failed!'
    return True




