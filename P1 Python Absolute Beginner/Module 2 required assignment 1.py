
def ggs():
    sen = input("Welcome, Cj Hudson. Enter a 1 sentence quote, non-alpha separate words: ")
    word = ""

    for char in sen:
        if char.isalpha():            
            word += char
        else:                         
            if word != "":
                if word[0].lower() > "g":  
                    print(word.upper())
                word = ""               


    if word != "":
        if word[0].lower() > "g":
            print(word.upper())


ggs()
