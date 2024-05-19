#!/usr/bin/python3

import paramiko
import time

file1=open("serverslist","r")
k = paramiko.RSAKey.from_private_key_file("/tmp/mykey.pem")   # Here we are loading the privte key to login server#
ssh = paramiko.SSHClient()  #To run ssh to start
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
for server in file1.readlines():
    print ("============================"+server.rstrip("\n")+"=========================")
    ssh.connect(server.rstrip("\n"), username = "ec2-user", pkey = k)
    commands = ["df -hT", "uname -a", "ls -l /tmp", "lscpu", "free -h"]
    for command in commands:
        stdin, stdout, stderr = ssh.exec_command(command)
        stdout_str = stdout.read().decode('utf-8')
        time.sleep(2)
        print(stdout_str)
    ssh.close()
