# [ ] create, call and test the str_analysis() function  
def str_analysis(insert):
    while True: 
        insert = input("[CJ HUDSON], enter word or integer:")
        if insert.isdigit():
            if int(insert) > 99:
                print(str(insert) + " is a pretty big number!")
            elif int(insert) < 99:
                print( str(insert) + " is a smaller number than expected!")
            else:
                print(str(insert) + " is equal to 99!")
        elif insert.isalpha():
            print("\"" + insert + "\" is all alphabetical characters!")
        elif insert == "":
            break
        else:
            print( "invalid input, input contains multiple character types")

print(str_analysis(insert))

