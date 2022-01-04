# import
import shutil
import os
from platform import system

# start the project
logo = """\033[33m
______                ______                  
___  / ______ ____  _____  /________ _______ _
__  /  _  __ \_  / / /__  //_/_  __ `/_  __ `/
_  /___/ /_/ // /_/ / _  ,<   / /_/ / / /_/ / 
/_____/\____/ \__,_/  /_/|_|  \__,_/  \__,_/     


\033[32m[✔]      https://github.com/loukaa554      [✔]
\033[32m[✔]            Version 1.1.0               [✔]
\033[91m[X] Please Don't Use For illegal Activity  [X]

\033[34m[1] Reset File 
\033[34m[2] Create HTML App & Reset File 
\033[34m[3] Create React App 
\033[34m[4] Create React App & Reset File 
\033[97m
"""
print(logo)

start = input("-> ")

# reset file
if start == "1" :
    # info user .reset.css
    print("_____________________________________")
    print("")
    command = input("Add file reset Css ? [Y/n] : ")
    # condition .reset.css
    if command == "yes" or command == "y" or command == "Y" or command == "Yes" or command == "YES" or command == "" :
        print("_____________________________________")
        print("")
        fileDestination = input("File destination ? : ")
        if fileDestination != "" :
            shutil.copy2('./assets/reset.css', fileDestination)
            print("_____________________________________")
            print("")
            print("Uploaded file ✅✅✅✅")
        else : 
            print("_____________________________________")
            print("")
            print("Critical error")
    # info user .root.css
    print("_____________________________________")
    print("")
    command = input("Add file root Css ? [Y/n] : ")
    # condition .root.css
    if command == "yes" or command == "y" or command == "Y" or command == "Yes" or command == "YES" or command == "" :
        if fileDestination != "" :
            print("_____________________________________")
            print("")
            commandDestination = input("File destination is "+fileDestination+" ? [Y/n] : ")
            if command == "yes" or command == "y" or command == "Y" or command == "Yes" or command == "YES" or command == "" :
                shutil.copy2('./assets/root.css', fileDestination)
                print("_____________________________________")
                print("")
                print("Uploaded file ✅✅✅✅")
            else : 
                fileDestination = input("File destination ? : ")
                if fileDestination != "" :
                    shutil.copy2('./assets/root.css', fileDestination)
                    print("_____________________________________")
                    print("")
                    print("Uploaded file ✅✅✅✅")
                else : 
                    print("_____________________________________")
                    print("")
                    print("Critical error")
        else : 
            fileDestination = input("File destination ? : ")        
            if fileDestination != "" :
                shutil.copy2('./assets/root.css', fileDestination)
                print("_____________________________________")
                print("")
                print("Uploaded file ✅✅✅✅")
            else : 
                print("_____________________________________")
                print("")
                print("Critical error")
        
        command = input("Start VsCode ? [Y/n] : ")
        if command == "yes" or command == "y" or command == "Y" or command == "Yes" or command == "YES" or command == "" :
            os.system("cd "+fileDestination+" && code .")
        print("_____________________________________")
        print("") 
        print("Finish !!! Happy hacking !")


# create html app & reset file
if start == "2" :
    print("_____________________________________")
    print("") 
    fileDestination = input("File destination ? : ")       
    print("_____________________________________")
    print("") 
    fileName = input("Name app ? : ")
    if fileName != "" and fileDestination != "" : 
        os.system("cd "+fileDestination+" && mkdir "+fileName)
        os.system("cd "+fileDestination+"/"+fileName+" && mkdir assets && cd assets && mkdir css && mkdir js && mkdir image")
        shutil.copy2('./assets/index.html', fileDestination+"/"+fileName)
        shutil.copy2('./assets/root.css', fileDestination+"/"+fileName+"/assets/css")
        shutil.copy2('./assets/reset.css', fileDestination+"/"+fileName+"/assets/css")
        print("_____________________________________")
        print("")
        command = input("Create README.md ? [Y/n] : ")
        if command == "yes" or command == "y" or command == "Y" or command == "Yes" or command == "YES" or command == "" :
            shutil.copy2('./assets/README.md', fileDestination+"/"+fileName)
        print("_____________________________________")
        print("")
        command = input("Github init ? [y/N] : ")
        if command == "yes" or command == "y" or command == "Y" or command == "Yes" or command == "YES" :
            os.system("cd "+fileDestination+"/"+fileName+" && git init")
        print("_____________________________________")
        print("")
        command = input("Start VsCode ? [Y/n] : ")
        if command == "yes" or command == "y" or command == "Y" or command == "Yes" or command == "YES" or command == "" :
            os.system("cd "+fileDestination+"/"+fileName+" && code .")
        print("_____________________________________")
        print("") 
        print("Finish !!! Happy hacking !")
    else : 
        print("_____________________________________")
        print("") 
        print("Critical error")



# create react app 
if start == "3" : 
    print("_____________________________________")
    print("") 
    fileDestination = input("File destination ? : ")     
    print("_____________________________________")
    print("")    
    fileName = input("Name app ? : ")        
    if fileName != "" and fileDestination != "" : 
        os.system("cd "+fileDestination+" && npx create-react-app "+fileName)
        os.system("cd "+fileDestination+"/"+fileName+"/src && mkdir assets && mkdir pages && mkdir components")
        shutil.copy2('./assets/App.js', fileDestination+"/"+fileName+"/src")
        print("_____________________________________")
        print("") 
        print("Finish !!! Happy hacking !")
    else : 
        print("_____________________________________")
        print("") 
        print("Critical error")


# create react app && reset file
if start == "4" : 
    print("_____________________________________")
    print("") 
    fileDestination = input("File destination ? : ")        
    print("_____________________________________")
    print("") 
    fileName = input("Name app ? : ")        
    if fileName != "" and fileDestination != "" :
        os.system("cd "+fileDestination+" && npx create-react-app "+fileName)
        os.system("cd "+fileDestination+"/"+fileName+"/src && mkdir assets && mkdir pages && mkdir components && cd assets && mkdir css && mkdir image")
        shutil.copy2('./assets/App.js', fileDestination+"/"+fileName+"/src")
        shutil.copy2('./assets/root.css', fileDestination+"/"+fileName+"/src/assets/css")
        shutil.copy2('./assets/reset.css', fileDestination+"/"+fileName+"/src/assets/css")
        print("_____________________________________")
        print("")
        command = input("Install react-router-dom ? [Y/n] : ")
        if command == "yes" or command == "y" or command == "Y" or command == "Yes" or command == "YES" or command == "" :
            os.system("cd "+fileDestination+"/"+fileName+" && npm i react-router-dom")
        print("_____________________________________")
        print("")
        command = input("Install firebase ? [Y/n] : ")
        if command == "yes" or command == "y" or command == "Y" or command == "Yes" or command == "YES" or command == "" :
            os.system("cd "+fileDestination+"/"+fileName+" && npm i firebase")
        print("_____________________________________")
        print("")
        command = input("Start VsCode ? [Y/n] : ")
        if command == "yes" or command == "y" or command == "Y" or command == "Yes" or command == "YES" or command == "" :
            os.system("cd "+fileDestination+"/"+fileName+" && code .")
        print("_____________________________________")
        print("") 
        print("Finish !!! Happy hacking !")
    else : 
        print("Critical error")
        print("_____________________________________")
        print("") 


