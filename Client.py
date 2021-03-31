'''
This program is for a Fluke Endurance. It is supposed to send commands
and recieve data. I believe I (SW) was able to query the spot laser status and 
turn the laser on and off. When requesting data, I was able to get a response,
but was not able to figure out what the response was. 
Currently active code was the most succesful attempt.
'''


import socket   
import time
import sys

host = '192.168.0.132'
port = 6363
#create socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(3)# 3 second timeout on commands
except socket.error:
    print ('Failed to create socket')
    sys.exit()
print ('Socket Created')

try:
    remote_ip = socket.gethostbyname( host )
    s.connect((host, port))

except socket.gaierror:
    print ('Hostname could not be resolved. Exiting')
    sys.exit()
print ('Socket Connected to ' + host + ' on ip ' + remote_ip)

try :    
    
   
    command = b'?$\r\n' #Query statis of spot laser    
    s.send(command) #string format
   
   '''
        # I do not remember if this one worked.
        command = input('enter command:')
    command+="'\r\n'"
    s.send(bytes(command.encode())) #string format
    '''
    
    print('The following command was sent')
    print(command)

    print ('command sent successfully') #was it the correct command?
    time.sleep(1)
    print ('Getting data')
    #usually stops here waiting for data
    time.sleep(2)
    
    
    
    data = s.recv(2048)
    print('Endurance returned the following')
    print (data.decode('ascii'))
    print (data)
    print( '\n')
    '''
    while data:
        data = s.recv(1024)
        print (data)
    '''
    ############
    command = b'?XU\r\n' #Query statis of spot laser    
    s.send(command) #string format
    '''
    
    command = input('enter command:')
    command+="'\r\n'"
    s.send(bytes(command.encode())) #string format
    '''
    
    print('The following command was sent')
    print(command)

    print ('command sent successfully') #was it the correct command?
    time.sleep(1)
    print ('Getting data')
    #usually stops here waiting for data
    #time.sleep(2)
    data = s.recv(2048)
    print('Endurance returned the following')
    print (data.decode('ascii'))
    print (data)
    print( '\n')


except socket.error:
    #Send failed
    print ('Send failed')
    
    s.close()
    sys.exit()
