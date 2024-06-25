from napalm import get_network_driver
import json
driver = get_network_driver('ios')
optional_args = {'secret': 'cisco123'}
ios = driver('192.168.1.30', 'admin', 'cisco123', optional_args=optional_args)
ios.open()

# print(dir(ios))
output = ios.get_arp_table()
# with open('arp_table.txt', 'w') as f:
#     f.write(output)       # Error : write must be str, not list

#for item in output:
    #print(item)

dump = json.dumps(output, sort_keys=True, indent=4)   #  list -> str by json
#print(dump)
with open('arp_table.txt', 'w') as f:
    f.write(dump)

ios.close()
