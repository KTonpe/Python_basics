'''
1.you can't directly add a number in a empty list
2. if you want to append without using it -> you add the lists : list_name = list_name + [x]
3. please check the index as it starts from 0 -> so length must be x+1
'''
import unittest
def assending(list_of_numbers):
    list_of_numbers.sort()
    return  list_of_numbers

class Testordering(unittest.TestCase):
    def test_assending(self):
        self.assertEqual(assending(assending([5, 3, 4, 1, 2])), [1, 2, 3, 4, 5])
    def test_with_similar_numnbers(self):
        self.assertEqual(assending(assending([5, 3, 3, 1, 2])), [1, 2, 3, 3, 5])
    
list_of_numbers = []
limit = int(input("Enter the limit: "))
for i in range(1,limit+1):
    list_of_numbers.append(int(input(f'Emter {i}.number : ')))

Order_list = assending(list_of_numbers)
print(Order_list)
unittest.main()




'''limit = int(input("Enter the limit: "))
#print(limit)
list_of_numbers = []
for i in range(0,limit):
    #list_of_numbers.append(int(input("Enter the number: ")))
    num = int(input(f"Your {i}.number is : "))
    list_of_numbers += [num]

list_of_numbers.sort() #arranged in asscending order
print(list_of_numbers)
list_of_numbers.sort(reverse=True) #arranged in descending order
print(list_of_numbers)'''

'''
#to print only the given number in a list
location = int(input('Enter the location: '))
number = int(input('Enter the number: '))
list_of_num =[0]*(location+1) #adding 0s in the list of length location+1
list_of_num[location] = number 

print(list_of_num,len(list_of_num))'''