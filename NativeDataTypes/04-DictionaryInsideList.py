Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> users = []
>>> user_1 = {'id' : 101, 'Name' : 'Ram'}
>>> users.append(user_1)
>>> users
[{'id': 101, 'Name': 'Ram'}]
>>> user_2 = {'id' : 102, 'Name' : 'Shyam'}
>>> users.append(user_2)
>>> user_3 = {'id' : 103, 'Name' : 'John'}
>>> users.append(user_3)
>>> users
[{'id': 101, 'Name': 'Ram'}, {'id': 102, 'Name': 'Shyam'}, {'id': 103, 'Name': 'John'}]
>>> for data in users:
	print(data)

	
{'id': 101, 'Name': 'Ram'}
{'id': 102, 'Name': 'Shyam'}
{'id': 103, 'Name': 'John'}
>>> users[0]
{'id': 101, 'Name': 'Ram'}
>>> 
