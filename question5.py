listOne = [1,1,1,2,3,4,55,55,8]

listTwo = []

def remove_duplicate(list):
    for item in list:
        if item not in listTwo:
            listTwo.append(item)
    return listTwo

filtered_list = remove_duplicate(listOne)
print(listTwo)

        
