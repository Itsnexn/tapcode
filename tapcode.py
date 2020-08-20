from pprint import pprint
# create tapcode struct with a dict

polybe = {
    1:["A","B","C","D","E"],
    2:["F","G","H","I","J"],
    3:["L","M","N","O","P"],
    4:["Q","R","S","T","U"],
    5:["V","W","X","Y","Z"],
}


matrix = [
    ["A","B","C","D","E"],
    ["F","G","H","I","J"],
    ["L","M","N","O","P"],
    ["Q","R","S","T","U"],
    ["V","W","X","Y","Z"]
]

def prepare_encyphered(code,sep=" "):
    """
    Split word according to a separator
    """
    return code.split(sep)

def decypher_matrix(code):
    decyphered = []
    
    code = prepare_encyphered(code) # list of word
    for word in code :
        splitting = [(word[l],word[l+1]) for l in range(0,len(word),2)]  

        for tuple in splitting :
            decyphered.append(matrix[int(tuple[0])-1][int(tuple[1])-1]) # minus one because index start at 0 but number in code start at 1
        decyphered.append(" ")

    return "".join(decyphered)


    return decyphered

#print(decypher_matrix("2315313134 2315313134"))

def encypher_matrix(sentence):
    sentence = prepare_sentence(sentence)
    

def prepare_sentence(sentence):
    """Prepare a sentence for the encryption"""
    accent = ["âà", "éèêë", "îï", "ô", "ûü", "ç"]
    ascii = ["A", "E", "I", "O", "U", "C"]
    i=0
    for word in accent: # Replacing accented characters possible
        for letter in word:
            sentence = sentence.replace(letter, ascii[i])
        i += 1
    for letter in "',-;:!?":  # Remove punctuation
        sentence = sentence.replace(letter, "")
    sentence = sentence.upper()

    return sentence.split(".")


print(prepare_sentence("Salut tête de con. Tu as l'air bien aise"))

def cypher(sentence):
    sentence=prepare_sentence(sentence)
    cypheredText = []
    letter = [letter for letter in sentence]

    for l in letter :
        if l == ' ':
            cypheredText.append(' ')
            continue

        for key in polybe.keys():
            if l.upper() in polybe[key]:
                cypheredClean = str(key)+str(int(polybe[key].index(l.upper())+1))
                cypheredText.append(cypheredClean)

    return ''.join(cypheredText)


print(encypher_matrix("Salut tête de con. Tu as l'air bien aise"))
