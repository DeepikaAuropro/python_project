my_list = [1,2,4,5,6,8,10,13,22,35,52,83]
for i in my_list:
    if(i >=10):
        print(i)

#-------------------------------------------

my_list = [1,2,4,5,6,8,10,13,22,35,52,83]
new_list = []
for i in my_list:
    if(i >= 10):
        new_list.append(i)
print(new_list)

#.............................................

a = int(input("enter a number"))
my_list = [1,2,4,5,6,8,10,13,22,35,52,83]
for i in my_list:
    if(i >= a):
        print(i)

#---------------------------------------------------------------------------------

employee = {"name":"tim","age":30,"b_day":"1990-03-10","job":"devops engineer"}
employee.pop('age')
employee["job"] = "Software Engineer"
for key, value in employee.items():
    print(key, ' : ', value)




