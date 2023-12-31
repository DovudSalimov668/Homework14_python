import pathlib
import os
import shutil
from help_functions import FileManigment,UserInput


# THE OPTIONS:

print("Functions of the program:")
print(" ")
print("1. List files in a directory (show file name, its size and last modification time)")
print(" ")
print("2. Create a new file (user input file name and create it if it does not exists already)")
print(" ")
print("3. Create a new directory (show dic's parent's directory, )")
print(" ")
print("4. Delete a file (warn a user before deleting)")
print(" ")
print("5. Delete a directory (also warm the user)")
print(" ")
print("6. Rename a file or directory")
print(" ")
print("7. Change a folder (user should be able to change working  directory to another one, and do file operations in new directory)")
print(" ")
print("8. Show cwd")
print(' ')
print("9:. Develop a function which open a file and lets you edit its content and saves it.")
print(' ')
print("10. Rewriting all information inside the file")
print(' ')
print("11. Appending text inside file.")
print(' ')
print("12. Search functionality inside a selected folder")
print(' ')
print("# 13.MOVING file(s)  and directory (es) from one place to another one")

# Functions


def read_files(user_file):
    try:
        cur_path = pathlib.Path.cwd()
        new_file = pathlib.Path(user_file)
        cur_p = cur_path / new_file
        print(cur_p)

        input_num = int(input("Enter number of lines: "))
        f = open(cur_p, "r")

        for i in range(1, input_num+1):
            print(f.readline())

    except FileNotFoundError:
        print("FileNotFoundError")


def write_files(path_file):
    try:
        with open(path_file, "w") as file:
            content = file.write(input("Enter data: "))
            print("Content:")
            print(content)
            open(path_file, "a").close()
    except FileNotFoundError:
        print("FileNotFoundError")


def append_files_text(path_file):
    try:
        with open(path_file, "a") as file:

            content = file.write(input("Enter data: "))
            print("Content:")
            print(content)
            open(path_file, "a").close()

    except FileNotFoundError:
        print("FileNotFoundError")


def move_files_dirs(name_input, place_input):
    try:

        name_input_path = pathlib.Path(name_input)
        place_input_path = pathlib.Path(place_input)
        cur_cwd = pathlib.Path.cwd()
        path_obj = cur_cwd / name_input_path
        path_place = cur_cwd / place_input_path
        move_place = shutil.move(path_obj, path_place)
        return (move_place)
    except FileNotFoundError:
        print("FileNotFoundError")


def search_in_file(user_file, user_word):

    cur_path = pathlib.Path.cwd()
    new_file = pathlib.Path(user_file)
    cur_p = cur_path / new_file
    print(cur_p)
    print(user_word)

    file_12 = open(cur_p, 'r')
    text = file_12.read()
    if user_word in text:
        print(user_word)
    else:
        pass


rep = True
while rep == True:
    user_input = int(input("Choose one of options(number:1-13) :"))

    if user_input == "exit":
        rep = False
    else:
        rep = True   

    # 1. List files in a directory

    if user_input == 1:
        try:
            line_directory = pathlib.Path.cwd()

            for i in line_directory.iterdir():
                file_1 = i

                print(i, end='')
                print(" Size: ", os.path.getsize(file_1), end=" ",)
                print(" Time: ", os.path.getatime(file_1), end=" \n ")
        except:
            print("Your are wrong")

    # 2. Create a new file

    elif user_input == 2:
        FileManigment(UserInput()).create_file()
        

    # 3. Create a new directory
              
    elif user_input == 3:
        FileManigment(UserInput()).create_directory()
       

    # 4. Delete a file

    elif user_input == 4:
        FileManigment(UserInput()).delete_file()
    

    # "5. Delete a directory

    elif user_input == 5:
        FileManigment(UserInput()).delete_directory()



    # 6. Rename a file or directory

    elif user_input == 6:

        FileManigment(UserInput()).rename_file_or_directory()
       

    elif user_input == 7:
        old_dir = pathlib.Path.cwd()
        print(f"Your current directory is: {old_dir}")

        print("Are you sure you want to change your current directory?")
        user_agree = input("YES OR NO\n")

        if user_agree == 'YES':
            user_new_place = input("Enter the new directory path: ")
            new_dir = pathlib.Path(user_new_place)

            if new_dir.is_dir():
                os.chdir(new_dir)
                print(f"Your current directory has been changed to: {new_dir}")
            else:
                print(f"The path '{user_new_place}' is not a valid directory.")
        else:
            pass

        # Show CWD

    elif user_input == 8:
        cur = pathlib.Path.cwd()
        print(f"Your current directory is: {cur}")


# 9. read

    elif user_input == 9:
        user_file = input("Enter the new file path: ")

        print(read_files(user_file))


# 10. Rewriting all information inside the file

    elif user_input == 10:
        user_file = input("Enter the new file path: ")

        print(write_files(user_file))

# 11. Appending text inside file.

    elif user_input == 11:
        user_file = input("Enter the new file path: ")

        print(append_files_text(user_file))


# 12. Search functionality inside a selected folder

    elif user_input == 12:
        search_in_file(user_file=input("Enter the new file path: "),
                       user_word=input("Enter the word for a search: "))


# 13.MOVING file(s)  and directory (es) from one place to another one

    elif user_input == 13:
        name_input = input("Enter the name of the file or directory: ")
        place_input = input("Enter the place to move object: ")

        move_files_dirs(name_input, place_input)
