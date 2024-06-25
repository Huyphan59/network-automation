from netmiko import ConnectHandler
import getpass

password = getpass.getpass('Enter password:')

arista_device = {
    'device_type': 'arista_eos',
    'ip': '192.168.1.10',
    'username': 'admin',
    'password': password,
    'port': 22,
    'secret': password,
    'verbose': True
}
connection = ConnectHandler(**arista_device)
if not connection.check_enable_mode():
    connection.enable()

output = connection.send_config_from_file('arista1_config.txt')
print(output)

print('Closing connection...')
connection.disconnect()
