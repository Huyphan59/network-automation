from netmiko import ConnectHandler


with open('devices.txt', 'r') as f:
    device_content = f.read().splitlines()

devices = []
for item in device_content:
    tmp = item.split(':')
    devices.append(tmp)


for device in devices:
    device = {
        'device_type': device[0],
        'ip': device[1],
        'username': device[2],
        'password': device[3],
        'port': 22,
        'secret': device[3],
        'verbose': True
    }
    print(f'Connecting to {device["ip"]}')
    connection = ConnectHandler(**device)
    if not connection.check_enable_mode():
        connection.enable()
    file_config = input(f'Enter file config for {device["ip"]}: ')
    connection.send_config_from_file(file_config)
    print('Closing connection...')
    connection.disconnect()
