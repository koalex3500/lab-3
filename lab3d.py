#!/usr/bin/env python3

import subprocess

#using the function freespace to help run a shell command to display disk space and filters
def free_space():
#this is the shell command
 process = subprocess.Popen(["df -h | grep '/$' | awk '{print $4} '"], stdout=subprocess.PIPE, shell=True)
#this is to capture output and the errors
 output, error = process.communicate()
#this will return the decoded output
 return output.decode('utf-8').strip()
