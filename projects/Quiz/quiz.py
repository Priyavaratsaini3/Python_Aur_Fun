import random
## Inputs 
# questions 5 
# randomly choice 
# 4 option 

title = "Welcome to Quiz Game"
print(title)
print("-" * 45)
print("Guess the right Answer of the Questions")
print("-" * 45)
def mcq1 ():
    mcq = {1: "How many state in India ?", 2: "What is the name of longest river in india ?", 3: "What is the capital of United Kingdom ?"}
    return mcq
mcq1()

for i in mcq1():
    if i == 1:
        print(f"{mcq1()[i]} \n Options: \n a: 21 \n b: 24 \n c: 27 \n d: 28")
        option_is_correct = input("Select the Option: ")
        if option_is_correct == "d":
            print("Your Answer is correct :", option_is_correct)
        else: 
            print("Your Answer is worng: ", option_is_correct)
    elif i == 2:
        print(f"{mcq1()[i]} \n Options: \n a: Ganga \n b: Yamuna \n c: Godavari \n d: Brahmaputra")
        option_is_correct = input("Select the Option: ")
        if option_is_correct == "a":
            print("Your Answer is correct :", option_is_correct)
        else: 
            print("Your Answer is worng: ", option_is_correct)
    elif i == 3:
        print(f"{mcq1()[i]} \n Options: \n a: London \n b: Manchester \n c: Birmingham \n d: Liverpool")
        option_is_correct = input("Select the Option: ")
        if option_is_correct == "a":
            print("Your Answer is correct :", option_is_correct)
        else: 
            print("Your Answer is wrong: ", option_is_correct)
