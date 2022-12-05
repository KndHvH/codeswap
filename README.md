# CodeSwap

## Sobre

Este é um projeto pessoal para poder testar e por meu conhecimento dos recentes cursos realizados em prática.

Consiste em um programa que tem como funcão principal armazenar textos de uma forma segura e criptografada.

Cada vez que um texto e submetido, uma chave é gerada e criptografa o texto com base na chave, o usuario entao guarda sua chave e na base de dados é guardado apenas o texto criptografado.

Podemos ver no exemplo a seguir que o mesmo texto é submetido 2 vezes, e nas duas a chave gerada é diferente,
consequentemente gerando textos completamente diferentes.


## Exemplo:

#### Texto exemplo: 
*"Zenit Polar é um sistema simples de criptografia, que consiste na substituição das letras de uma palavra pela sua correspondente no nome ZENIT POLAR."*

#### Primeira vez submetido:

Key:

    key_tifugabitece:39S617EM^uD@8sRKIntwZqcAQY*rTJljp&h45Wx%zi-B2C.VH#!fXNPabymGUF \e$v0o?O,kdgL

Output:

    {
    "code": [
             {
              "title": "tifugabitece",
              "file": "9C5UWBd#@g^BéBT%BpUpWC%gBpU%s@CpBPCB6^UsW#a^gOUgXBSTCB6#5pUpWCB5gBpTLpWUWTUçã#BPgpB@CW^gpBPCBT%gBsg@gV^gBsC@gBpTgB6#^^Cps#5PC5WCB5#B5#%CB9Yk4uBdfb1&$"
             }
            ]
    }
  
#### Segunda vez submetido:

Key:

    key_mobumupadisuta:Td12,ew-t4q8rDSu!7Hc^hNEU\Rzxsaf%BLkAy#n9v@jCl*OKYP?$b3V.FXmW0p6QJGMoI&Zi g5

Output:
    
    {
    "code": [
             {
              "title": "mobumupadisuta",
              "file": "$UXbz3IYQ8f3é3L93qbqzU983qb9jQUq3^U3TfbjzYVf8rb8E3sLU3TYXqbqzU3X83qLiqzbzLbçãY3^8q3QUzf8q3^U3L983j8Q8Wf83jUQ83qL83TYffUqjYX^UXzU3XY3XY9U3$,2Pc3IGu7-5"
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

