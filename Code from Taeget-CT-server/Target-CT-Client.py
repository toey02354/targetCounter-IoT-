# import json
import socket

# def Convert_function():
#     with open("data-copy-as-json.json", "w+") as g:
#         with open("data-from-arduino.txt","r") as f:
#             g.write(f.read())
#             print(f.read())
#             f.close()
#             g.close()

def  main_function():
    host = "192.168.30.123"
    port = 5050
    server = socket.socket()
    server.connect((host,port))


    with open("data-from-arduino.txt","r") as f:
        read_line = f.read().splitlines()
        last_line = read_line[-1]
        print(last_line)
    f.close()

    check_lastline = ["Right to Left","Left to Right"]

    while last_line in check_lastline:
        server.send(last_line.encode('utf-8'))
        message_server = server.recv(1024).decode('utf-8')
        print(message_server)
    server.close()

if __name__ == "__main__":
    # Convert_function()
    main_function()