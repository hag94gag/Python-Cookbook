num_one=10
num_two=20
result=num_one+num_two
print(result)
print(result**3)
print((result**3)%26000)
result=str(((result**3)%26000)/5)
print(result)
print(type(result))