# CodeSwap

## Sobre

Este é um projeto pessoal para poder testar e por meu conhecimento dos recentes cursos realizados em prática.

Consiste em um programa que tem como funcão principal armazenar textos de uma forma segura e criptografada.

Cada vez que um texto e submetido, uma chave é gerada e criptografa o texto com base na chave, o usuario entao guarda sua chave e na base de dados é guardado apenas o texto criptografado.

Podemos ver no exemplo a seguir que o mesmo texto é submetido 2 vezes, e nas duas a chave gerada é diferente,
consequentemente gerando textos criptografados completamente distintos e dependentes da chave.


## Exemplo:

#### Texto exemplo: 
*"Zenit Polar é um sistema simples de criptografia, que consiste na substituição das letras de uma palavra pela sua correspondente no nome ZENIT POLAR."*

#### Primeira vez submetido:

Key:

    key_cudagosi:Jn-O.bigX6EzG9r7SKu,2t?aFI%m ^Zqyk$UDQMHfC0deR14@PxwNl3LcTYjv5p&o!B8#h*AWVs\_

DB:

    {
        "code": [
            {
                "title": "cudagosi",
                "file": "z&2I-6#RW.k6\u00e96QX6LIL-&X.6LIXdW&L6p&6\\kId-R%k.jI.J6GQ&6\\R2LIL-&62.6LQFL-I-QI\u00e7\u00e3R6p.L6W&-k.L6p&6QX.6d.W.Ck.6d&W.6LQ.6\\Rkk&LdR2p&2-&62R62RX&6z^AiM6#?sNoa"
            }
        ]
    }
  
#### Segunda vez submetido:

Key:

    key_togulapusa:jX3b@y2dCUaPev,I%LBYpWDEoVZH9MGO0?76lg^r&\-JFk*.#ctfwKN5hzQATSuq$! R81mxni4s_

Output:
    
    {
        "code": [
            {
                "title": "cudagosi",
                "file": "z&2I-6#RW.k6\u00e96QX6LIL-&X.6LIXdW&L6p&6\\kId-R%k.jI.J6GQ&6\\R2LIL-&62.6LQFL-I-QI\u00e7\u00e3R6p.L6W&-k.L6p&6QX.6d.W.Ck.6d&W.6LQ.6\\Rkk&LdR2p&2-&62R62RX&6z^AiM6#?sNoa"
            },
            {
                "title": "togulapusa",
                "file": "dOKN1.GyLMQ.\u00e9.Jf.hNh1OfM.hNfXLOh.ZO.8QNX1yBQMmNM?.FJO.8yKhNh1O.KM.hJDh1N1JN\u00e7\u00e3y.ZMh.LO1QMh.ZO.JfM.XMLM0QM.XOLM.hJM.8yQQOhXyKZOK1O.Ky.KyfO.d@i7\\.Gel&# "
            }
        ]
    }
    

## Funções atualmente:

- Adicionar Texto
- Ler um Texto
- Editar texto
- Apagar texto

## Próximos Passos:
- Enviar chave para email pessoal
- Guardar textos em banco de dados

