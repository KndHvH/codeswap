# Readme Language

 - [Portuguese](#README.md)
 - [English](/README-en.md)

# CodeSwap

Este é um projeto pessoal para poder testar e por meu conhecimento dos recentes cursos realizados em prática.
Consiste em um programa que tem como função principal armazenar localmente textos e informações sensíveis de uma forma fácil e segura.

![](codeswap-showcase.gif)

## Conteúdo
- [Readme Language](#readme-language)
- [CodeSwap](#codeswap)
  - [Conteúdo](#conteúdo)
  - [Sobre](#sobre)
  - [Instalação](#instalação)
  - [Funcionalidades](#funcionalidades)
    - [Adicione](#adicione)
      - [Arquivo exemplo](#arquivo-exemplo)
      - [Contexto](#contexto)
      - [Primeira vez submetido](#primeira-vez-submetido)
      - [Segunda vez submetido](#segunda-vez-submetido)
    - [Leia](#leia)
      - [Exemplo](#exemplo)
    - [Edite](#edite)
    - [Delete](#delete)
    - [Liste](#liste)
    - [Backup](#backup)
  - [Como Funciona?](#como-funciona)
    - [Inspiração](#inspiração)
    - [Key](#key)
    - [Senha](#senha)
  - [Próximos Passos](#próximos-passos)

## Sobre

O grande diferencial do CodeSwap, é que o texto armazenado localmente é impossível de ser lido sem a senha criada pelo usuário, e essa mesma senha não é armazenada em nenhum lugar!


Outra questão positiva, é que não existe uma senha "certa" ou "errada", a lógica do CodeSwap permite que o usuário tente ler um documento mesmo que a senha esteja incorreta, porém o texto que esse usuário irá ler, será o mesmo guardado no banco de dados que ainda não foi decifrado, uma vez que a senha é uma apenas uma engrenagem no funcionamento do programa como um todo!


## Instalação

    $ git clone https://www.github.com/kndhvh/codeswap.git
    $ cd codeswap
    $ pip install -e .

## Funcionalidades
### Adicione

Adicione um arquivo na base de dados, precisa criar um título e em sequida de uma senha.

    $ cswap file
    or
    $ cswap file -t titulo_do_arquivo

#### Arquivo exemplo
 
*"Zenit Polar é um sistema simples de criptografia, que consiste na substituição das letras de uma palavra pela sua correspondente no nome ZENIT POLAR."*

#### Contexto

Primeiramente insira uma senha de sua escolha. Em seguida escreva o texto no editor que deseja armazenar.
Cada vez que um texto é submetido, uma chave é gerada aleatoriamente, então o texto é criptografado com base na chave, a chave então é criptografada com base na senha que o usuário escolheu e então no banco de dados é armazenado o título, a chave e o texto.

Podemos ver no exemplo a seguir que o mesmo texto é submetido 2 vezes com a mesma senha, gerando 2 chaves aleatórias em cada situação,
consequentemente gerando textos criptografados completamente distintos e completamente dependentes da senha do usuário.

#### Primeira vez submetido

Terminal:

    $ cswap file -t zenit
    password_1234

    file_Zenit Polar é um sistema simples de criptografia, que consiste na substituição das letras de uma palavra pela sua correspondente no nome ZENIT POLAR.

Json File:

        {
        "code": [
            {
                "title": "zenit",
                "user": 262979485013135803500474813246863587345959969717478505924687595301339316512807340426346468772743803575761683854513764250747205931588213829678260361427059235872336795191486371162345610139981254042634757911234636115311111123697923577239486397062511248097588332281434659439210517062380591935915758722266986851111111250553357911111508607191359146346358946744039158685124685111234374,
                "file": "Lt'yevflojbv\u00e9vw4vOyOet4jvOy4zotOvDtv3byzel.bjPyj>v0wtv3l'OyOetv'jvOwrOeyewy\u00e7\u00e3lvDjOvotebjOvDtvw4jvzjoj bjvztojvOwjv3lbbtOzl'Dt'etv'lv'l4tvLNE)8vfsZGhg"
            }
        ]
    }

#### Segunda vez submetido

Terminal:

    $ cswap file -t zenit2     
    password_1234

    file_Zenit Polar é um sistema simples de criptografia, que consiste na substituição das letras de uma palavra pela sua correspondente no nome ZENIT POLAR.

Json File:

        {
        "code": [
            {
                "title": "zenit",
                "user": 262979485013135803500474813246863587345959969717478505924687595301339316512807340426346468772743803575761683854513764250747205931588213829678260361427059235872336795191486371162345610139981254042634757911234636115311111123697923577239486397062511248097588332281434659439210517062380591935915758722266986851111111250553357911111508607191359146346358946744039158685124685111234374,
                "file": "Lt'yevflojbv\u00e9vw4vOyOet4jvOy4zotOvDtv3byzel.bjPyj>v0wtv3l'OyOetv'jvOwrOeyewy\u00e7\u00e3lvDjOvotebjOvDtvw4jvzjoj bjvztojvOwjv3lbbtOzl'Dt'etv'lv'l4tvLNE)8vfsZGhg"
            },
            {
                "title": "zenit2",
                "user": 2617574551097660685262906713739961705113629967953234647221311234537037477040056111025259822919274012932418299921704240193285824257299963452357821434771758072048220974523574634770279530158742854043747580591911111248245531111248109791123453591586974511234512480853595216057467279103746394471235761155618599137148524685234512369791113579111135914512594527463825482569941819680548374,
                "file": ",P-ch\\eKyd^\\\u00e9\\;1\\9c9hP1d\\9c1qyP9\\aP\\i^cqhKS^dLcdZ\\p;P\\iK-9c9hP\\-d\\9;J9hch;c\u00e7\u00e3K\\ad9\\yPh^d9\\aP\\;1d\\qdydD^d\\qPyd\\9;d\\iK^^P9qK-aP-hP\\-K\\-K1P\\,4XO#\\eIf2jw"
            }
        ]
    }
    
 
### Leia
 
Leia um arquivo na base de dados, precisa inserir o nome do arquivo e a senha correspondente no mesmo comando usado anteriormente. Se colocar a senha errada, o programa irá trazer o documento da forma que ele está na base de dados, porem se for a senha certa, ele ira te mostrar o arquivo como gostaria.

    $ cswap file
    or
    $ cswap file -t titulo_do_arquivo
 
#### Exemplo
 
Senha certa:
    
    $ cswap file -t zenit
    password_1234

    Zenit Polar é um sistema simples de criptografia, que consiste na substituição das letras de uma palavra pela sua correspondente no nome ZENIT POLAR.
 
Senha errada:
    
    $ cswap file -t zenit
    password_4321

    Lt'yevflojbv\u00e9vw4vOyOet4jvOy4zotOvDtv3byzel bjPyj>v0wtv3l'OyOetv'jvOwrOeyewy\u00e7\u00e3lvDjOvotebjOvDtvw4jvzjoj bjvztojvOwjv3lbbtOzl'Dt'etv'lv'l4tvLNE)8vfsZGhg
 
 
### Edite

Utilize o mesmo comando usado para adicionar e ler um documento, faça as alterações necessárias no editor e salve seu arquivo normalmente. O arquivo apenas sera sobrescrevido se a senha for correta.

### Delete

Apague um arquivo na base de dados da seguinte forma:

    $ cswap delete
    or 
    $ cswap delete -t titulo_do_arquivo

Você precisará inserir o título do arquivo que deseja excluir, bem como sua senha. se a senha estiver incorreta, o arquivo não será removido, caso contrário, será removido com sucesso.

### Liste

Liste os arquivos presentes localmente da seguinte forma:

    $ cswap list

### Backup

Com os seguintes comandos você pode exportar ou importar um arquivo Json com todas as informações necessárias para ler os arquivos de qualquer dispositivo, se você tiver a senha é claro ;)

    $ cswap backup -b save
    $ cswap backup -b load

Em ambos abrirá uma janela de arquivo, onde em 'save', você precisa selecionar onde deseja salvar o arquivo, e 'load', você deve selecionar o arquivo json que deseja importar, por padrão as janelas são abertas no caminho Desktop.

Se você importar um documento que já existe localmente, o programa ira ignorar este documento para evitar sobrescrever os dados. Se você quiser fazer essa substituição, primeiro exclua a versão local e depois importe o json normalmente.

## Como Funciona?
 
 
### Inspiração
 
A inspiração do projeto foi um antigo sistema de criptografia chamado Zenit Polar. O sistema funciona de uma forma, em que a primeira letra de uma das duas palavras zenit e polar, sempre é trocada pela primeira letra da outra, a segunda é trocada pela segunda e assim por diante. Como mostra o esquema a seguir:
 
| Z   | E   | N   | I   | T   |
| --- | --- | --- | --- | --- |
| P   | O   | L   | A   | R   |
 
 
Para um texto ser criptografado, cada letra deve ser trocada pela sua equivalente.
 
Então a palavra *'Banana'* ficaria *'Bilili'* em Zenit Polar.
 
### Key
 
Cada vez que um texto é submetido, uma key como esta é criada:
 
    39S617EM^uD@8sRKIntwZqcAQY*rTJljp&h45Wx%zi-B2C.VH#!fXNPabymGUF \e$v0o?O,kdgL
 
E usa o modelo do Zenit Polar para trocar as letras do texto submetido, como mostra o modelo a seguir:
 
| 3   | 9   | S   | 6   | 1   | 7   | E   | M   | ... |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| w   | Z   | q   | c   | A   | Q   | Y   | *   | ... |
 
 
Então a palavra *'Banana'* ficaria *' g5g5g'* com essa Key.
 
 
### Senha
 
 
 
Depois da criação de uma key, ela é transformada em Binário, e depois passa por um processo onde é feita uma contagem dos '0' e '1' para dar origem a outro número, como mostra o exemplo:
 
 
    key -> a
    
    key em Binário -> 01100001
    
    Contagem de 0 e 1 ->  10 21 40 11
    
    Separado em 0 e depois 1 ->  10 40 | 21 11
    
    Retirada de números desnecessários e é colocado um divisor ->  14021
 
 
Por último, esse novo número é multiplicado pela senha que o usuário inseriu, e então guardada no banco de dados junto do texto criptografado.
 
E por isso é impossível ler o arquivo sem a senha, porque sem a senha não é possível transformar o número em binário, sem o número em binário não é possível descobrir a key, e sem a key não é possível descriptografar o texto corretamente.
 
## Próximos Passos
  - feat: edit password
  - feat: interface command
  - fix: read, edit, delete, non existant file


 
 


