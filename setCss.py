# import
import shutil
import os
from platform import system

# start the project
logo = """\033[33m
______                ______          
___  / ______ ____  _____  /________ _
__  /  _  __ \_  / / /__  //_/_  __ `/
_  /___/ /_/ // /_/ / _  ,<   / /_/ / 
/_____/\____/ \__,_/  /_/|_|  \__,_/       


\033[32m[✔]      https://github.com/loukaa554      [✔]
\033[32m[✔]            Version 1.1.0               [✔]
\033[91m[X] Please Don't Use For illegal Activity  [X]

\033[34m[1] Reset File 
\033[34m[2] Creat React App 
\033[34m[3] Creat React App & Reset File 
\033[97m
"""
print(logo)

start = input("-> ")

# reset file
if start == "1" :
    # info user .reset.css
    command = input("Add file reset Css ? [Y/n] : ")
    # condition .reset.css
    if command == "yes" or command == "y" or command == "Y" or command == "Yes" or command == "YES" or command == "" :
        fileDestination = input("File destination ? : ")
        if fileDestination != "" :
            shutil.copy2('C:/Project/set/assets/.reset.css', fileDestination)
            print("Uploaded file ✅✅✅✅")
        else : 
            print("Critical error")
    # info user .root.css
    command = input("Add file root Css ? [Y/n] : ")
    # condition .root.css
    if command == "yes" or command == "y" or command == "Y" or command == "Yes" or command == "YES" or command == "" :
        if fileDestination != "" :
            commandDestination = input("File destination is "+fileDestination+" ? [Y/n] : ")
            if command == "yes" or command == "y" or command == "Y" or command == "Yes" or command == "YES" or command == "" :
                shutil.copy2('C:/Project/set/assets/.root.css', fileDestination)
                print("Uploaded file ✅✅✅✅")
            else : 
                fileDestination = input("File destination ? : ")
                if fileDestination != "" :
                    shutil.copy2('C:/Project/set/assets/.root.css', fileDestination)
                    print("Uploaded file ✅✅✅✅")
                else : 
                    print("Critical error")
        else : 
            fileDestination = input("File destination ? : ")        
            if fileDestination != "" :
                shutil.copy2('C:/Project/set/assets/.root.css', fileDestination)
                print("Uploaded file ✅✅✅✅")
            else : 
                print("Critical error")


# create react app 
if start == "2" : 
    fileDestination = input("File destination ? : ")        
    fileName = input("Name app ? : ")        
    if fileName != "" and fileDestination != "" : 
        os.system("cd "+fileDestination+" && npx create-react-app "+fileName)
        os.system("cd "+fileName+"/src && mkdir assets && mkdir pages && mkdir components")
        shutil.copy2('C:/Project/set/assets/App.js', fileDestination+"/"+fileName+"/src")
    else : 
        print("Critical error")


# create react app && reset file
if start == "3" : 
    fileDestination = input("File destination ? : ")        
    fileName = input("Name app ? : ")        
    if fileName != "" and fileDestination != "" :
        os.system("cd "+fileDestination+" && npx create-react-app "+fileName)
        os.system("cd "+fileDestination+"/"+fileName+"/src && mkdir assets && mkdir pages && mkdir components && cd assets && mkdir css && mkdir image")
        shutil.copy2('C:/Project/set/assets/App.js', fileDestination+"/"+fileName+"/src")
        shutil.copy2('C:/Project/set/assets/.root.css', fileDestination+"/"+fileName+"/src/assets/css")
        shutil.copy2('C:/Project/set/assets/.reset.css', fileDestination+"/"+fileName+"/src/assets/css")
        command = input("Install react-router-dom ? [Y/n] : ")
        if command == "yes" or command == "y" or command == "Y" or command == "Yes" or command == "YES" or command == "" :
            os.system("cd "+fileDestination+"/"+fileName+" && npm i react-router-dom")
        command = input("Install firebase ? [Y/n] : ")
        if command == "yes" or command == "y" or command == "Y" or command == "Yes" or command == "YES" or command == "" :
            os.system("cd "+fileDestination+"/"+fileName+" && npm i firebase")
        command = input("Start VsCode ? [Y/n] : ")
        if command == "yes" or command == "y" or command == "Y" or command == "Yes" or command == "YES" or command == "" :
            os.system("cd "+fileDestination+"/"+fileName+" && code .")
    else : 
        print("Critical error")


