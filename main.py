#!/usr/bin/env python
import argparse
import tapcode


parser = argparse.ArgumentParser()
parser.add_argument("-s","--sentence",help="Sentence to cypher or decipher")
parser.add_argument("-f","--file",help="file to cypher or decipher")
parser.add_argument("-d", "--decode", action="store_true", help="decode tapcode sentence.")
parser.add_argument("-e", "--encode", action="store_true", help="encode sentences to tapcode.")
args = parser.parse_args()


if args.sentence:
    if args.decode :
        print(tapcode.decipher(args.sentence," ","."))

    elif args.encode:
        print(tapcode.encipher(args.sentence," ","."))
    else:
        print("The sentence cannot be processed !")

elif args.file :
    f = open(args.file)
    sentences = f.read()
    out = file = open('outfile', 'w+')
    if args.decode :
        dec = tapcode.decipher(sentences," ",".")
        out.write(dec)

    elif args.encode:
        enc = tapcode.encipher(sentences," ",".")
        out.write(enc)
    out.close()

else :
    print("Please provide a sentence to cypher or encipher !")
    exit()