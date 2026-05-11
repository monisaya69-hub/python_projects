f_name= input("What is your name? ")
s_name= input("What is your surname? ")
def initials(f_name, s_name):
    return f_name[0].upper() + "." + s_name[0].upper() + "."
print(initials(f_name, s_name))