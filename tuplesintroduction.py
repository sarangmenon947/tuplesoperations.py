introduction = ("Sarang", "13", "Kerala", "Cyboard", "Python", "Hindi")
print(introduction)

introduction2 = "Sarang", "13", "Kerala", "Cyboard", "Python", "Hindi"
print(introduction2)

name, age, state, schoolname, programminglanguage, secondlanguage = introduction
print(name, age, state, schoolname, programminglanguage, secondlanguage)

print(introduction[0:4])

#introduction[1] = 15 #Tuples cannot be changed or edited

print(introduction[4:6])

print(introduction[-1])

for i in range(0, 6):
    print(introduction[i])
