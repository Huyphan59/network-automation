from napalm import get_network_driver
import json

driver = get_network_driver('ios')
optional_args = {'secret': 'cisco123'}

ios = driver('192.168.1.30', 'admin', 'cisco123', optional_args=optional_args)
ios.open()


ios.load_replace_candidate('config.txt')   # create filename candidate.txt in disk0: memory
diff = ios.compare_config()
# print(diff)
if len(diff) > 0:
    print('Commit changes...')
    ios.commit_config()
    print('Done')
else:
    print('No changes required...')
    ios.discard_config()

ios.close()
