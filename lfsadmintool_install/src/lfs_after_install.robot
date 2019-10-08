*** Settings ***
Library	OperatingSystem
Library	DatabaseLibrary
Library	psutil
Library	psutil.Process

*** Test Cases ***
1、检查nginx是否安装
	${nginx_check}=	Run	/usr/local/nginx/sbin/nginx -t
	Log	${nginx_check}
	Should Contain	${nginx_check}	test is successful
	
2、检查librsync是否安装
	${librsync_check}=	Run	rdiff
	Log	${librsync_check}
	Should Contain	${librsync_check}	rdiff: You must specify an action: `signature', `delta', or `patch'

3、检查swftool是否安装
	${swftool_check}=	Run	pdf2swf
	Log	${swftool_check}
	Should Contain	${swftool_check}	Usage: pdf2swf [-options] file.pdf -o file.swf
	
4、检查ffmpeg是否安装
	${ffmpeg_check}=	Run	ffmpeg
	Log	${ffmpeg_check}
	Should Contain	${ffmpeg_check}	ffmpeg version 1.0.1 Copyright (c)

5、检查mysql数据库是否安装
	${mysql_check}	Run	service mysqld status
	LOG	${mysql_check}
	Should Contain	${mysql_check}	MySQL running

6、内存、CPU、存储空间使用情况
    ${cpu_count}    psutil.cpu_count
    LOG    ${cpu_count}    # CPU逻辑个数
    ${cpu_times}    psutil.cpu_times
    LOG    ${cpu_times}    # CPU时间
    ${memory_info}    psutil.virtual_memory
    LOG    ${memory_info}    # 内存信息
    #@{disk_partitions}    psutil.disk_partitions    # 分区信息
    #: FOR    ${p}    IN    @{disk_partitions}
    #\    Continue For Loop If    '${p.fstype}' == ''    # 跳过光驱等
    #\    ${p_info}    evaluate    psutil.disk_usage('${p.device}\\')    psutil
    #${net_info}    psutil.net_if_stats
    #LOG    ${net_info}
	
7、检查tomcat是否已经启动
	${tomcat_check}=	Run	ps -ef|grep tomcat
	Log	${tomcat_check}
	Should Contain	${tomcat_check}	file=/usr/linkapp/bin/tomcat-master/conf

8、检查数据库连接是否正常
    Connect To Database Using Custom Params    pymysql    database='data_linkapp', user='root', password='mysql2012', host='192.168.7.26', port=3306
	
9、检查数据库是否有慢查询日志
	${slow_log}	Run	ls /data/var
	LOG	${slow_log}
	Should Not Contain	${slow_log}	slow.log
	LOG	/data/var目录下没有慢查询日志

10、检查数据库主主同步是否正常
	${mysqls}	Run	mysql -uroot -pmysql2012 < /LFS_check/src/test.sql
	LOG	${mysqls}
	Should Contain	${mysqls}	Slave_IO_Running: Yes
	Should Contain  ${mysqls}	Slave_SQL_Running: Yes
	
11、检查keepalived服务器是否正常
	${keepalived_check}=	Run	service keepalived status
	Log	${keepalived_check}
	Should Contain	${keepalived_check}	active (running)

12、检查glusterfs服务运行及挂载
	${glusterfs_status}=      Run     service glusterd status
        Log     ${glusterfs_status}
        Should Contain  ${glusterfs_status}       active (running)	#查看服务器是否在运行
	${glusterfs_mount}=      Run     df -h
        Log     ${glusterfs_mount}
        Should Contain  ${glusterfs_mount}       /myvolume	#查看glusterfs是否已挂载