#3) Manipulating lists 
        # You may be familiar with adding individual data elements to a list by using the .append() method. However, if you want to combine a list with another array type(list, set, tuple), you can use the .extend() method on the list.

        # You can also use the .index() method to find the position of an item in a list. You can then use that position to remove the item with the .pop() method.

        # In this exercise, you'll practice using all these methods!


        # Ask 4 students at Datanomics to enter their names one at a time
        
        # Add their names to the list

student_names = ['Muluken', 'Bethelhem', 'Samuel', 'Workneh']

        # Extend the list student_names using the .extend() list method with two additional new students 

student_names.extend(['Meklit', 'Hana'])

        # Print student_names

print("Updated list of students:", student_names)

        # Find the position of one of the students and store the result in a variable called 'position'
       
position = student_names.index('Samuel')
position=2

        # Remove that student  from the list student_names using the .pop() list method
student_names.pop(position)  

        # Print student_names one more time

print("Final list of students:", student_names)




