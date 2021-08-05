# Introdução

Neste trabalho, foi implementado um sistema cliente-servidor que comunica uma pequena passagem do conto _O Depoimento de Randolph Carter_ de Howard Philips Lovecraft, no qual dois personagens conversam através de um rádio. Esse sistema foi implementado de maneira criptografada, utilizando o algoritmo de Diffie-Hellman para estabelecer uma chave secreta.

## Modelo Cliente-Servidor

O modelo cliente-servidor serve de base para a comunicação entre processos por meio de uma rede. Nele, existem duas importantes entidades:

- <b> Servidor :</b> Um processo que fica em modo de escuta para atender pedidos de clientes, ele está em constante execução e aguarda uma nova comunicação.

- <b> Cliente :</b> Processo que inicia uma comunicação com algum servidor e é atendido por ele.

Isso é ilustrado na figura abaixo.

![](1.svg.png)
<center>
<b>Fonte:</b> https://en.wikipedia.org/wiki/Client%E2%80%93server_model
</center>

Um servidor pode estabelecer conexão com múltiplos processos, não limitando-se somente a um único cliente.

## Implementação

A implementação do sistema apresentado foi feita de forma bastante simples, no formato _request/reply_. Isso significa que um cliente conecta-se a um servidor, manda uma mensagem e aguarda uma resposta. A conexão encerra-se quando não há mais mensagens a serem trocadas.

Para testar o sistema, o cliente envia (sequencialmente):

```
O que é Warren?
Warren, o que é? O que é?
Warren me responda!
Warren, porfavor, o que você encontrou?
Warren, aguente firme! Estou descendo!
O que..
Warren! Warren! Responda-me - Você está ai?
```

E o servidor responde:

```
Deus! Se você pudesse ver o que eu estou vendo!
Carter, é terrível - monstruoso - inacreditável!
Não posso contar Carter! É tão absolutamente além do pensamento! Não ouso lhe dizer - homem algum pode conhecer isso e continuar vivendo! Meu deus! Eu nunca sonhei com isso!
Carter! Pelo amor de Deus, ponha a laje de volta e saia daqui se puder! Rápido! Largue tudo e saia! É sua única chance! Faça o que eu digo e não peça explicações!
Não! Você não compreende! É tarde demais - e é minha culpa. Devolva a laje e corra - não há nada que você ou qualquer outro possa fazer agora!
Rápido - antes que seja tarde!
IDIOTA! WARREN ESTÁ MORTO!
```

Re-criando o diálogo do conto mencionado.
