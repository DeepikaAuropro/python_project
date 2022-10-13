import random
target_num = random.randrange(10) #assigning range to the target_num
guess_num = 0
count = 0
while target_num!=guess_num:
    count = count+1 #to count the repetition of the loop
    try:
        guess_num=int(input("enter guess number"))
        if(target_num < guess_num):
            print("The number is greater than the target number")
        elif(target_num > guess_num):
             print("The number is lesser than the target number")
        elif(target_num == guess_num):
            print("YOU WON THE GAME")
    except:
        print("alphabets are not allowed, try only numbers from 1-10")

print(f'You won the game after {count} chances')

#------------------------------------------------------------------------------------------
#Program to count the number of upper case and lower case letters in a string

def strcount():
    word = str(input("enter string"))
    upper_case = [] #declaring an empty array
    lower_case = []
    for i in word: #i means a letter in a word
        if(i >= 'a') and (i <= 'z'):
            lower_case.append(i) #adding the letter to the array

        if(i >= 'A') and (i <= 'Z'):
            upper_case.append(i)
    print(f"The upper case letters are:{len(upper_case)}")#printing the length of the array to get the number of letters
    print(f"The lower case letters are:{len(lower_case)}")
strcount()

#--------------------------------------------------------------------------------------------------------
#Program to print even numbers from a list

input_elements = input("Enter numbers separated by space ")
Num_list  = input_elements.split( )
print(Num_list)
for num in Num_list:
    value = int(num)
    if(value%2 == 0):
        print(f'The even numbers in a list are: {value}')

