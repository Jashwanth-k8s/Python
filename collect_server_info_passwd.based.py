#!/usr/bin/python3

import paramiko
import time
import getpass
mypass = getpass.getpass() 
servers = open("serverslist","r")
ssh = paramiko.SSHClient()  #To run ssh to start
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
for i in server.readlines():
    print ("============================"+server.rstrip("\n")+"=========================")
    #ssh.connect(server.rstrip("\n"), username = "ec2-user", pkey = k)
     ssh.connect(i.strip("\n"), username = "ec2-user", password = mypass)
    commands = ["df -hT", "uname -a", "ls -l /tmp", "lscpu", "free -h"]
    for command in commands:
        stdin, stdout, stderr = ssh.exec_command(command)
        stdout_str = stdout.read().decode('utf-8')
        time.sleep(2)
        print(stdout_str)
    ssh.close()
