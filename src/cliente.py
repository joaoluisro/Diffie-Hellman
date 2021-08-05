#   Programa cliente do trabalho prático.
#   Lê o arquivo 'data/client-dialog.txt' e envia ao servidor
#
#   Autor: João Luis Ribeiro Okimoto - GRR20186983
#   Disciplina: Redes de Computadores II - CI1061
#   Data da última atualização: 04/08/2021

import socket
import loggingutils as log
import encryption as cryp
import time
from random import randint

SERVER_IP_ADDR = '127.0.0.1'
PORT = 1026

# Gera chave privada do cliente
PRIVATE_KEY = randint(1, 10**5)

# Gera os parâmetros de Diffie-Hellman
n, g = randint(1, 10**9), randint(1, 10*5)

LOG_FILE = log.LogFile("../logs/client.log",0)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Se conecta ao servidor
    s.connect((SERVER_IP_ADDR, PORT))
    LOG_FILE.write_log("Conexão com servidor estabelecida.")

    # envia as chaves públicas
    LOG_FILE.write_log("Enviando as chaves públicas geradas ...")
    public_keys = (str(n) + "," + str(g) + "\n")
    s.send(public_keys.encode())
    LOG_FILE.log_send(public_keys)

    # recebe o primeiro resultado de Diffie-Hellman
    LOG_FILE.write_log("Aguardando a chave do servidor ...")
    server_key = int(s.recv(1024).decode())
    LOG_FILE.log_recv(str(server_key))

    # calcula (g ^chave mod n) e envia
    LOG_FILE.write_log("Enviando a minha chave (cliente) ...")
    my_key = str((g ** PRIVATE_KEY) % n)
    s.send(my_key.encode())
    LOG_FILE.log_send(my_key)

    # calcula a chave secreta
    LOG_FILE.write_log("Chave secreta estabelecida, comunicação criptografada pode iniciar.")
    SECRET_KEY = (server_key ** PRIVATE_KEY) % n

    # Abre o arquivo de dados a ser enviado
    with open("../data/client-dialog.txt", "r") as f:
        lines = f.readlines()
        for line in lines:

            encrypted_msg = cryp.encrypt(line, SECRET_KEY)
            # envia cada linha
            s.send(encrypted_msg)
            LOG_FILE.log_send(line)

            encrypted_reply = s.recv(1024)
            reply = cryp.decrypt(encrypted_reply, SECRET_KEY)
            LOG_FILE.log_recv(reply)

            if 'fin' in reply:
                break
    f.close()
