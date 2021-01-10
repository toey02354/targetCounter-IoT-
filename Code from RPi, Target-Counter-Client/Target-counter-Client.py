import US_Left
import US_Right
import time
import socket

Threshold = 50

def valuefunc():
    host = "192.168.10.130"
    port = 5050
    server = socket.socket()
    server.connect((host,port))
    
    while True:
        dist1 = US_Left.distance()
        dist2 = US_Right.distance()
#         print("Distance1: %.2f" %dist1)
#         print("Distance2: %.2f" %dist2)
        motion = dist1-dist2
        
        if abs(motion) < Threshold:
            message = "No motion"
            print(message)
            time.sleep(3)
            motion = 0
        elif motion<0:
            message = "Animal is approacing! Be Careful!"
            print(message)
            time.sleep(3)
            motion = 0
        else:
            message = "Animal is leaving"
            print(message)
            time.sleep(3)
            motion = 0
            
        server.send(message.encode('utf-8'))
        message_server = server.recv(1024).decode('utf-8')
        print(message_server)
    server.close()
        
 
if __name__ == '__main__':
    valuefunc()


