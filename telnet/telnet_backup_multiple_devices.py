import telnet_class
from datetime import datetime


now = datetime.now()
year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute

router1 = {'host': '192.168.1.10', 'user': 'admin', 'enable_password': 'cisco123', 'loopback_ip': '1.1.1.1',
           'file': 'C:\\Users\\Huy Phan\\PycharmProjects\\Network_automation\\Telnet\\test1.txt'}
router2 = {'host': '192.168.1.20', 'user': 'admin', 'enable_password': 'cisco123', 'loopback_ip': '2.2.2.2',
           'file': 'C:\\Users\\Huy Phan\\PycharmProjects\\Network_automation\\Telnet\\test2.txt'}
router3 = {'host': '192.168.1.30', 'user': 'admin', 'enable_password': 'cisco123', 'loopback_ip': '3.3.3.3',
           'file': 'C:\\Users\\Huy Phan\\PycharmProjects\\Network_automation\\Telnet\\test3.txt'}
routers = [router1, router2, router3]

for router_dic in routers:
    try:
        router = telnet_class.Device(host=router_dic['host'], user=router_dic['user'], password=None)
        router.connect()
        router.authenticate()

        # 2.
        # router.send('show users')
        # router.send('exit')
        # 3.
        print('Backing up...')
        router.backup()
        print('Backup completed.')
        # write log
        with open('log.txt', 'a') as f:
            f.write(f'Backup completed for {router_dic["host"]}_{year}-{month}-{day}-{hour}:{minute}.\n')

        # 8. Send command from file
        # router.send_from_file(router_dic['file'])

        # router.show()
        print('#'*50)
    except Exception as e:
        print(e)
        print('Failed to connect to', router_dic['host'])
        with open('log.txt', 'a') as f:
            f.write(f'Failed to back up {router_dic["host"]}.\n')
        print('#'*50)
        continue





