# TAPCODE

[![PyPI version](https://badge.fury.io/py/tapcode.svg)](https://badge.fury.io/py/tapcode) [![Requirements Status](https://requires.io/github/remiflavien1/tapcode/requirements.svg?branch=master)](https://requires.io/github/remiflavien1/tapcode/requirements/?branch=master) [![Documentation Status](https://readthedocs.org/projects/tapcode/badge/?version=latest)](https://tapcode.readthedocs.io/en/latest/?badge=latest)

Tapcode Cypher also known as Prisoner's tapcode.
For a complete documentation look at [ReadTheDocs](https://tapcode.readthedocs.io/en/latest/)

## Install

You can install ```tapcode``` either via pip (PyPI) or from source.
To install using pip:
```bash
pip3 install tapcode
```
Or manually:
```
git clone https://github.com/remiflavien1/tapcode
cd tapcode
python3 setup.py install
```

## CLI
### Help Menu:

```
$ tapcode --help

usage: tapcode [-h] [-i INPUT] [-f [FILE]] [-o [OUTPUT]] [-I] [-d] [-e] [-C] [-G] [-v]

Encipher or Decipher a tapcode message.

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Sentence to cypher or decipher
  -f [FILE], --file [FILE]
                        File to cypher or decipher
  -o [OUTPUT], --output [OUTPUT]
                        Output file.
  -I, --stdin           Standard input
  -d, --decode          Decode tapcode sentence.
  -e, --encode          Encode sentences to tapcode (Should be decimal values).
  -C, --convert         Convert tapcode to Decimal value. '.... ...' => '43'
  -G, --generate        Generate tapcode!
  -v, --version         outputHandeler version
```

### Features:
- **Multiple input method:**
  - Input text
  - File input
  - Standard input(Pipe)
- **Bulit in output flag**
- **Generate and convert any tapcode**

### Examples:

Encipher a clear message:
```sh
$ tapcode -es "I Love Tapcode"
24 31 34 51 15 44 11 35 13 34 14 15
```

Decipher a tapcode message:
```sh
$tapcode -ds "24 31 34 51 15 44 11 35 13 34 14 15"
ilovetapcode
```

**For More Examples check [ReadTheDocs](https://tapcode.readthedocs.io/en/latest/)**


## API

**For a complete API documentation look at [ReadTheDocs](https://tapcode.readthedocs.io/en/latest/)**

> Tapcode-cli 2.0.0 (Windows | GNU/Linux) libTapcode 2.0.0</br>
> Release Date: Aug 20, 2020</br>
> credits: shadawck, Itsnexn</br>
> Copyright 2020, The TapCode Project