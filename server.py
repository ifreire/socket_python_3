import socket

def Main():
    host = "10.0.2.15" #"127.0.0.1"
    port = 5000

    mySocket = socket.socket()
    mySocket.bind((host, port))

    mySocket.listen(1)
    conn, addr = mySocket.accept()
    print("Connection from: " + str(addr))

    saldo = 0
    opcao = "0"
    lista_opcoes = ""
    menu_inicial = "- Para voltar ao menu inicial, digite 0."
    lista_0 = ["- Para recarregar seus créditos, digite 1.", "- Quer saber seu saldo? digite 2."]
    lista_1 = ["- Para recarregar 10 reais, digite 3.", "- Para recarregar 20 reais, digite 4.", "- Para recarregar 30 reais, digite 5.", menu_inicial]
    lista_2 = ["- Seu saldo é: @saldo@ reais.", menu_inicial]

    while True:
        if opcao == "0":
            lista_opcoes = ""
            for op in lista_0:
                lista_opcoes += op + "\n"

        elif opcao == "1":
            lista_opcoes = ""
            for op in lista_1:
                lista_opcoes += op + "\n"

        elif opcao == "2":
            lista_opcoes = ""
            for op in lista_2:
                op = op.replace("@saldo@", str(saldo))
                lista_opcoes += op + "\n"

        elif opcao == "3":
            lista_opcoes = ""
            saldo += 10
            for op in lista_2:
                op = op.replace("@saldo@", str(saldo))
                lista_opcoes += op + "\n"

        elif opcao == "4":
            lista_opcoes = ""
            saldo += 20
            for op in lista_2:
                op = op.replace("@saldo@", str(saldo))
                lista_opcoes += op + "\n"

        elif opcao == "5":
            lista_opcoes = ""
            saldo += 30
            for op in lista_2:
                op = op.replace("@saldo@", str(saldo))
                lista_opcoes += op + "\n"

        else:
            lista_opcoes = "Opção inválida!\n" + lista_opcoes


        conn.send(lista_opcoes.encode())
        data = conn.recv(1024).decode()

        if not data:
            break

        opcao = data

        print("from connected  user: " + str(data))

    conn.close()


if __name__ == '__main__':
    Main()
