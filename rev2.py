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


output:
    enter guess number3
    The number is lesser than the target number
    enter guess number7
    YOU WON THE GAME
    You won the game after 2 chances


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


output:
    enter stringDevOps
    The upper case letters are:2
    The lower case letters are:4




#--------------------------------------------------------------------------------------------------------
#Program to print even numbers from a list

input_elements = input("Enter numbers separated by space ")
Num_list  = input_elements.split( )
even_list = []
print(Num_list)
for num in Num_list:
    value = int(num)
    if(value%2 == 0):
        even_list.append(value)

print(f'The even numbers in a list are:  {even_list}')
    
    
output:
    Enter numbers separated by space 1 3 4 6 8 9 11 14 15 18 22 33
    ['1', '3', '4', '6', '8', '9', '11', '14', '15', '18', '22', '33']
    The even numbers in a list are:  [4, 6, 8, 14, 18, 22]

    
