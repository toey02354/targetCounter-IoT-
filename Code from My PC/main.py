import socket
from time import sleep

def  main_function():
    host = "192.168.10.130"
    port = 5050
    server = socket.socket()
    server.connect((host,port))

    while True:
        with open("data-from-arduino.txt", "r") as f:
            read_line = f.read().splitlines()
            last_line = read_line[-1]
            print(last_line)
        f.close()

        server.send(last_line.encode('utf-8'))
        message_server = server.recv(1024).decode('utf-8')
        print(message_server)
        sleep(3)
    server.close()


if __name__ == "__main__":
    main_function()
