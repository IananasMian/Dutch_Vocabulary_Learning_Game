import random

name = input("Hello!:) What is your name?")
answer = input("Do you wanna play the vocabulary game? ('y' to continue)")

if answer == "y":
    print(f"{name}, you are so diligent. Let's start the game!")
    
dutch_vocabulary_dict = {"de maat": "the size", "de riem": "the belt", "het overhemd": "the shirt", 
                         "de pet": "the cap", "het vest": "the cardigan", "de sjaal": "the scarf", 
                         "de laars": "the boot", "de rok": "the skirt", "de maillot": "the tights",
                         "dragen": "to wear", "de spijkerbroek": "the jeans", "de kleren": "the clothes",
                         "uitzoeken": "to choose", "passen": "to try on", "moeilijk": "difficult",
                         "het ding": "the thing", "de hoek": "the corner", "kennen": "to know",
                         "het advies": "the advice", "eerlijk": "honest", "staan": "to suit",
                         "de verkoper": "the salesman", "depaskamer": "the fitting room", "proberen": "to try",
                         "zelf": "yourself", "het model": "the model", "roze": "pink", "zitten": "to fit",
                         "strak": "tight", "de V-hals": "the V-neck", "geel": "yellow", "waterdicht": "waterproof",
                         "de mouw": "the sleeve", "de bloes\de blouse": "the blouse", "de sok": "the sock", "grijs": "gray"      
}

keyword_list = list(dutch_vocabulary_dict.keys())
random.shuffle(keyword_list)
print("In total there are 36 vocabularies. If you wanna finish the game immediatly during the process, please type 'leave'.")
correct = 0
incorrect = 0

for keyword in keyword_list:
    display = "{}"
    print(display.format(keyword))
    your_answer = input("Your answer: ")
    print(dutch_vocabulary_dict[keyword])

    if your_answer == dutch_vocabulary_dict[keyword]:
        print("Your answer is correct")
        correct += 1
    elif your_answer == "leave":
        print(f"Dear {name}, Thanks for playing my dutch vocabulary game. See you!")
        break;
    else:
        print("Your answer is incorrect.")
        incorrect+=1
    
print(f"Your score: {correct} correct & {incorrect} incorrect.")