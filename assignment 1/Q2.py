def revword(new):
    new = new.lower().strip()[::-1]
    return(new)

def countword():
    fh = open("text.txt" , "r")
    Counter = 1
    for line in fh:
        new_word = ''
        lineWords = line.split(" ")
        if len(lineWords) == 1:
            W1 = lineWords[0].lower().strip()
            print(W1 ,end ='')
        else:
            for j in lineWords:
                Word = revword(j)
                new_word += (Word + ' ')
                if Word == W1:
                    Counter += 1
        print(new_word)
    print(Counter)
countword()

