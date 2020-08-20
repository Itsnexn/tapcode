# create tapcode struct with a dict

polybe = {
    1:["A","B","C","D","E"],
    2:["F","G","H","I","J"],
    3:["L","M","N","O","P"],
    4:["Q","R","S","T","U"],
    5:["V","W","X","Y","Z"],
}

def prepare_sentence():
    """Prepare a sentence for the encryption"""
    accent = ["âà", "éèêë", "îï", "ô", "ûü", "ç"]
    ascii = ["A", "E", "I", "O", "U", "C"]
    for word in accent: # Replacing accented characters possible
        for letter in word:
            sentence = sentence.replace(letter, ascii[i])
        i += 1
    for letter in "',-;:!?.":  # Remove punctuation
        sentence = sentence.replace(letter, "")
    
    return sentence.upper()


def decypher(sentence):
    
    letter = [letter for letter in sentence]
    decypheredText = [""]*(len(sentence)//2+1)

    space = [index for index, element in enumerate(letter) if element == " "]
    print(space)
    for s in space :
        decypheredText[s//2-1] = " "
    print(decypheredText)

    letter = [i for i in letter if i != " "]

    for i in range(0,len(letter)-1,2):
        decypheredText.insert(i, polybe[int(letter[i])][int(letter[i+1])-1])
        print(decypheredText)

    return ''.join(decypheredText)

def cypher(sentence):
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
    
            

print(decypher("2315313134 12451515"))
print(cypher("HELLO BUEB BUEE"))
#print(cypher("je n aime pas les hareng"))