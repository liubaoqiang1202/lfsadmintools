#!/usr/bin/env python
# -*- coding: utf-8 -*-
import psutil
import tqdm
import time


def get_ps_count(service_name):
    """
    获取各服务的进程数，检查进程是否存在
    :param service_name:
    :return:
    """
    ps_count = 0
    service_process = psutil.process_iter()
    for service in service_process:
        if service.name() == service_name:
            ps_count += 1
    return ps_count


def service_progress(maxrange=100):  # 进度条
    for i in tqdm.tqdm(range(0, maxrange)):
        time.sleep(0.1)


def check_web_service(index_file):
    with open(index_file, 'r') as f:
        count = 0
        find_str = '缓存服务异常'
        for line in f.readlines():
            a = line.find(find_str)
            if a != -1:
                count = a
        return count



