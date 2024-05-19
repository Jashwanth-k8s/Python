#!/usr/bin/python3

import  os
print(os.popen("uname -a").read())

# We can use below method also to fecth the server information of a server#
import subprocess
val = subprocess.Popen("uname -a", stdout=subprocess.PIPE, shell=True)
(output,error)=val.communicate()
print(output)

