#!/usr/bin/env python
# -*- coding: utf-8 -*-
import commands
import time
from publicCommands import get_ps_count


def lfs_start():
    if get_ps_count('java') != 0:  # 检查tomcat是否已经启动,如果已经启动,出现文字提示,选择是否需要重启
        print '应用已经启动,如果需要重启,请选择重启项!'
    else:
        cmd = '/usr/linkapp/bin/tomcat_check.sh'
        print '开始启动LFS应用'
        start_status, start_msg = commands.getstatusoutput(cmd)
        if start_status == 0 and get_ps_count('java') != 0:
            print 'start LFS success...'
        else:
            print 'start LFS failed'


def lfs_stop():
    cmd = '/usr/bin/sync'  # 将内存缓冲区数据写入磁盘
    commands.getstatusoutput(cmd)
    time.sleep(10)
    cmd = '/usr/linkapp/bin/tomcat_stop.sh'
    print '开始停止LFS应用'
    commands.getstatusoutput(cmd)
    time.sleep(5)  # 需要等待5s，否则检查进程数会异常。
    if get_ps_count('java') == 0:
        print 'stop LFS success...'
    else:
        print 'stop LFS failed,please check logfile /usr/linkapp/bin/tomcat-master/logs'


def lfs_restart():
    cmd = '/usr/linkapp/bin/tomcat_restart.sh'
    print '开始重启LFS应用'
    commands.getstatusoutput(cmd)
    wget_status, wget_msg = commands.getstatusoutput(cmd='wget http://127.0.0.1:6800')

    if wget_status != 0 and get_ps_count('java') != 0:
        print 'tomcat已启动，页面功能异常，请检查'
    elif wget_status == 0 and get_ps_count('java') > 0:
        print 'start LFS success'
    else:
        print 'start LFS service failed...'
        print '请查看tomcat日志 /usr/linkapp/bin/tomcat-master/logs/'


