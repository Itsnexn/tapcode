#!/usr/bin/env python
import argparse
import tapcode


parser = argparse.ArgumentParser()
parser.add_argument("sentence",help="Sentence to cypher or decipher")
parser.add_argument("-d", "--decode", action="count", help="decode tapcode sentence.")
parser.add_argument("-e", "--encode", action="count", help="encode sentences to tapcode.")
args = parser.parse_args()

if args.decode :
    print(tapcode.decipher(args.sentence," ","."))

elif args.encode:
    print(tapcode.encipher(args.sentence," ","."))
else:
    print("The sentence cannot be processed !")