# import pathlib

# # THE OPTIONS:

# print("Functions of the program:")
# print(" ")
# print("1. List files in a directory (show file name, its size and last modification time)")
# print(" ")
# print("2. Create a new file (user input file name and create it if it does not exists already)")
# print(" ")
# print("3. Create a new directory (show dic's parent's directory, )")
# print(" ")
# print("4. Delete a file (warn a user before deleting)")
# print(" ")
# print("5. Delete a directory (also warm the user)")
# print(" ")
# print("6. Rename a file or directory")
# print(" ")
# print("7. Change a folder (user should be able to change working  directory to another one, and do file operations in new directory)")
# print(" ")


# # END OF OPTIONS

# # CHOOSING THE OPTION
# your_choice = 0
# def choose_option(n):
 
#     if n==1:
#         your_choice = n
#         print("You choosed option number: 1")
#     elif n==2:
#         your_choice = n
#         print("You choosed option number: 2")
#     elif n==3:
#         your_choice = n 
#         print("You choosed option number: 3")       
#     elif n==4:
#         your_choice = n
#         print("You choosed option number: 4")
#     elif n==5:
#         your_choice = n 
#         print("You choosed option number: 5")       
#     elif n==6:
#         your_choice = n
#         print("You choosed option number: 6")
#     elif n==7:
#         your_choice = n
#         print("You choosed option number: 7")
#     if n>7 or n<1:
#         print("Choice the functions beetwen 1 and 7, please.") 
#     def functions_work(num):
#         if num==2:
#             creating_file(file_name)


# choise_opt = int(input("To choose the option, enter the number of  one of them: "))

# print(choose_option(choise_opt))

# # CHOOSING THE OPTION     

# # FUNCTIONS OF PROGRAM

# # 2 

# def creating_file(file_name):
#     path = pathlib.Path.cwd() / "file_name"
#     True_False_file =  path.exists()
#     Is_file_check = path.is_file()
#     if True_False_file== True and Is_file_check==True:
#         print("File with same name already exists, please enter another file name")
#     else:
#         path.touch()

# file_name = ("Input file name:")
import os
import pathlib
# print(dir(os))  

    
       