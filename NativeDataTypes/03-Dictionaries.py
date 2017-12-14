Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = [1,2,3,4]
>>> type(a)
<class 'list'>
>>> a = (1,2,3,4)
>>> type(a)
<class 'tuple'>
>>> users = {'id' : 101, 'Name' : 'Ram', 'Age' : 20}
>>> users
{'id': 101, 'Name': 'Ram', 'Age': 20}
>>> users[0]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    users[0]
KeyError: 0
>>> users['id']
101
>>> users['name']
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    users['name']
KeyError: 'name'
>>> users['Name']
'Ram'
>>> users['Age'] = 21
>>> users
{'id': 101, 'Name': 'Ram', 'Age': 21}
>>> users['Course'] = 'MCA'
>>> users
{'id': 101, 'Name': 'Ram', 'Age': 21, 'Course': 'MCA'}
>>> users.keys()
dict_keys(['id', 'Name', 'Age', 'Course'])
>>> users.values()
dict_values([101, 'Ram', 21, 'MCA'])
>>> users.items()
dict_items([('id', 101), ('Name', 'Ram'), ('Age', 21), ('Course', 'MCA')])
>>> for data in users:
	print(data)

	
id
Name
Age
Course
>>> for data in users.values():
	print(data)

	
101
Ram
21
MCA
>>> for data in users.items():
	print(data)

	
('id', 101)
('Name', 'Ram')
('Age', 21)
('Course', 'MCA')
>>> users.pop()
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    users.pop()
TypeError: pop expected at least 1 arguments, got 0
>>> users.pop('id')
101
>>> users
{'Name': 'Ram', 'Age': 21, 'Course': 'MCA'}
>>> users = {'id' : [101,102,103,104,105], "Name" : ['Ram', 'Shyam', 'Ravi', 'Amit', 'Ajay']}
>>> users
{'id': [101, 102, 103, 104, 105], 'Name': ['Ram', 'Shyam', 'Ravi', 'Amit', 'Ajay']}
>>> users['id']
[101, 102, 103, 104, 105]
>>> users['Name']
['Ram', 'Shyam', 'Ravi', 'Amit', 'Ajay']
>>> users['Name'][4]
'Ajay'
>>> users['Name'][4] = "Akshay"
>>> users
{'id': [101, 102, 103, 104, 105], 'Name': ['Ram', 'Shyam', 'Ravi', 'Amit', 'Akshay']}
>>> user_id = users['id']
>>> user_id.append(106)
>>> users
{'id': [101, 102, 103, 104, 105, 106], 'Name': ['Ram', 'Shyam', 'Ravi', 'Amit', 'Akshay']}
>>> user_name = users['Name']
>>> user_name
['Ram', 'Shyam', 'Ravi', 'Amit', 'Akshay']
>>> user_name.append('Ajay')
>>> users
{'id': [101, 102, 103, 104, 105, 106], 'Name': ['Ram', 'Shyam', 'Ravi', 'Amit', 'Akshay', 'Ajay']}
>>> 
