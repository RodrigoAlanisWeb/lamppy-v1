import subprocess
import os

# Lampp
def start_lampp():
    subprocess.call('sudo /opt/lampp/lampp start', shell=True)

def stop_lampp():
    subprocess.call('sudo /opt/lampp/lampp stop', shell=True)

def restart_lampp():
    subprocess.call('sudo /opt/lampp/lampp restart', shell=True)
def repare_lampp():
    subprocess.call('sudo /etc/init.d/apache2 stop ', shell=True)
    subprocess.call('service mysql stop ', shell=True)
    restart_lampp()

# Mysql
def enter_mysql(host,user,password=False):
    if password:
        subprocess.call(f'mysql -h {host} -u {user} -p {password}', shell=True)
    else:
        subprocess.call(f'mysql -h {host} -u {user}', shell=True)
