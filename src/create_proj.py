import os


c_proj = "C"
cpp_proj = "C++"
py_proj = "python"
web_proj = "web"


def evaluate(x):
    if x == c_proj:
        dirName = input("name of the project? ")

        create_c_proj(dirName)
    

    elif x == cpp_proj:
        dirName = input("name of the project? ")


        create_cpp_proj(dirName)


    elif x == py_proj:
        dirName = input("name of the project? ")

        create_py_proj(dirName)


    elif x == web_proj:
        dirName = input("name of the project? ")

        create_web_proj(dirName)


    else:
        print(f"No option '{x}'")




def create_c_proj(dirName):
    try:
        os.mkdir(dirName)
        print(f"Directory {dirName} created")


    except FileExistsError:
        print(f"Directory {dirName} already exists")



def create_cpp_proj(dirName):
    try:
        os.mkdir(dirName)
        print(f"Directory {dirName} created")

        
    except FileExistsError:
        print(f"Directory {dirName} already exists")



def create_py_proj(dirName):
    try:
        os.mkdir(dirName)
        print(f"Directory {dirName} created")


    except FileExistsError:
        print(f"Directory {dirName} already exists")



def create_web_proj(dirName):
    try:
        os.mkdir(dirName)
        print(f"Directory {dirName} created")


    except FileExistsError:
        print(f"Directory {dirName} already exists")




def create_main_file(dirName):
    dirLocation = dirName + "/src/"

    os.mkdir(dirLocation)



def main():
    project_language = input("What's your project's language of choice? ")

    evaluate(project_language)

main()