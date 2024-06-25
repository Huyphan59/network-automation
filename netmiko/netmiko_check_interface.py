from netmiko import ConnectHandler

cisco_device = {
    'device_type': 'cisco_ios',
    'host': '192.168.1.10',
    'port': '22',
    'username': 'admin',
    'password': 'cisco',
    'secret': 'cisco',
    'verbose': 'true'
}
connection = ConnectHandler(**cisco_device)
connection.enable()
# print(connection.find_prompt())
interface = input('Enter interface: ')

output = connection.send_command('sh ip int ' + interface).splitlines()[0]
# print(output)
cmds = ['int ' + interface, 'no shut', 'exit']
if not 'up' in output:
    print('Interface ' + interface + ' is down. Config interface up...')
    connection.send_config_set(cmds)
    print('Interface ' + interface + ' is Up')
else:
    print('Interface ' + interface + ' is Up')
print('Closing connection')
connection.disconnect()
