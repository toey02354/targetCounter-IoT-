def readdata():
    with open("data-from-arduino.txt","r") as f:
        read_line = f.read().splitlines()
        last_line = read_line[-1]
    f.close()
    print(last_line+"\n")
    
if __name__ == '__main__':
    while True:
        readdata()