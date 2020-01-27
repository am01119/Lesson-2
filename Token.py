print('Hello')


import random
Token = random.randrange(100000,999999)

print(Token)

Token2 = int(input("Please input your token digits: "))

if Token2 == Token:
	print('Transaction successful')
else:
	print('Transaction unsuccessful')


input()