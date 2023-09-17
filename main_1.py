my_list_1 = [1,2,2,3,5,4,5]
print ("Оріг : " + str(my_list_1))

li = []
duplicates = []
for i in my_list_1:
  if i not in li:
    li.append(i)
  else:
    duplicates.append(i)




print ("Після : " + str(li))

print("Викидиши: " + str(duplicates))