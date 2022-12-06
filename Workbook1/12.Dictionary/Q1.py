'''Q1.Create a list of students name. Create another list with corresponding marks for the students. 
Now, create a dictionary with the students name as keys and marks as values.
'''
Stud_lst = ['Bhakti', 'Prerna', 'Aishwarya']
stud_data = dict.fromkeys(Stud_lst)
stud_data['Bhakti'] = 90
stud_data['Prerna'] = 80
stud_data['Aishwarya'] = 70
print(stud_data)