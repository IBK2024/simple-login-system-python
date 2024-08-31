username1 = input("Username: ").lower()
password1 = input("Password: ")
print(f"Hello {username1}.")

while True:
    sign_in = input('Type "Sign in": ').lower()
    if sign_in == "sign in":
        while True:
            username2 = input("Username: ").lower()
            password2 = input("Password: ")
            if username2 == username1 and password2 == password1:
                break

            if username2 == username1 and password2 != password1:
                print("Password invalid")
            elif username2 != username1 and password2 == password1:
                print("Username invalid")
            else:
                print("Username and password invalid")
        break
    print("Command was not correct.")
