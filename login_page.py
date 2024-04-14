import re
regex = r"^[a-zA-Z0-9_.+-]+@gmail+\.com+$"
def authenticate():
    pass
def register():
    db = open("test.txt","r") 
    email = str(input())
    authenticate(email)
    password = str(input())
    re_password = str(input())
    if password != re_password:
        print("Password re-entered does not match ")
        register()
    else:
        if len(password) < 8:
            print("Password should be eight characters long ")
            register()
        elif email in db:
            print("Email already exists ")
            register()
        else:
            db.open()
            db.write(email)
            db.write(password)
            print("success")
#print(f.read())
def login():
    db = open("test.txt","r") 
    email = str(input())
    authenticate(email)
    password = str(input())
    if(email not in db):
        print("Email does not match")
        login()
    else:
        if(password not in db):
            print("Password does not match")
            login()
        else:
            print("success")


    

def authenticate(email):
    if(re.match(regex, email)):
        print("Valid Email")
 
    else:
        print("invalid")
        login()
register()
