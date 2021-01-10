import socket

def Server_func():
    hnp = ("192.168.10.118",5050)
    serv = socket.socket()
    serv.bind(hnp)

    serv.listen(1)
    print("Waiting for the connection...")

    target_ct,addr = serv.accept()
    print("Connected from : " + str(addr))

    while True:
        data_target_ct = target_ct.recv(1024).decode('utf-8')
        print(data_target_ct)
        reply_message = "I've already received the data."
        target_ct.send(reply_message.encode('utf-8'))
    target_ct.close()

if __name__ == "__main__":
    Server_func()
