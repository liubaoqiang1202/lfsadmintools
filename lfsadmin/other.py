# -*- coding: utf-8 -*-

import os
import datetime


def setting():
    print 'setting...'


def before_check():  # 应用安装前检查 日志存放路径/home
    now = str(datetime.datetime.now())
    cmd = 'source /LFS_check/venv/bin/activate;robot -d "/home/beforeCheck' + now + '" src/lfs_before_install.robot'
    os.system(cmd)
    return True


def after_check():  # 应用安装后检查 日志存放路径/home
    now = str(datetime.datetime.now())
    cmd = 'source /LFS_check/venv/bin/activate;robot -d "/home/afterCheck' + now + '" src/lfs_after_install.robot'
    os.system(cmd)
    return True


