
import os
import pathlib

def UserInput():
    file_dir_path = input("Enter the name of the file or directory: ")
    file_dir_path_input = pathlib.Path(file_dir_path)
    cwd_dir = pathlib.Path.cwd()
    file_dir_path_final = cwd_dir / file_dir_path_input
    return file_dir_path_final

class FileManigment:
    def __init__(self, file_dir_path):
        self.file_dir_path = file_dir_path

    def create_file(self):
        try:
            new_file = self.file_dir_path

            if new_file.exists():
                print("Your file already exists in this directory")
            else:
                new_file.touch()
                print(new_file)
        except:
            print("Something went wrong")

    def create_directory(self):
        try:
            new_directory = self.file_dir_path

            if new_directory.exists() == True and os.path.isdir() == True:
                print("You directory exist in this place")
            else:
                new_directory.mkdir()
                print(new_directory)
        except:
            print("You directory exist in this place")

    def delete_file(self):
        try:
            new_file = self.file_dir_path
            if new_file.exists() == True:
                print("You file has in this directory ")
                print("Are sure , that do you want to delite this file")
                user_agree = input("YES OR NO\n")
                if user_agree == 'YES':
                    new_file.unlink()
                    print(f"{new_file} was deleted")
                else:
                    pass
        except:
            print("Your are wrong") 

    def delete_directory(self):
        try:
            print("Enter name your directory :")
            new_directory = self.file_dir_path
            if new_directory.exists() == True:
                print("You directory existed in this place")
                print("Are sure , that do you want to delite this directory")
                user_agree = input("YES OR NO\n")
                if user_agree == 'YES':
                    new_directory.rmdir()
                    print(f"{new_directory} was deleted")
                else:
                    pass
        except:
            print("Your are wrong")

    def rename_file_or_directory(self):
        try:
            user_input = input(
                "Enter name your directory or file, that you used :")
            line_directory_file = pathlib.Path.cwd()
            last_directory = line_directory_file / user_input
            user_input_new_name = input(
                "Enter a new name of your directory or file:")
            new_directory_file = line_directory_file / user_input_new_name

            if last_directory.exists() == True:
                print("You directory or file existed in this place")
                print("Are sure , that do you want to rename this directory or file")
                user_agree = input("YES OR NO\n")
                if user_agree == 'YES':
                    last_directory.replace(new_directory_file)
                    print(line_directory_file)
                else:
                    pass
        except:
                    print("Your are wrong")
                
                       

