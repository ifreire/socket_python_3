import socket

def Main():
    host = '127.0.0.1'
    port = 5000

    mySocket = socket.socket()
    mySocket.connect((host, port))

    print("\nPara sair digite 'q'.\n")

    message = 'a'

    while message != 'q':
        data = mySocket.recv(1024).decode()

        print(data)
        message = input(" -> ")

        mySocket.send(message.encode())

    mySocket.close()


if __name__ == '__main__':
    Main()