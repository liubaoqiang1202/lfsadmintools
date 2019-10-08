#!/bin/bash
#安装依赖包,否则安装psutil等失败
yum install gcc python-devel
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

#安装虚拟空间
cd ../..
pip install packages/virtualenv-16.6.0-py2.py3-none-any.whl
virtualenv --no-site-packages venv

#source venv/bin/activate

echo "C_INCLUDE_PATH=/usr/local/python-2.7.5/include/python2.7" >> /etc/profile
echo "LIBRARY_PATH=/usr/local/python-2.7.5/lib" >> /etc/profile
#CPLUS_INCLUDE_PATH=/usr/local/include

source /etc/profile
#export CPLUS_INCLUDE_PATH

pip install --no-index --find-links=packages -r requirements_linux.txt
