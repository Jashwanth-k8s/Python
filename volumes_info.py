#!/usr/bin/python3
import os
import json
#Collecting json data
myjson_data=os.popen("aws ec2 describe-volumes").read()

#converting json to dictonay
mydict_data=json.loads(str(myjson_data))

#Creating the file
file1=open("/tmp/volumeinfo.txt","w")
#Printing the volume information
print("SNO\tVOLUME_ID\tSIZE",end="",file=file1)
print("\n",end="",file=file1)
for vol in range(len(mydict_data["Volumes"])):
    print (vol+1,mydict_data["Volumes"][vol]["VolumeId"], mydict_data["Volumes"][vol]["Size"],end="",file=file1)
    print("\n",end="",file=file1)
file1.close()
