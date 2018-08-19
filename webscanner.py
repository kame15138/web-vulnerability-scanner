#!/usr/bin/env python
import socket
import subprocess
import sys
import os
import portdetail
from datetime import datetime
# Clear the screen
subprocess.call('clear', shell=True)

# Ask for input
scan_name=input("enter target site name:")
remoteServer    = input("Enter a remote host to scan: ")
remoteServerIP  = socket.gethostbyname(remoteServer)
#scan choice

choice=input("select\n1.Full scan\n2.custom scan\n ")
#starting scan
t1 = datetime.now()
if choice==1:
        #creating log
        log=list()
	sysname=os.getlogin()
	directory="/home/"+sysname+"/webscanner"
	if not os.path.exists(directory):
	    os.makedirs(directory)
        #starting full scan
	subprocess.call('clear', shell=True)
        print("-" * 60)
        print("Please wait, scanning remote host", remoteServerIP)
        print("-" * 60)
	try:
	    for port in range(1,25):  
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
		    k=portdetail.portdetail(port)
                    print(k)
                    log.append(k)
		sock.close()
            #writing to the log file
	    f=open(directory+"/"+scan_name,'w')
            log="".join(log)
	    f.write(log)
	    f.close()
	except KeyboardInterrupt:
	    print "You pressed Ctrl+C"
	    sys.exit()

	except socket.gaierror:
	    print 'Hostname could not be resolved. Exiting'
	    sys.exit()

	except socket.error:
	    print "Couldn't connect to server"
	    sys.exit()
else:
    subprocess.call('clear', shell=True)
    print("-" * 60)
    print("Please wait, scanning remote host", remoteServerIP)
    print("-" * 60)
    try:
      cust_ports=input("Enter the ports").split(" ")
      for i in range(len(cust_ports)):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP,int(cust_ports[i])))
        if result == 0:
            print("Port",cust_ports[i],"open")
	sock.close()
    except KeyboardInterrupt:
		    print "You pressed Ctrl+C"
		    sys.exit()

    except socket.gaierror:
		    print 'Hostname could not be resolved. Exiting'
		    sys.exit()

    except socket.error:
		    print "Couldn't connect to server"
		    sys.exit()
          
t2 = datetime.now()
print(t2)
#scan time
total =  t2 - t1

#completion
print("Scanning Completed in: ",total)
