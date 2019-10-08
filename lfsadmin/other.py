# -*- coding: utf-8 -*-
import os
import datetime
from lfsmemcached import *
from lfstomcat import *
from lfsnginx import *


def setting():
    print 'setting...'


def before_check():  # 应用安装前检查 日志存放路径/home
    now = str(datetime.datetime.now())
    cmd = 'source /opt/lfsadmintools-master/lfsadmintool_install/venv/bin/activate;' \
          'robot -d "/home/beforeCheck' + now + '" src/lfs_before_install.robot'
    os.system(cmd)
    return True


def after_check():  # 应用安装后检查 日志存放路径/home
    now = str(datetime.datetime.now())
    cmd = 'source /opt/lfsadmintools-master/lfsadmintool_install/venv/bin/activate;' \
          'robot -d "/home/afterCheck' + now + '"  src/lfs_after_install.robot'
    os.system(cmd)
    return True


def start_all():
    if get_ps_count('nginx') == 0:
        nginx_start()
    else:
        nginx_restart()
    if get_ps_count('memcached') == 0:
        memcached_start()
    else:
        memcached_restart()
    if get_ps_count('java') == 0:
        lfs_start()
    else:
        lfs_restart()
    after_check()


def stop_all():
    lfs_stop()
    memcached_stop()
    nginx_stop()


def clearScreen():
    cmd = 'clear'
    os.system(cmd)


def get_ip():
    cmd = "ip addr |grep 'inet ' |grep -v '127.0.0.1' |awk -F ' ' {'print $2'} |awk -F '/' {'print $1'}"
    out = os.popen(cmd).read()
    print out
