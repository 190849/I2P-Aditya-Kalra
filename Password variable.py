

v_password = str (input("please input your password"))
v_count = 1
while v_password != "password":
    print("incorrect password")
    print("you have entered", v_count, "times")
    v_count += 1
    if v_count >= 4:
        print("Sorry you have entered", v_count, "times, you're kicked")
        break
    else:
        v_password = str(input("Please input Password Again"))
else:
    print("access granted. ")
