import telnetlib
import time
import getpass

router1 = {'host': '192.168.1.10', 'user': 'admin'}
router2 = {'host': '192.168.1.20', 'user': 'admin'}
router3 = {'host': '192.168.1.30', 'user': 'admin'}
routers = [router1, router2, router3]

for router in routers:
    print(f'Connecting to {router["host"]}...')
    tn = telnetlib.Telnet(host=router['host'])
    tn.read_until(b'Username: ')
    tn.write(router['user'].encode() + b'\n')
    password = getpass.getpass(f'Enter password: ')
    tn.read_until(b'Password: ')
    tn.write(password.encode() + b'\n')

    tn.write(b'terminal length 0\n')
    #tn.write('show ip int bri\n'.encode())
    tn.write(b'enable\n')
    tn.write(password.encode() + b'\n')
    tn.write(b'conf t\n')
    tn.write(b'ip route 0.0.0.0 0.0.0.0 f0/0 192.168.1.254\n')
    tn.write(b'end\n')
    tn.write(b'show ip route\n')
    tn.write(b'wr\n')
    tn.write('exit\n'.encode())
    time.sleep(1)

    output = tn.read_all()
    print(output.decode())
    print('#' * 50)
