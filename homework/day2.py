python_para = """Python is a powerful, easy-to-learn programming language used for web development,
data analysis, artificial intelligence, and automation. This course helps beginners understand 
Python basics, syntax, and concepts through hands-on coding exercises and real-world examples."""
print(len(python_para))
print('first character:',python_para[0])
print('last character:',python_para[-1])
print('first 50 characters:',python_para[:50])
print('replace:',python_para.replace('Python','PYTHON'))
print('paragraph in lowercase:',python_para.lower())
print("after strip:", python_para.strip())
words = python_para.split()
print('after split',python_para.split())
a = 'course' in python_para
print(a)
print('the course description is {} characters long and has {} words.'.format(len(python_para),len(words)))
