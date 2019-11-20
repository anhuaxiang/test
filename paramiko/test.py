import paramiko


# ssh
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='192.168.0.210', port=22, username='root', password='root')
std_in, std_out, sed_err = ssh.exec_command('df -h')
for l in std_out:
    print(l.strip('\n'))


# sftp
transport = paramiko.Transport(('192.168.0.210', 22))
transport.connect(username='root', password='root')
sftp = paramiko.SFTPClient.from_transport(transport)
sftp.get('/home/yan/.ssh/id_rsa.pub', '/home/yan/a.txt')
sftp.put('/home/yan/a.txt', '/home/yan/aaa.txt')


# ssh transport sftp
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='192.168.0.210', port=22, username='root', password='root')
transport = ssh.get_transport()
sftp = transport.open_sftp_client()
channel = transport.open_session()
channel.settimeout(2)
channel.get_pty(term='xterm', width=80, height=24)
channel.invoke_shell()
data = channel.recv(1024).decode('utf-8', 'ignore')
print(data)
channel.send('htop')
while not channel.exit_status_ready():
    data = channel.recv(1024).decode('utf-8', 'ignore')
    if len(data) != 0:
        print(data)
    else:
        break
