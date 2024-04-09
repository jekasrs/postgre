import paramiko
import sys

# Return: an SSHClient object if connection is successful, None otherwise
def ssh_connect(ssh_settings):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=ssh_settings['ip'],
                       port=ssh_settings['port'],
                       username=ssh_settings['username'],
                       password=ssh_settings['password'])
        return client
    except Exception as e:
        print(f"Error connecting to {ssh_settings['ip']}: {e}", file=sys.stderr)
        return None
