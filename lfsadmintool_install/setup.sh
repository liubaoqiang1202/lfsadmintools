#!/bin/bash
#安装依赖包,否则安装psutil等失败
yum install -y gcc python-devel
#lfsadmintools执行脚本
cp /opt/lfsadmintools-master/lfsadmintool_install/lfsadmintools /usr/sbin/
chmod 777 /usr/sbin/lfsadmintools
#创建日志存放目录
mkdir -p /home/afterCheck
mkdir -p /home/beforeCheck

chmod 755 -R /opt/lfsadmintools-master
#安装python
cd ./python
tar -zxvf Python-2.7.5.tgz
cd Python-2.7.5
./configure --prefix=/usr/local/python-2.7.5 -enable-shared CFLAGS=-fPIC
make
make install
#mv /usr/bin/python /usr/bin/python2.6.6
#ln -s /usr/local/python-2.7.9/bin/python /usr/bin/python

#安装setuptools
cd ..
unzip setuptools-36.0.1.zip
cd setuptools-36.0.1
python setup.py install

#安装pip
cd ..
tar -zxvf pip-19.1.1.tar.gz
cd pip-19.1.1
python setup.py install
#ln -s /usr/local/python-2.7.5/bin/pip /usr/bin/pip

pip install /opt/lfsadmintools-master/lfsadmintool_install/packages/tqdm-4.36.1-py2.py3-none-any.whl

cd /opt/lfsadmintools-master/lfsadmintool_install/packages/

tar -zxvf psutil-5.5.1.tar.gz
cd -
cd /opt/lfsadmintools-master/lfsadmintool_install/packages/psutil-5.5.1/
/usr/bin/python setup.py install
cd -
#安装虚拟空间
cd ../..
pip install packages/virtualenv-16.6.0-py2.py3-none-any.whl
virtualenv --no-site-packages venv

source venv/bin/activate

C_INCLUDE_PATH=/usr/local/python-2.7.5/include/python2.7
LIBRARY_PATH=/usr/local/python-2.7.5/lib
#CPLUS_INCLUDE_PATH=/usr/local/include

#export CPLUS_INCLUDE_PATH
export C_INCLUDE_PATH
export LIBRARY_PATH

pip install --no-index --find-links=packages -r /opt/lfsadmintools-master/lfsadmintool_install/requirements_linux.txt

pip install /opt/lfsadmintools-master/lfsadmintool_install/packages/tqdm-4.36.1-py2.py3-none-any.whl

pip install /opt/lfsadmintools-master/lfsadmintool_install/packages/psutil-5.5.1-cp27-cp27m-linux_x86_64.whl