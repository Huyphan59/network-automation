from netmiko import ConnectHandler
import threading


def execute(device, cmd):
    connection = ConnectHandler(**device)
    output = connection.send_config_set(cmd)
    print(output)
    connection.disconnect()
    print('#' * 50)


devices = ['192.168.1.11', '192.168.1.21', '192.168.1.31']

cmd1 = ['router ospf 1', 'network 0.0.0.0 0.0.0.0 area 0']
cmd2 = ['int loopback 0', 'ip address 1.1.1.1 255.255.255.255', 'end', 'sh ip int loopback 0']
cmd3 = ['username k9 secret abck9', 'ip domain-name k9']
device_list = list()
for ip in devices:
    device = {
        'device_type': 'cisco_ios',
        'host': ip,
        'username': 'admin',
        'password': 'cisco',
        'port': 22,
        'secret': 'cisco',
        'verbose': True
    }
    if ip in '192.168.1.11':
        r1 = (device, cmd1)
    if ip in '192.168.1.21':
        r2 = (device, cmd2)
    if ip in '192.168.1.31':
        r3 = (device, cmd3)


device_list.append(r1)
device_list.append(r2)
device_list.append(r3)
threads = list()
for device in device_list:
    # try:
        # excute(device[0], device[1])
    th = threading.Thread(target=execute, args=(device[0], device[1]))  # device[0] is the dictionary and device[1] is the list with commands
    threads.append(th)
    #except Exception as e:
        # print(f'{e}\n')
        # print(f'{router[0]["host"]} is DOWN!!\n')

for th in threads:
    th.start()

for th in threads:
    th.join()
