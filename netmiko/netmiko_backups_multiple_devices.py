from netmiko import ConnectHandler

with open('devices.txt', 'r') as f:
    devices = f.read().splitlines()
    #print(type(devices))
device_list = list()

for ip in devices:
    cisco_device = {
        'device_type': 'cisco_ios',
        'host': ip,
        'port': '22',
        'username': 'cisco',
        'password': 'cisco',
        'secret': '123',     #enable password
        'verbose': 'true'
    }
    device_list.append(cisco_device)
#print(device_list)

for device in device_list:
    connection = ConnectHandler(**device)
    print('Entering the enable mode...')
    connection.enable()

    output = connection.send_command('show run')
    output = output.splitlines()[6:-1]
    output = '\n'.join(output)
    #print(output)

    from datetime import datetime
    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day
    filename = f'{device["host"]}_{year}-{month}-{day}.txt'

    with open(filename, 'w') as f:
        f.write(output)

    print(f'Closing connection device {device["host"]}')
    connection.disconnect()
    print('#'*50)
