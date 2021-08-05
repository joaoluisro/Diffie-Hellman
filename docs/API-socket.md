# API Socket

A principal biblioteca utilizada na implementação é a bilioteca _socket_, que fornece estruturas de dados e funções para manipulação de sockets BSD. Ela pode ser facilmente importada utilizando:
```python
import socket
```

A documentação oficial pode ser encontrada
[aqui.](https://docs.python.org/3/library/socket.html)

## Funções utilizadas

<b>_Função_</b> : ```socket.socket()```

<b>_Descrição_</b> : Cria um novo objeto socket BSD. São passados dois parâmetros que indicam o protocolo utilizado para comunicação:

`socket.AF_INET` : Indica a familia de endereços (Address Family) que o protocolo irá utilizar, neste caso *AF_INET* refere-se a familia de indereços IPv4.

`socket.SOCK_STREAM` : Indica que a comunicação utilizará o protocolo TCP.

<br />
<b>_Função_</b> : ```s.bind()```

<b>_Descrição_</b> : Associa um endereço (de acordo com a familia de endereços previamente configurada) ao socket do servidor, assim como a porta que será utilizada.

Neste caso foram passados o endereço de loopback (localhost) 127.0.0.1 e a porta 1026.

<br />
<b>_Função_</b> : ```s.connect()```

<b>_Descrição_</b> : Conecta um cliente a um servidor por meio do endereço e porta especificados. Os valores passados são iguais ao de _bind()_.

<br />
<b>_Função_</b> : ```s.accept()```

<b>_Descrição_</b> : Chamada bloqueante que aguarda uma conexão com algum cliente. Ao estabelecê-la, retorna um objeto socket que representa a conexão, assim como uma tupla com o endereço e a porta do cliente.

<br />
<b>_Função_</b> : ```s.send()```

<b>_Descrição_</b> : Envia uma mensagem por meio da abstração de socket.

<br />
<b>_Função_</b> : ```s.recv(n)```

<b>_Descrição_</b> : Recebe uma mensagem com no máximo _n_ bytes de tamanho. 
