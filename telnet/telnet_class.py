import telnetlib
import getpass
import time
from datetime import datetime

now = datetime.now()
year = now.year
month = now.month
day = now.day


class Device:
    def __init__(self, host, user, password, tn=None):
        self.host = host
        self.user = user
        self.password = password
        self.tn = tn
        self.password = getpass.getpass(f'Enter password for {self.host}: ')

    def connect(self):
        self.tn = telnetlib.Telnet(self.host)
        print(f'Connecting to {self.host}...')

    def authenticate(self):
        self.tn.read_until(b'Username: ')
        self.tn.write(self.user.encode() + b'\n')
        self.tn.read_until(b'Password: ')
        self.tn.write(self.password.encode() + b'\n')

        time.sleep(1)

    def send(self, command, timeout=1):
        import time
        self.tn.write(command.encode() + b'\n')
        time.sleep(timeout)

    def send_from_list(self, commands):
        for cmd in commands:
            self.send(cmd)

    def send_from_file(self, filename):

        with open(filename, 'r') as f:
            lines = f.readlines()
        self.send_from_list(lines)

    def show(self):
        output = self.tn.read_all()
        output = output.decode()
        print(output)

    def backup(self):
        commands = ['enable', self.password, 'terminal length 0', 'show run', 'exit']
        self.send_from_list(commands)
        output = self.tn.read_all().decode().split('\n')[9:-2]
        output = '\n'.join(output)
        # print(output)
        filename = f'{self.host}_{year}-{month}-{day}.txt'
        with open(filename, 'w') as f:
            f.write(output)

    # def backup_multiple_devices(**self):
    #     import threading
    #     threads = []
    #     for f, v in self.items():
    #         thread = threading.Thread(target=self.backup, args=(self,))
    #         threads.append(thread)
    #     for th in threads:
    #         th.start()
    #     for th in threads:
    #         th.join()


if __name__ == '__main__':
    router1 = {'host': '192.168.1.10', 'user': 'admin', 'password': 'cisco123', 'enable_password': 'cisco123',
               'loopback_ip': '1.1.1.1'}
    router2 = {'host': '192.168.1.20', 'user': 'admin', 'password': 'cisco123', 'enable_password': 'cisco123',
               'loopback_ip': '2.2.2.2'}
    router3 = {'host': '192.168.1.30', 'user': 'admin', 'password': 'cisco123', 'enable_password': 'cisco123',
               'loopback_ip': '3.3.3.3'}
    routers = [router1, router2, router3]

    for router_dict in routers:
        router = Device(host=router_dict['host'], user=router_dict['user'], password=router_dict['password'])
        router.connect()
        router.authenticate()
        commands = ['enable', router_dict['enable_password'], 'conf t', 'int lo0',
                    'ip add ' + router_dict['loopback_ip'] + ' 255.255.255.255',
                    'exit', 'router ospf 1', 'net ' + router_dict['loopback_ip'] + ' 0.0.0.0 area 0', 'end', 'exit']
        router.send_from_list(commands)

        router.show()
        print('#' * 50)
