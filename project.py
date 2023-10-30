import pathlib
import os
import shutil

# def action_options(numer_of_opt):

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
print("10. rewrite")
print("11. ")
# current_directory = os.getcwd()

# with open("db.txt", "w") as file:
#     file.write(current_directory)

def read_files(path_file):
    try:
        with open(path_file, mode = 'r', encoding='utf-8') as file:
            content = file.read()
            print("Content:")
            print(content)
              
    except FileNotFoundError:
        print("FileNotFoundError")    

def write_files(path_file):
    try:
        with open(path_file,"w") as file:
            content = file.write(input("Enter data: "))
            print("Content:")
            print(content)    
            open(path_file,"a").close()
    except FileNotFoundError:
        print("FileNotFoundError")             

def append_files_text(path_file):
    try:
        with open(path_file,"a") as file:

            content = file.write(input("Enter data: "))
            print("Content:")
            print(content)    
            open(path_file,"a").close()
            
    except FileNotFoundError:
        print("FileNotFoundError")
        

def move_files_dirs(name_input,place_input):
    try:
        
        name_input_path = pathlib.Path(name_input)
        place_input_path = pathlib.Path(place_input)
        cur_cwd = pathlib.Path.cwd()
        path_obj = cur_cwd / name_input_path
        path_place = cur_cwd / place_input_path
        move_place = shutil.move(path_obj, path_place)
        return(move_place) 
    except FileNotFoundError:
        print("FileNotFoundError")         

rep = True
while rep==True:
    user_input = int(input("Choose one of options(number:1-12) :"))

    if user_input == "exit":
        rep = False


 

    # 1. List files in a directory

    if user_input == 1:
        try :
            line_directory = pathlib.Path.cwd()
            # for i in line_directory.iterdir():
            #     print(i, i.stat(),"\n")
            # print(" ")    
            # print(os.listdir(line_directory))
            for i in line_directory.iterdir():
                file_1 = i
            
                print(i,end='')
                print(" Size: ",os.path.getsize(file_1),end=" ",)
                print(" Time: ",os.path.getatime(file_1),end=" \n ")
        except:
            print("Your are wrong")

    # 2. Create a new file

    elif user_input == 2:
        try:
            user_input = input("Enter name your file :")
            line_file = pathlib.Path.cwd()
            new_file = line_file / f"{user_input}"
            if new_file.exists() == True:
                print("You file has in this directory ")
            else :
                new_file.touch()
                print(new_file)
        except:
            print("Your are wrong")

    # 3. Create a new directory        

    elif user_input == 3:
        try:
            user_input = input("Enter name your directory :")
            line_directory = pathlib.Path.cwd()
            new_directory = line_directory / f"{user_input}"
            if new_directory.exists() == True:
                print("You directory exist in this place")
            else :
                new_directory.mkdir()
                print(new_directory)
        except:
            print("Your are wrong")

    # 4. Delete a file       

    elif user_input == 4:
        try:
            user_input = input("Enter name your file :")
            line_file = pathlib.Path.cwd()
            new_file = line_file / f"{user_input}"
            if new_file.exists() == True:
                print("You file has in this directory ")
                print("Are sure , that do you want to delite this file")
                user_agree = input("YES OR NO\n")
                if user_agree == 'YES':
                    new_file.unlink()
                    print(line_file)
                else :
                    pass
        except:
            print("Your are wrong")

    # "5. Delete a directory 

    elif user_input == 5:
        try:
            user_input = input("Enter name your directory :")
            line_directory = pathlib.Path.cwd()
            new_directory = line_directory / f"{user_input}"
            if new_directory.exists() == True:
                print("You directory existed in this place")
                print("Are sure , that do you want to delite this directory")
                user_agree = input("YES OR NO\n")
                if user_agree == 'YES':
                    new_directory.rmdir()
                    print(line_directory)
                else :
                    pass
        except:
            print("Your are wrong")

    # 6. Rename a file or directory

    elif user_input == 6:
        try:
            user_input = input("Enter name your directory or file, that you used :")
            line_directory_file = pathlib.Path.cwd()
            last_directory = line_directory_file / user_input
            user_input_new_name = input("Enter a new name of your directory or file:")
            new_directory_file = line_directory_file / user_input_new_name

            if last_directory.exists() == True:
                print("You directory or file existed in this place")
                print("Are sure , that do you want to rename this directory or file")
                user_agree = input("YES OR NO\n")
                if user_agree == 'YES':
                    last_directory.replace(new_directory_file)
                    print(line_directory_file)
                else :
                    pass
        except:
            print("Your are wrong")

    # 7. Change a folder()

    elif user_input == 7 :
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

        # 8 cwd

    elif user_input == 8 :
        cur = pathlib.Path.cwd()
        print(f"Your current directory is: {cur}") 

    elif user_input == 9 :
        user_file = input("Enter the new file path: ")
        cur_path = pathlib.Path.cwd()
        new_file = pathlib.Path(user_file)
        cur_p = cur_path / user_file
        print(cur_p)
 
        read_files(cur_p)

       
    #  10 rewrite


    elif user_input == 10 : 
        user_file = input("Enter the new file path: ")
        cur_path = pathlib.Path.cwd()
        new_file = pathlib.Path(user_file)
        cur_p = cur_path / user_file
        print(cur_p)
        f = open("demofile2.txt", "a")
        print(write_files(user_file))

#11 append tetxt

    elif user_input == 11 : 
        user_file = input("Enter the new file path: ")
        cur_path = pathlib.Path.cwd()
        new_file = pathlib.Path(user_file)
        cur_p = cur_path / user_file
        print(cur_p)
        f = open(cur_p, "a")
        print(append_files_text(user_file))

# 12 search
    elif user_input == 12 :
        user_file = input("Enter the new file path: ")
        user_word = input("Enter the word for a search: ")
        cur_path = pathlib.Path.cwd()
        new_file = pathlib.Path(user_file)
        cur_p = cur_path / user_file
        print(cur_p)     
        print(user_word)
        
        file_12=open(cur_p,'r')
        text=file_12.read()
        if user_word in text:
            print(user_word)
        else:
            print("Not found")



    elif user_input == 13 :
        name_input = input("Enter the name of the file or directory: ")
        place_input = input("Enter the place to move object: ")

        move_files_dirs(name_input,place_input)    

                 
           




    