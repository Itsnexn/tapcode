Commend line interface (CLI)
============================

- `Help`_
- `Input Methods and output`_
- `Encode`_
- `Decode`_
- `Generate`_
- `Convert`_


----
Help
----

**Help Menu**
    -i INPUT, --input INPUT       Sentence to cypher or decipher
    -f FILE, --file FILE          File to cypher or decipher
    -o OUTPUT, --output OUTPUT    Output file.
    -I, --stdin                   Standard input
    -d, --decode                  Decode tapcode sentence.
    -e, --encode                  Encode sentences to tapcode (Should be decimal values).
    -C, --convert                 Convert tapcode to Decimal value.
    -G, --generate                Generate tapcode!


For flags that does not need an Argument you can combine them together!

Example:
  ``tapcode -df myfile.txt``

in this example we used ``-d`` which is decipher but doesnt need any argument so we can combine it with ``-f`` which is our file input


------------------------
Input Methods and output
------------------------

Input
#####

**Tapcode-cli** has three option to get input from user:

- Input string
- File input
- Stdin (Standard-Input/Pipe)

**Input As a String:**
  ``tapcode -i "This is my Input"``

**Input As a File**
  ``tapcode -f myfile.txt``

**input from Stdin/Pipe**
  ``echo "I love tapcode" | tapcode -s``
OR:
  ``tapcode -s < echo "I love tapcode"``

**You can't use input methods together this is also apply to other arguments!**

**NOTE:** all of the input methods doing the same thing but here we are going to use the input flag to make documents easier.

Output
######

For output we have option ``-o`` or ``--output`` which both you can use them to specify an output file.

Example:
  ``tapcode -ei "I love tapcode" -o out.txt``
OR:
  ``tapcode -i "I love tapcode" -e -o out.txt``

And this is how we write into file:

.. code-block:: python

  with open("FILE", "w") as f:
    f.write(stdout)

**so be careful because you can damage your files with this argument!**

--------
Encode
--------

**Flag Help Menu:**
  -e, --encode                  Encode sentences to tapcode (Should be decimal values).

Encode flag doesn't need an argument and it returns a string of enciphered text.

Example:
  ``tapcode -i "I love Tapcode" -e``
OR:
  ``tapcode -ei "I love Tapcode"``

And it's going to return:
  ``24 31 34 51 15 44 11 35 13 34 14 15``


------
Decode
------

**Flag Help Menu:**
  -d, --decode                  Decode tapcode sentence.

Decode flag doesn't need an argument and it returns a string of deciphered text.

Example:
  ``tapcode -i "24 31 34 51 15 44 11 35 13 34 14 15" -d``
OR:
  ``tapcode -di "24 31 34 51 15 44 11 35 13 34 14 15"``

And it's going to return:
  ``ilovetapcode``

you may think why there is no **space**?
Well, according to `TapCode Wikipedia page <https://en.wikipedia.org/wiki/Tap_code>`_
tapcode is and letter-by-letter message, and
`Polybius square (Wikipedia link) <https://en.wikipedia.org/wiki/Polybius_square>`_
is a 5x5 grid which doesn't have space!

--------
Generate
--------

**Flag Help Menu:**
  -G, --generate                Generate tapcode!

Generate flag doesn't need an argument and it generates tapcode from the **String** input.

Example:
  ``tapcode -i "tapcode" -G``
OR:
  ``tapcode -Gi "tapcode"``

And it's going to return:
  ``.... .... . . ... ..... . ... ... .... . .... . .....``

-------
Convert
-------

**Flag Help Menu:**
  -C, --convert                 Convert tapcode to Decimal value.