# execute comment very slow because: no lam theo thu tu


import myparamiko
from datetime import datetime
import threading


def backup(router):
    client = myparamiko.connect(**router)

    shell = myparamiko.get_shell(client)
    myparamiko.send_command(shell, 'enable')
    myparamiko.send_command(shell, '123')
    myparamiko.send_command(shell, 'terminal length 0')
    myparamiko.send_command(shell, 'show run')
    output = myparamiko.show(shell)
    # print(output)

    output_list = output.splitlines()
    # print(output_list)
    output_list = output_list[11:-1]
    # print(output_list)

    output = '\n'.join(output_list)
    # print(output)

    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day

    filename = f'{router["server_ip"]}_{year}-{month}-{day}.txt'

    with open(filename, 'w') as f:
        f.write(output)
    myparamiko.close(client)


router1 = {'server_ip': '192.168.1.10', 'server_port': '22', 'user': 'cisco', 'passwd': 'cisco'}
router2 = {'server_ip': '192.168.1.20', 'server_port': '22', 'user': 'cisco', 'passwd': 'cisco'}
router3 = {'server_ip': '192.168.1.30', 'server_port': '22', 'user': 'cisco', 'passwd': 'cisco'}
routers = [router1, router2, router3]

threads = list()
for router in routers:
    th = threading.Thread(target=backup, args=(router,))
    threads.append(th)

for th in threads:
    th.start()
for th in threads:
    th.join()    # th.join the join method will make the main program wait for each thread to finish executing
