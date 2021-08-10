import os




def setup():
    git_username = input("what is your github username? ")
    git_pass = input("what is your github password? ")


    directory = "crt_git"

    parent_directory = "~/automation/"


    path = os.path.join(parent_directory, directory)

    os.mkdir(path)

    print(f"created {directory} in path ${path}")



    



def open_github():
    os.system("firefox https://github.com/new")




def main():

    if not os.path.isfile("~/automation/crt_git/cred.txt"):
        setup()
    else:
        pass

    open_github()

    git_name = input("what is the name of the repo? ")

    


main()