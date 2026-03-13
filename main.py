import random
alphabet = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
length = int(input('Введите длину пароля: '))
password = ''
for i in range(length):
    password += random.choice(alphabet)

print('Ваш пароль: ',password)
print('Спасибо, что пользуетесь нашей программой')