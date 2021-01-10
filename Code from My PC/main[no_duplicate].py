# import json
import socket
from time import sleep

# def Convert_function():
#     with open("data-copy-as-json.json", "w+") as g:
#         with open("data-from-arduino.txt","r") as f:
#             g.write(f.read())
#             print(f.read())
#             f.close()
#             g.close()

def  main_function():
    # host = "192.168.10.118"
    host = "192.168.10.130"
    port = 5050
    server = socket.socket()
    server.connect((host,port))

    check_data = "To check data"
    nonmessage = "No motion"

    while True:
        with open("data-from-arduino.txt", "r") as f:
            read_line = f.read().splitlines()
            last_line = read_line[-1]
            #print(last_line)
        f.close()

        if check_data != last_line:
            server.send(last_line.encode('utf-8'))
            check_data = last_line
        else:
            server.send(nonmessage.encode('utf-8'))
        message_server = server.recv(1024).decode('utf-8')
        print(message_server)
        sleep(3)
    server.close()


if __name__ == "__main__":
    # Convert_function()
    main_function()
