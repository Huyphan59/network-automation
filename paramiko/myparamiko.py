import time
import paramiko


def connect(server_ip, server_port, user, passwd):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print(f'Connecting to {server_ip}...')
    ssh_client.connect(server_ip, server_port, user, passwd, look_for_keys=False, allow_agent=False)
    return ssh_client


def get_shell(ssh_client):
    shell = ssh_client.invoke_shell()
    return shell


def send_command(shell, command, timeout=1):
    print(f'Sending command: {command}')
    shell.send(command+'\n')
    time.sleep(timeout)


def show(shell, n=10000):
    output = shell.recv(n)
    return output.decode()


def close(ssh_client):
    if ssh_client.get_transport().is_active() == True:
        print('Closing connection')
        ssh_client.close()


if __name__ == '__main__':
    router = {'server_ip': '192.168.1.10', 'server_port': '22', 'user': 'cisco', 'passwd': 'cisco'}
    client = connect(**router)
    shell = get_shell(client)
    send_command(shell, 'enable')
    send_command(shell, '123')
    send_command(shell, 'terminal length 0')
    send_command(shell, 'sh ip int bri')
    output = show(shell)
    print(output)

