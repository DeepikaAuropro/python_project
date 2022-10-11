my_list = [1,2,4,5,6,8,10,13,22,35,52,83]
for i in my_list:
    if(i >=10):
        print(i)

output:
10
13
22
35
52
83

#-------------------------------------------

my_list = [1,2,4,5,6,8,10,13,22,35,52,83]
new_list = []
for i in my_list:
    if(i >= 10):
        new_list.append(i)
print(new_list)

output:[10, 13, 22, 35, 52, 83]

#.............................................

a = int(input("enter a number"))
my_list = [1,2,4,5,6,8,10,13,22,35,52,83]
for i in my_list:
    if(i >= a):
        print(i)

output:
enter a number13
13
22
35
52
83

#---------------------------------------------------------------------------------

employee = {"name":"tim","age":30,"b_day":"1990-03-10","job":"devops engineer"}
employee.pop('age')
employee["job"] = "Software Engineer"
for key, value in employee.items():
    print(key, ' : ', value)

output:
name  :  tim
b_day  :  1990-03-10
job  :  Software Engineer
    
#------------------------------------------------------------

employees = [{
  "name": "Tina",
  "age": 30,
  "birthday": "1990-03-10",
  "job": "DevOps Engineer",
  "address": {
    "city": "New York",
    "country": "USA"
  }
},
{
  "name": "Tim",
  "age": 35,
  "birthday": "1985-02-21",
  "job": "Developer",
  "address": {
    "city": "Sydney",
    "country": "Australia"
  }
}]
for employee in employees:
    print("name:" , employee['name'])
    print("job:" , employee['job'])
    print("city:" , employee['address']['city'])
    print("\n")

print(employees[1]["address"]['country'])

output:
name: Tina
job: DevOps Engineer
city: New York


name: Tim
job: Developer
city: Sydney


Australia

#-------------------------------------------------------------------




