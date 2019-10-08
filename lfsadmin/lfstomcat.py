#!/usr/bin/env python
# -*- coding: utf-8 -*-
import commands
import os
from publicCommands import get_ps_count, service_progress, check_web_service
# import time


def lfs_start():
    if get_ps_count('java') != 0:  # 检查tomcat是否已经启动,如果已经启动,出现文字提示,选择是否需要重启
        print '应用已经启动,如果需要重启,请选择重启项!'
    else:
        cmd = '/usr/linkapp/bin/tomcat_check.sh'
        print '开始启动LFS应用'
        start_status, start_msg = commands.getstatusoutput(cmd)
        service_progress()
        if start_status == 0 and get_ps_count('java') != 0:
            print 'start LFS success...'
        else:
            print 'start LFS failed'


def lfs_stop():
    if get_ps_count('java') != 0:
        cmd = '/usr/bin/sync'  # 将内存缓冲区数据写入磁盘
        print '开始同步缓冲区数据到磁盘...'
        commands.getstatusoutput(cmd)
        service_progress()
    #    time.sleep(10)
        cmd = '/usr/linkapp/bin/tomcat_stop.sh'
        print '开始停止LFS应用'
        commands.getstatusoutput(cmd)
        service_progress()  # 使用进度条代替sleep，避免在显示上卡住。
    #    time.sleep(5)  # 需要等待5s，否则检查进程数会异常。
        if get_ps_count('java') == 0:
            print 'stop LFS success...'
        else:
            print 'stop LFS failed,please check logfile /usr/linkapp/bin/tomcat-master/logs'
    else:
        print 'LFS应用未启动...'


def lfs_restart():
    cmd = '/usr/linkapp/bin/tomcat_restart.sh'
    print '开始重启LFS应用'
    os.system(cmd)
    wget_status, wget_msg = commands.getstatusoutput(cmd='wget http://127.0.0.1:6800')
    if wget_status != 0 and get_ps_count('java') != 0:
        print 'tomcat已启动，页面功能异常，请检查'
    elif wget_status == 0 and get_ps_count('java') > 0:
        print 'start LFS success'
    else:
        print 'start LFS service failed...'
        print '请查看tomcat日志 /usr/linkapp/bin/tomcat-master/logs/'

