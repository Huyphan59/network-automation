from napalm import get_network_driver


driver = get_network_driver('ios')
optional_args = {'secret': 'cisco123'}

ios = driver('192.168.1.30', 'admin', 'cisco123', optional_args=optional_args)
ios.open()

ios.load_merge_candidate('acl.txt')
diff = ios.compare_config()
# if len(diff) > 0:
#     print(diff)
#     answer = input('Commit changes? <yes|no>')
#     if answer == 'yes':
#         ios.commit_config()
#         print('Done')
#     else:
#         print('No changes required.')
#         ios.discard_config()
answer = input('Rollback?<yes|no>')
if answer == 'yes':
    print('Rolling back...')
    ios.rollback()
    print('Done')


ios.close()