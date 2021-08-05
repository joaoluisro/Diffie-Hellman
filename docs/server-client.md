# Implementação do sistema

A partir da API de sockets e os recursos fornecidos pela linguagem Python, o sistema cliente-servidor criptografado foi implementado. A comunicação ocorre por meio dos padrões TCP/IP, que é definida na criação dos sockets de cada processo.

O sistema pode ser executado a partir dos comandos:

```bash
python3 servidor.py
python3 cliente.py
```

O servidor inicialmente é associado ao endereço 127.0.0.1 (localhost) e a porta 1026 através da criação de um socket e pela chamada da função _bind_. Em seguida, ele é colocado em modo de escuta através de _listen_, que permite identificá-lo como servidor. Após isso, o servidor entra em um laço infinito que aguarda uma conexão com algum cliente.

O cliente também cria um socket para comunicar-se, no entanto, utiliza a chamada _connect_ para conectar-se ao servidor, informando o endereço e porta de destino.

Depois que cliente e servidor estabeleceram a conexão, o procedimento de estabelecimento da chave secreta de criptografia ocorre como descrito na seção anterior.

Quando cada processo já possui a chave secreta, a comunicação ocorre por meio do padrão request/reply. Neste padrão, servidor e cliente trocam mensagens de forma sequencial, isto é, o cliente envia uma mensagem e o servidor responde, até que não existam mais mensagens a serem trocadas.

A implementação do servidor pode ser encontrada no arquivo _servidor.py_ e pode ser acessado [aqui](servidor.py.txt).

A implementação do cliente pode ser encontrada no arquivo _cliente.py_ e pode ser acessado [aqui](cliente.py.txt).
