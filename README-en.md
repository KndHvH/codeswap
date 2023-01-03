# Readme Language

 - [Portuguese](/README.md)
 - [English](/README-en.md)

# CodeSwap

This is a personal project to be able to test my knowledge of the recent courses realized in test.
It consists of a program whose main function is to locally store texts and sensitive information in an easy and safe way.

![](codeswap-showcase.gif)

## Content
- [Readme Language](#readme-language)
- [CodeSwap](#codeswap)
  - [Content](#content)
  - [About](#about)
  - [Installation](#installation)
  - [Functionalities](#functionalities)
    - [Add](#add)
      - [Sample file](#sample-file)
      - [Context](#context)
      - [First time submitted](#first-time-submitted)
      - [Second time submitted](#second-time-submitted)
    - [Read](#read)
      - [Example](#example)
    - [Edit](#edit)
    - [Delete](#delete)
    - [List](#list)
    - [Backup](#backup)
  - [How it works?](#how-it-works)
    - [Inspiration](#inspiration)
    - [Key](#key)
    - [Password](#password)
  - [Next steps](#next-steps)

## About

The great advantage of CodeSwap is that the text stored locally is impossible to be read without the password created by the user, and that same password is not stored anywhere!


Another positive issue is that there is no "right" or "wrong" password, CodeSwap's logic allows the user to try to read a document even if the password is incorrect, but the text that this user will read will be the same saved in the database that has not yet been deciphered, since the password is just a cog in the functioning of the program as a whole!


## Installation

    Make sure you have Python installed and added to the PATH!

    $ pip install codeswap

## Functionalities
### Add

Add a file to the database, you will need to create a title and then a password.


    $ cs file
    or
    $ cs file -t file_title

#### Sample file

*"Zenit Polar is a simple encryption system, which consists of replacing the letters of a word by their corresponding name in the name ZENIT POLAR."*

#### Context

First enter a password of your choice. Then write the text in the editor that you want to store.
Each time a text is submitted, a key is randomly generated, then the text is encrypted based on the key, the key is then encrypted based on the password that the user has chosen and then the title, the key and the text are all stored in the database.

We can see in the following example that the same text is submitted 2 times with the same password, generating 2 random keys in each situation,
consequently generating completely different ciphertexts and completely dependent on the user's password.

####  First time submitted

Terminal:

    $ cs file -t zenit
    password_1234

    file_Zenit Polar is a simple encryption system, which consists of replacing the letters of a word by their corresponding name in the name ZENIT POLAR..

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

#### Second time submitted

Terminal:

    $ cs file -t zenit2     
    password_1234

    file_Zenit Polar is a simple encryption system, which consists of replacing the letters of a word by their corresponding name in the name ZENIT POLAR.

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
    
 
### Read
 
Read a file in the database, you need to enter the file name and the corresponding password in the same command used before. If you put the wrong password, the program will bring the document the way it is in the database, but if it's the right password, it will show you the file as you would like.

    $ cs file
    or
    $ cs file -t file_title
 
#### Example
 
Correct password:
    
    $ cs file -t zenit
    password_1234

    Zenit Polar is a simple encryption system, which consists of replacing the letters of a word by their corresponding name in the name ZENIT POLAR.
 
Wrong password:
    
    $ cs file -t zenit
    password_4321

    Lt'yevflojbv\u00e9vw4vOyOet4jvOy4zotOvDtv3byzel bjPyj>v0wtv3l'OyOetv'jvOwrOeyewy\u00e7\u00e3lvDjOvotebjOvDtvw4jvzjoj bjvztojvOwjv3lbbtOzl'Dt'etv'lv'l4tvLNE)8vfsZGhg
 
 
### Edit

Use the same command used to add and read a document, make the necessary changes in the editor and save your file as usual. The file will only be overwritten if the password is correct.

### Delete

Delete a file in the database as follows:

    $ cs delete
    or 
    $ cs delete -t file_title

You will need to enter the title of the file you want to delete, as well as your password. if the password is incorrect, the file will not be removed, otherwise it will be removed successfully.

### List

List the files present locally as follows:

    $ cs list

### Backup

With the following commands you can export or import a Json file with all the necessary information to read the files from any device, if you have the password of course ;)

    $ cs backup -b save
    $ cs backup -b load

In both, a file window will open, where in 'save', you need to select where you want to save the file, and 'load', you must select the json file you want to import, by default the windows are opened in the Desktop path.

If you import a document that already exists locally, the program will ignore this document to avoid overwriting the data. If you want to do this replacement, first delete the local version and then import the json as normal.

## How it works?
 
 
### Inspiration
 
The inspiration for the project was an old encryption system called Zenit Polar. The system works in a way, in which the first letter of one of the two words zenit or polar is always replaced by the first letter of the other, the second is replaced by the second and so on. As the following scheme shows:

 
| Z   | E   | N   | I   | T   |
| --- | --- | --- | --- | --- |
| P   | O   | L   | A   | R   |
 
 
For a text to be encrypted, each letter must be replaced by its equivalent.

 
So the word *'Banana'* would become *'Bilili'* in Zenit Polar.

 
### Key
 
Each time a text is submitted, a key like this is created:
 
    39S617EM^uD@8sRKIntwZqcAQY*rTJljp&h45Wx%zi-B2C.VH#!fXNPabymGUF \e$v0o?O,kdgL
 
And it uses the Zenit Polar template to change the letters of the submitted text, as shown in the following template:
 
| 3   | 9   | S   | 6   | 1   | 7   | E   | M   | ... |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| w   | Z   | q   | c   | A   | Q   | Y   | *   | ... |
 
 
So the word *'Banana'* would look like *' g5g5g'* with this Key.
 
 
### Password 
 
 
After creating a key, it is transformed into Binary, and then goes through a process where the '0' and '1' are counted to give rise to another number, as shown in the example:
 
    key -> a
    
    key in Binary -> 01100001
    
    Counting from 0 and 1 -> 10 21 40 11
    
    Separated into 0 and then 1 -> 10 40 | 21 11
    
    Removing unnecessary numbers and placing a divisor -> 14021
 
 
Finally, this new number is multiplied by the password that the user entered, and then stored in the database along with the encrypted text.
 
And that is why it is impossible to read the file without the password, because without the password it is not possible to transform the number into binary, without the number into binary it is not possible to discover the key, and without the key it is not possible to decrypt the text correctly.
 
## Next steps
  - feat: edit password
  - feat: interface command
  - fix: read, edit, delete, non existing file


 
 


