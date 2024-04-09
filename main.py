import paramiko

host = 'localhost'
user = 'root'
password = 'root'
port = 2222

if __name__ == '__main__':
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=host, username=user, password=password, port=port)
    stdin, stdout, stderr = client.exec_command('ls -a')
    data = stdout.read().decode("utf-8")
    print(data)
    client.close()
