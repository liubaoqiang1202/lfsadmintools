# -*- coding: utf-8 -*-
from publicCommands import get_ps_count
import commands


def memcached_start():
    if get_ps_count('memcached') == 0:
        cmd = 'sh /etc/rc.local'
        get_ps_count(cmd)
        if get_ps_count('memcached') != 0:
            print 'restart memcached Success!'
        else:
            print 'start memcached Failed'
    else:
        print 'memcached already started!'


def memcached_stop():
    if get_ps_count('memcached') == 0:
        print 'memcached not start'
    else:
        cmd = 'pkill memcached'
        commands.getoutput(cmd)


def memcached_restart():
    memcached_stop()
    if get_ps_count('memcached') == 0:
        print 'stop memcached success'
        print 'starting memcached....'
        memcached_start()
    else:
        print 'stop memcached Failed!'




