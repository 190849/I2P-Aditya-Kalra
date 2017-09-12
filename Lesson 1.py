print("Hello, World!")
print("5 + 6 = " , 5+6)
print("5 * 9 = " , 5*9)
print(min(1, 5, 9, 10))
print(max(2, 3, 4, 5, 1000))
print("I didnt do it")
print (eval("45/5+35/5"))
print(pow(6, 2))
print(pow(6, 32))
num = 12
for i in range(1, 11):
   print(num,'x',i,'=',num*i)
num = int(input("What number do u want?"))
for i in range (1, 12):
    print(num, 'x', i, '=' , num*i)
name = input("What's your name? ")
print("Nice to meet you " + name + "!")
age = int(input("Your age? "))
print("So, you are already " + str(age) + " years old, " + name + "!")
print("you have been alive for",  int(age) * 365, "days! Thats pretty cool")
days = int(age) * 365
print("Its pretty cool that you have been alive for", int(days) * 24, "hours!! That's a really long time!")
hours = int(days) * 24
print("In case you were wondering, you have been alive for", int(hours) * (60*60), "seconds. Woah!")
