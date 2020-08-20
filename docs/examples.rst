CLI Examples 
=============

Help
-----

```
$ tapcode --help 

usage: tapcode [-h] [-s SENTENCE] [-f FILE] [-d] [-e]

optional arguments:
  -h, --help            show this help message and exit
  -s SENTENCE, --sentence SENTENCE
                        Sentence to cypher or decipher
  -f FILE, --file FILE  file to cypher or decipher
  -d, --decode          decode tapcode sentence.
  -e, --encode          encode sentences to tapcode.
```


Encipher a clear message 
-------------------------
```sh
$ tapcode -es "I Love Tapcode"
24 31345115 44113513341415.
```


Decipher a tapcode message 
----------------------------
```sh
$tapcode -ds "24 31345115 44113513341415"
I LOVE TAPCODE .
```

File input
-----------
You can do the same but from file :

```sh
# Encipher
$ echo "I love coffee !" > to_encode.txt
$ tapcode -ef to_encode.txt
$ cat encoded
24 31345115 133421211515 .

# Decipher
$ echo "24 31345115 3511434411" > to_decode.txt
$ tapcode -df to_decode.txt
$ cat decoded
I LOVE PASTA .
```