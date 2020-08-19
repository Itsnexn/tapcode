# create tapcode struct with a dict

polybe = {
    1:["A","B","C","D","E"],
    2:["F","G","H","I","J"],
    3:["L","M","N","O","P"],
    4:["Q","R","S","T","U"],
    5:["V","W","X","Y","Z"],
}

def decypher(sentence):
    
    letter = [letter for letter in sentence]
    decypheredText = []


    for i in range(0,len(letter)-1,2):
        decypheredText.append(polybe[int(letter[i])][int(letter[i+1])-1])

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
    
            

print(decypher("1234244215"))
#print(cypher("je n aime pas les hareng"))