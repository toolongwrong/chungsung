import platform
import os
import sys
if platform.system() == 'Windows' :
    os.system('pip install konlpy')
    os.system('sudo pip3 install PyMySQL')
else :
    os.system('pip3 --version >>test.txt')
    with open('test.txt','r') as open_file :
        version = open_file.readline()
        if (version) != 'null' :
            version = version.split(" ")
        if version[1] == "10.0.1" :
            os.system('echo version clear')
        else:
            os.system('wget https://bootstrap.pypa.io/get-pip.py')
            os.system('sudo python3 get-pip.py')
            os.system('sudo pip3 install -U setuptools')
            os.system('rm get-pip.py')
    os.system('rm test.txt')
    os.system('sudo pip3 install konlpy')
    os.system('sudo pip3 install PyMySQL')

