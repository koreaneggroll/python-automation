import os




def setup():
    git_username = input("what is your github username? ")
    git_pass = input("what is your github password? ")


    with open("creds.txt", "w") as creds:
        



    



def open_github():
    os.system("firefox https://github.com/new")




def main():

    if not os.path.isfile("./creds.txt"):
        setup()
    else:
        pass

    open_github()

    git_name = input("what is the name of the repo? ")

    


main()