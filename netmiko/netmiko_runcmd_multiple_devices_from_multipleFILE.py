from netmiko import ConnectHandler

with open('devices.txt', 'r') as f:
    devices = f.read().splitlines()
    print(type(devices))
device_list = list()

for ip in devices:
    cisco_device = {
        'device_type': 'cisco_ios',
        'host': ip,
        'port': '22',
        'username': 'cisco',
        'password': 'cisco',
        'secret': '123',     # enable password
        'verbose': 'true'
    }
    device_list.append(cisco_device)
print(device_list)

for device in device_list:
    connection = ConnectHandler(**device)
    print('Entering the enable mode...')
    connection.enable()

    file = input(f'Enter the configuration file (use a valid path) for {device["host"]}: ')
    output = connection.send_config_from_file(file)
    print(output)

    print(f'Closing connection device {device["host"]}')
    connection.disconnect()
