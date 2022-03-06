from pexpect import pxssh
import getpass

def create_user(hostname):
    s = pxssh.pxssh()
    username = "justincase"
    password = "Password01"
    s.login(hostname, username, password)

    s.sendline('sudo useradd ryanmcginty')
    s.prompt()
    s.sendline('Password01')
    s.sendline('sudo passwd ryanmcginty')
    s.prompt()
    s.sendline('FruitBasket')
    s.sendline('FruitBasket')
    s.prompt()
    print(s.before)
    s.sendline('hostname')
    s.prompt()
    print(s.before)

    s.logout()

def install_apache(hostname):
    s = pxssh.pxssh()
    username = "justincase"
    password = "Password01"
    s.login(hostname, username, password)

    s.sendline('sudo apt update')
    s.prompt()
    s.sendline('Password01')
    s.prompt()
    s.sendline('sudo apt install apache2')
    s.prompt()
    s.sendline('y')
    s.prompt()
    print(s.before)
    s.sendline('hostname')
    s.prompt()
    print(s.before)

    s.sendline('sudo service apache2 start')
    s.prompt()
    print(s.before)
    

    s.sendline('sudo systemctl enable apache2')
    s.prompt()
    s.sendline('sudo systemctl is-enabled apache2')
    s.prompt()
    print(s.before)

    s.logout()

def install_mariadb(hostname):
    s = pxssh.pxssh()
    username = "justincase"
    password = "Password01"
    s.login(hostname, username, password)

    s.sendline('sudo apt update')
    s.prompt()
    s.sendline('Password01')
    s.prompt()
    s.sendline('sudo apt install mariadb-server')
    s.prompt()
    s.sendline('y')
    s.prompt()
    print(s.before)
    s.sendline('hostname')
    s.prompt()
    print(s.before)

    s.sendline('sudo service mariadb start')
    s.prompt()
    print(s.before)

    s.sendline('sudo systemctl enable mariadb')
    s.prompt()
    s.sendline('sudo systemctl is-enabled mariadb')
    s.prompt()
    print(s.before)

    s.logout()

ip_addresses = ["192.168.0.111", "192.168.0.112", "192.168.0.121", "192.168.0.122"]
for ip_address in ip_addresses:
    create_user(ip_address)

web = ["192.168.0.111", "192.168.0.112"]
for i in web:
    install_apache(i)

db = ["192.168.0.121", "192.168.0.122"]
for j in db:
    install_mariadb(j)