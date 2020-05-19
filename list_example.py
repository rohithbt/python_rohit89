list=[1,2,3]
list.append("machine learning")
print(list)


list.extend(['g','h'])
print(list)

list.insert(1,'scripting')
print(list)

list.remove(3)
print(list)

list1=sorted(['python','java','dotnet','golang'])
for course in list1[::-1]:
        print(course)
