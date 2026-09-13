#python TheOpenSupport.py
import os
import webbrowser
print("eng:\nWelcome to TOS\nEnter the name of the app or website to open it.\n")
print("ru:\nДобро пожаловать в TOS\nВведите имя приложения или сайта чтобы открыть его.\n")

while True:
    command = input(">> ").lower()
    
    
    #русская версия  / russian version
    #сайты / sites
    if command == "ютуб":
        webbrowser.open('www.youtube.com')
        
    elif command == "телеграм сайт":
        webbrowser.open('https://web.telegram.org/')
        
    elif command == "гитхаб":
        webbrowser.open('https://github.com/')
        
    elif command == "гитхаб разработчика":
        webbrowser.open('https://github.com/DewGit3')
        
    elif command == "чат гпт":
        webbrowser.open('https://chatgpt.com/uc/6aa296e2-980c-83ea-9095-e25ceac01998')
        
    elif command == "клод":
        webbrowser.open('https://claude.com/')
        

    #приложения / apps
    elif command == "хром":
        os.system("start chrome")
        
    elif command == "фаерфокс":
        os.system("start firefox")
        
    elif command == "дискорд":
        os.system("start discord:")
        
    elif command == "телеграм":
        os.system("start tg:")
        
    elif command == "тг":
        os.system("start tg:")
    
    elif command == "стим":
        os.system("start steam:")
        
    elif command == "консоль":
        os.system("start cmd")
        
    elif command == "калькулятор":
        os.system("start calc")
        
    elif command == "блокнот":
        os.system("start notepad")
        
    elif command == "проводник":
        os.system("start explorer")
        
    elif command == "вс код":  
        os.system("start code")
    
    
    #английская версия / english version
    #сайты / sites:
    elif command == "youtube":
        webbrowser.open('https://www.youtube.com')
        
    elif command == "telegram site":
        webbrowser.open('https://web.telegram.org/')

    elif command == "github":
        webbrowser.open('https://github.com/')
    
    elif command == "github developer":
        webbrowser.open('https://github.com/DewGit3')
        
    elif command == "chat GPT":
        webbrowser.open('https://chatgpt.com/uc/6aa296e2-980c-83ea-9095-e25ceac01998')  
        
    elif command == "Claude":
        webbrowser.open('https://claude.com/')
        
    elif command == "spotify":
        webbrowser.open('https://open.spotify.com')


    #приложения / apps    
    elif command == "chrome":
        os.system("start chrome")
        
    elif command == "firefox":
        os.system("start firefox")
        
    elif command == "discord":
        os.system("start discord:")
        
    elif command == "telegram":  
        os.system("start tg:")
        
    elif command == "tg":        
        os.system("start tg:")
    
    elif command == "steam":
        os.system("start steam:")
        
    elif command == "console":
        os.system("start cmd")
    
    elif command == "vs code":  
        os.system("start code")
        
    elif command == "code":     
        os.system("start code")
    
    elif command == "visual studio":  
        os.system("start devenv")
    
    elif command == "vs":            
        os.system("start devenv")
        
    elif command == "calc":
        os.system("start calc")
        
    elif command == "notepad":
        os.system("start notepad")
        
    elif command == "explorer":
        os.system("start explorer")
        
    elif command == "spotify":
        os.system("start spotify")
    
    
    #конец / end
    elif command == "close":
        break
    elif command == "stop":
        break
    

    else:
        print("The command is invalid.")