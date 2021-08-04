import socket
import loggingutils as log
import encryption as cryp
from random import randint

SERVER_IP_ADDR = '127.0.0.1'
PORT = 1026

# Gera a chave privada do servidor
PRIVATE_KEY = randint(1, 10**5)

# socket.socket() -> cria um objeto socket
# AF_INET         -> Address Family InterNET (IPv4)
# SOCK_STREAM     -> tipo de socket TCP
# Isso significa que usaremos comunicação por TCP/IP.

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    # bind() -> associa o socket com o endereço e número da porta
    s.bind((SERVER_IP_ADDR, PORT))

    # seta o socket para modo de escuta (servidor)
    s.listen()

    i = 1

    # laço no qual aguardamos uma conexão com algum cliente

    while True:

        k = 0
        # accept() -> bloqueante, aguarda uma conexão de um cliente
        # retorna um objeto socket que representa a conexão
        # e uma tupla com o endereço e porta do cliente
        conn, addr = s.accept()

        # Abre um novo log após aceitar uma conexão
        LOG_FILE = log.LogFile("../logs/server" + str(i)+".log",i)
        LOG_FILE.write_log("Conexão com processo " + str(i) + " estabelecida.")
        # Processa a conexão
        with conn:

            LOG_FILE.write_log("Aguardando as chaves públicas ...")
            # recebe as chaves públicas n e g
            public_keys = conn.recv(1024).decode()
            n, g = int(public_keys.split(",")[0]), int(public_keys.split(",")[1])
            LOG_FILE.log_recv(public_keys)
            LOG_FILE.write_log("Chaves públicas recebidas.")


            # calcula (g ^chave mod n) e envia
            LOG_FILE.write_log("Enviando a primeira parte da chave ...")
            my_key = str((g ** PRIVATE_KEY) % n)
            conn.send(my_key.encode())
            LOG_FILE.log_send(my_key)

            # recebe o calculo do cliente
            LOG_FILE.write_log("Aguardando a segunda parte da chave ...")
            client_key = int(conn.recv(1024).decode())
            LOG_FILE.log_recv(str(client_key))

            # calcula a chave secreta
            SECRET_KEY = (client_key ** PRIVATE_KEY) % n
            LOG_FILE.write_log("Chave secreta estabelecida, comunicação criptografada pode iniciar.")
            sv_file = open("../data/server_dialog.txt", "r")
            dialog = sv_file.readlines()

            # Depois do estabelecimento da chave secreta, comunicação inicia
            while True:

                # recebe uma mensagem criptografada
                encrypted_msg = conn.recv(1024)

                # decodifica ela
                msg = cryp.decrypt(encrypted_msg, SECRET_KEY)

                # Conexão encerra quando o cliente envia b''
                if not msg or k >= len(dialog):
                    LOG_FILE.end_log()
                    sv_file.close()
                    break
                # Escreve no log
                LOG_FILE.log_recv(msg)

                # Codifica a resposta e envia
                encrypted_reply = cryp.encrypt(dialog[k], SECRET_KEY)
                conn.send(encrypted_reply)
                LOG_FILE.log_send(dialog[k])
                k += 1

        i += 1
