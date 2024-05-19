#!/usr/bin/python3

import paramiko
import time
import getpass

# Prompt user for password
mypass = getpass.getpass()

# Open the file containing the list of servers
servers = open("serverslist", "r")

# Initialize the SSH client
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Iterate over each server in the list
for server in servers.readlines():
    print("============================" + server.rstrip("\n") + "=========================")
    
    try:
        # Connect to the server using username and password
        ssh.connect(server.strip(), username="ec2-user", password=mypass)
        
        # List of commands to execute on the server
        commands = ["df -hT", "uname -a", "ls -l /tmp", "lscpu", "free -h"]
        
        # Execute each command
        for command in commands:
            stdin, stdout, stderr = ssh.exec_command(command)
            stdout_str = stdout.read().decode('utf-8')
            time.sleep(2)
            print(stdout_str)
        
        # Close the SSH connection
        ssh.close()
    
    except Exception as e:
        print(f"Error connecting to {server.strip()}: {str(e)}")

# Close the file containing the list of servers
servers.close()

