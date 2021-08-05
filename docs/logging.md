# Logging

O logging do sistema foi feito através de funções auxiliares contidas no arquivo _loggingutils.py_ que pode ser encontrado [aqui](loggingutils.py.txt).

Nele está descrito a classe _LogFile_, que possui alguns métodos importantes:

- ```write_log```: Escreve uma mensagem no log criado.

- ```log_recv```: Escreve uma mensagem de recebido no log criado, seguido da mensagem recebida.

- ```log_send```: Escreve a mensagem enviada no log criado.

- ```log_end```: Encerra o log criado.

## Logs de testes

Os logs de teste que utilizaram a chave correta para codificar e decodificar as mensagens são mostrados a seguir:

- [client-original.log](client-original.log.txt)
- [server1-original.log](server1-original.log.txt)

Neles, podemos acompanhar a narrativa dos dois personagens Carter e Warren, que tiveram um final trágico.

No entanto, para observar o comportamento de um agente malicioso, os logs de teste com as chaves secretas incorretas também são mostrados a seguir :


- [client-m.log](client-m.log.txt)
- [server2-m.log](server2-m.log.txt)

Os caracteres estranhos podem ser explicados pela codificação UTF-8, que interpreta bytes "fora do lugar" com símbolos de certa forma aleatória.
