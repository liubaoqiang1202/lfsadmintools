*** Settings ***
Library           psutil
Library           psutil.Process
Library           OperatingSystem
Library           String
Library           Telnet
Library           os
Library           json

*** Test Cases ***
1、查看CPU配置
    ${cpu_count}    psutil.cpu_count
    LOG    ${cpu_count}    # CPU逻辑个数
    ${cpu_times}    psutil.cpu_times
    LOG    ${cpu_times}    # CPU时间

2、服务器内存信息
    ${memory_info}    psutil.virtual_memory
    LOG    ${memory_info}    # 内存信息

3、硬盘信息
	${disk_IO}	psutil.disk_io_counters	#读取硬盘总个数
	LOG	${disk_IO}
    @{disk_partitions}    psutil.disk_partitions    # 分区信息
    : FOR    ${p}    IN    @{disk_partitions}
    \    Continue For Loop If    '${p.fstype}' == ''    # 跳过光驱等
    \    ${p_info}    evaluate    psutil.disk_usage('${p.device}')    psutil

4、网络检查
    ${net_info}    psutil.net_if_stats
    LOG    ${net_info}
	${net_ip}	psutil.net_if_addrs	#查看ip
	LOG	${net_ip}
	Open Connection    www.baidu.com    port=80    #检查外网是否通
	Close Connection
	#${connect_internet}	Run	ping www.baidu.com -c 2	#检查外网是否通
	#LOG	${connect_internet}
	#Should Contain	${connect_internet}	64 bytes from 14.215.177.39:

5、检查防火墙是否已关闭
	${system_version}       Run     cat /etc/redhat-release
	LOG     ${system_version}
	${redhat}       get regexp matches      ${system_version}       Red Hat
	LOG     ${redhat}
	${firewall_status}      run keyword if  ${redhat}!=[]   run     service iptables status
	...    ELSE     run	firewall-cmd --state
	should contain any      ${firewall_status}      not running     iptables：未运行防火墙	
	
6、检查selinux是否关闭
	${selinux_check}	Run	cat /etc/selinux/config
	LOG	${selinux_check}
	Should Contain	${selinux_check}	SELINUX=disabled
	
