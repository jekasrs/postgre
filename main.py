import sys
from ssh_functions import ssh_connect
from ssh_settings import ssh_settings


def main():
    if len(sys.argv) != 2:
        print("Input command with ip argument, example: python script.py <ip>", file=sys.stderr)
        sys.exit(1)
    ip = sys.argv[1]

    port = input("Enter port: ")
    username = input("Enter username: ")
    password = input("Enter password: ")

    ssh_settings['ip'] = ip
    ssh_settings['port'] = port
    ssh_settings['username'] = username
    ssh_settings['password'] = password

    client = ssh_connect(ssh_settings)
    if client is None:
        print("Unsuccessful connection, see error above this message", file=sys.stderr)
    else:
        _, stdout, _ = client.exec_command('ls -a')
        print(stdout.read().decode("utf-8"))
        client.close()


if __name__ == '__main__':
    main()
