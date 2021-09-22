#!/usr/bin/env python3

# polybe square
polybe = [
    ["a", "b", "c", "d", "e"],
    ["f", "g", "h", "i", "j"],
    ["l", "m", "n", "o", "p"],
    ["q", "r", "s", "t", "u"],
    ["v", "w", "x", "y", "z"]
]


def prepare_sentence(sentence: str):
    """
    Prepare a sentence for the encryption

    Args:

        Sentence (String):          Sentences to encode.

    Return:

        String. Cleaned sentences.

    Example:

        >>> prepare_sentence("Hêllô?!:_)")
        "hello"

    """

    accent = ["âà", "éèêë", "îï", "ô", "ûü", "çk"]
    ascii = ["a", "e", "i", "o", "u", "c"]
    specialChars = "~!@#$%^&*()-_+={}][|\`,./?;:'\"<>"

    for item, itemIndex in zip(accent, range(len(accent))):    # Replacing accented characters possible
        for letter in item:
            if letter in sentence:
                sentence = sentence.replace(letter, ascii[itemIndex])

    for letter in specialChars:                                 # Remove special characters
        sentence = sentence.replace(letter, "")
    sentence = sentence.lower()

    return sentence


def decipher(code: str):
    """
    Decipher tapcode sentences.

    Args:

        Code (String):              Tapcode sentence to decipher.

    Return:

        String. Deciphered tapcode sentences.

    Example:

        >>> decipher("23 15 31 31 34")
        "hello"
    """

    inp = "".join(filter(str.isdigit , code)) # keep numbers and remove other chars
    deciphered = []

    for i in range(0, len(inp), 2):
        splitting = (inp[i], inp[i + 1])
        char = polybe[int(splitting[0]) - 1][int(splitting[1]) - 1]
        deciphered.append(char)


    return "".join(deciphered)


def encipher(sentence: str, sep: str = " ") -> str:
    """
    Encipher a sentence with tapcode system

    Args:

        Sentence (String):          sentence
        Sep (String):               Separator(space by default)

    Return:

        String. Enciphered sentences.

    Example:

        >>> encipher("Hello")
        "23 15 31 31 34"
        >>> encipher("", "_")
        "23_15_31_31_34"
    """

    sentence = prepare_sentence(sentence)
    encipheredText = []

    for word in sentence.strip().split(" "):
        for letter in word:
            for i in range(len(polybe)):
                for j in range(len(polybe[i])):
                    if polybe[i][j] == letter:
                        encipheredText.append(str(i+1) + str(j+1))
                        encipheredText.append(sep)

    # This pice of code will add sep to the end of our encipheredText
    # so for remove that we can use output[:-len(sep)]
    # but what if that sep was empty string?
    # 23 = h become 2 then we cant decode the sentence

    # Thats why i wrote this if statement
    if sep:
        return "".join(encipheredText)[:-(len(sep))]
    else:
        return "".join(encipheredText)




def tapcodeConvert(sentence: str, tap: str= " ", sep: str=".", outputSep: str = " ") -> str:
    """
    Convert TapCode to decimal values

    Args:

        Sentence (String):         Tapcode to convert
        Tap (String):               Tap string ("." by default)
        Sep (String):               Separator (" " by default)
        OutputSep (String):         Output separator (" " by default)

    Return:

        String. Enciphered sentences.

    Example:

        >>> tapcodeConvert(".. ... . ..... ... . ... . ... ....")
        "23 15 31 31 34"
        >>> tapcodeConvert("--_---_-_-----_---_-_---_-_---_----", "-", "_")
        "23 15 31 31 34"
        >>> tapcodeConvert(".. ... . ..... ... . ... . ... ....", outputSep="_")
        "23_15_31_31_34"
    """

    converted = []
    cleaned = ""

    # Clean the sentence to just taps and separators
    for i in sentence:
        if i == tap:
            cleaned += i
        if i == sep:
            cleaned += sep

    splited = cleaned.split(sep) # split the cleaned sentence to list of taps

    for i in range(1, len(splited), 2):
        converted.append(str(len(splited[i - 1])))
        converted.append(str(len(splited[i])))
        converted.append(outputSep)

    # Just like encipher function
    if outputSep:
        return "".join(converted)[:-(len(sep))]
    else:
        return "".join(converted)

def genTapcode(sentence: str, tap:str = ".", sep: str = " ", dec:bool = False) -> str:
    """
    Generate TapCode from string\Decimal Values

    Args:

        sentence (String):         Sentence
        tap (String):               Tap string ("." by default)
        sep (String):               Separator (" " by default)
        dec (Boolean):              Input type (True for decimal input False for String input!)

    Return:

        String. Generated tap code.

    Example:

        >>> genTapcode("Hello")
        ".. ... . ..... ... . ... . ... ...."
        >>> genTapcode("Hello", "-", "_")
        "--_---_-_-----_---_-_---_-_---_----"
        >>> genTapcode("23 15 31 31 34", dec=True)
        ".. ... . ..... ... . ... . ... ...."

    """
    if dec:
        inp = sentence
    if not dec:
        inp = encipher(sentence, sep)

    DecimalTaps = "".join(filter(str.isdigit , inp)) # keep numbers and remove other chars

    output = []
    for i in DecimalTaps:
        output.append(int(i) * tap)
        output.append(sep)

    # Just like encipher function
    if sep:
        return "".join(output)[:-(len(sep))]
    else:
        return "".join(output)