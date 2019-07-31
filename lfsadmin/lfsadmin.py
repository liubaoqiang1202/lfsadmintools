#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv, exit
from argparse import ArgumentParser
from other import after_check, before_check, start_all, stop_all
from lfstomcat import *
from lfsnginx import *
from lfsmemcached import *


def quitService():
    print '感谢您的使用...'
    exit(0)


class SubCmd:
    def __init__(self, act_list):
        self.act_table = act_list

    def __call__(self, parent):
        output_and_do_action(self.act_table, parent)


def build_select_info(act_list, parent=None):
    select_msg = '({index}) {msg}\n'
    ret_msg = ''
    act_list_len = len(act_list)

    for i in range(act_list_len):
        sel = act_list[i]
        ret_msg += select_msg.format(index=i+1, msg=sel[0])

    if parent is not None:
        ret_msg += select_msg.format(index=act_list_len+1, msg='back')

    return ret_msg


def output_and_do_action(act_list, parent=None):
    msg = build_select_info(act_list, parent)
    sel = 0
    act_list_len = len(act_list)
    max_sel = act_list_len if parent is None else act_list_len+1

    print msg

    try:
        sel = int(raw_input('choose: '))
    except ValueError:
        return output_and_do_action(act_list, parent)

    if sel < 1 or sel > max_sel:
        return output_and_do_action(act_list, parent)

    print '\n'

    # 如果是返回上一层
    if parent and sel == act_list_len+1:
        return output_and_do_action(parent)

    func = act_list[sel-1][1]

    # 如果是SubCmd的实例，传入上层菜单list给它，以实现返回上层菜单的功能
    if func.__class__.__name__ == 'SubCmd':
        func(act_list)
    else:
        func()

    return output_and_do_action(act_list, parent=parent)


def main():
    action_list = [
        ('system maintenance', SubCmd([
            ('start tomcat', lfs_start),
            ('stop tomcat', lfs_stop),
            ('restart tomcat', lfs_restart),
            ('start nginx', nginx_start),
            ('stop nginx', nginx_stop),
            ('restart nginx', nginx_restart),
            ('check nginx config', nginx_config_check),
            ('start memchched', memcached_start),
            ('stop memcached', memcached_stop),
            ('restart memcached', memcached_restart),
            ('stop all service', stop_all)])),  # 停止所有软件（nginx/memcached/tomcat）
        ('Normal startup all service', start_all),
        # ('Abnormal startup', lfs_start),
        ('Stop LFS', lfs_stop),  # 停止tomcat
        ('LFS check', SubCmd([
            ('before install check', before_check),
            ('after install check', after_check),
            ('Quit', quitService)
        ])),
        ('Quit', quitService)
    ]

    output_and_do_action(action_list)


if __name__ == '__main__':
    main()
