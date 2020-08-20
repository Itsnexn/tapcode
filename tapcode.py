# create tapcode struct with a dict

polybe = {
    1:["A","B","C","D","E"],
    2:["F","G","H","I","J"],
    3:["L","M","N","O","P"],
    4:["Q","R","S","T","U"],
    5:["V","W","X","Y","Z"],
}

def prepare_sentence(sentence):
    """Prepare a sentence for the encryption"""
    accent = ["âà", "éèêë", "îï", "ô", "ûü", "ç"]
    ascii = ["A", "E", "I", "O", "U", "C"]
    i=0
    for word in accent: # Replacing accented characters possible
        for letter in word:
            sentence = sentence.replace(letter, ascii[i])
        i += 1
    for letter in "',-;:!?.":  # Remove punctuation
        sentence = sentence.replace(letter, "")
    print(sentence.upper())
    return sentence.upper()

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
    
            

print(cypher("BONJOUR COMMENT ALLEZ VOUS ETES VOUS BIEN REPOSE"))
#print(cypher("je n aime pas les hareng"))