import os
import sys
import time
def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1./10)
slowprint("Tool Spam Sms By Trần Thế Nghĩa")
time.sleep(1.0)
slowprint("[+] Install Pystyle Resources . . .")
os.system("pip3 install pystyle")
slowprint("[+]Install Successful")