from main_page import command
import webbrowser as web
import os, time
import subprocess as sub


def def_command():
    # ========= Sites =========
    if command == "youtube":
        print(f"                    || open {command}.. ||")
        web.open("https://www.youtube.com/")
        
    if command == "web telegram":
        print(f"                    || open {command}.. ||")
        web.open("https://web.telegram.org/")
        
    if command == "github":
        print(f"                    || open {command}.. ||")
        web.open("https://github.com/")
        
    if command == "chatgpt":
        print(f"                    || open {command}.. ||")
        web.open("https://chatgpt.com/")
        
    if command == "claude":
        print(f"                    || open {command}.. ||")
        web.open("https://claude.com/")
        
    if command == "typerun":
        print(f"                    || open {command}.. ||")
        web.open("https://typerun.top/#eng_basic")
        
    if command == "gmail":
        print(f"                    || open {command}.. ||")
        web.open("https://mail.google.com/")
        
    if command == "virus total":
        print(f"                    || open {command}.. ||")
        web.open("https://www.virustotal.com/")
        
    if command == "virustotal":
        print(f"                    || open {command}.. ||")
        web.open("https://www.virustotal.com/")
        
    if command == "google":
        print(f"                    || open {command}.. ||")
        web.open("http://www.google.com/")
        
    if command == "twitch":
        print(f"                    || open {command}.. ||")
        web.open("https://www.twitch.tv/")
        
    if command == "kick":
        print(f"                    || open {command}.. ||")
        web.open("https://www.kick.com")
        
    if command == "python":
        print(f"                    || open {command}.. ||")
        web.open("https://www.python.org")
        
    if command == "jetbrains":
        print(f"                    || open {command}.. ||")
        web.open("https://www.jetbrains.com/")
        
    if command == "web spotify":
        print(f"                    || open {command}.. ||")
        web.open("http://open.spotify.com/")
        
    if command == "web soundcloud":
        print(f"                    || open {command}.. ||")
        web.open("https://soundcloud.com/")
        
    
    # ========= Apps =========
    if command == "notepad":
        print(f"                    || open {command}.. ||")
        os.system("notepad.exe")
        
    if command == "pycharm":
        print(f"                    || open {command}.. ||")
        os.system("start pycharm")
        
    if command == "code":
        print(f"                    || open {command}.. ||")
        os.system("start code")
        
    if command == "cmd":
        print(f"                    || open {command}.. ||")
        os.system("start cmd")
        
    if command == "explorer":
        print(f"                    || open {command}.. ||")
        os.system("start explorer")
        
    if command == "calculator":
        print(f"                    || open {command}.. ||")
        os.system("start calc")
        
    if command == "calc":
        print(f"                    || open {command}.. ||")
        os.system("start calc")
        
    if command == "chrome":
        print(f"                    || open {command}.. ||")
        os.system("start chrome")
        
    if command == "discord":
        print(f"                    || open {command}.. ||")
        os.system("start discord:")
        
    if command == "ds":
        print(f"                    || open {command}.. ||")
        os.system("start discord:")
        
    if command == "telegram":
        print(f"                    || open {command}.. ||")
        os.system("start tg:")
        
    if command == "tg":
        print(f"                    || open {command}.. ||")
        os.system("start tg:")
        
    if command == "steam":
        print(f"                    || open {command}.. ||")
        os.system("start steam:")
        
    if command == "visual studio":  
        print(f"                    || open {command}.. ||")
        os.system("start devenv")
        
    if command == "vs":            
        print(f"                    || open {command}.. ||")
        os.system("start devenv")
        
    if command == "vs code":  
        print(f"                    || open {command}.. ||")
        os.system("start code")
        
    if command == "spotify":
        print(f"                    || open {command}.. ||")
        os.system("start spotify")
        
        
    # ========= add site =========
    if command == "add a site":
        create_name = input("\nOkay, enter the website name.\n>> ")
        create_link = input("Please enter the link to your website.\n>> ")
        
        os.system("cls")
        print(r"  _____ ___  ___ ")
        print(r" |_   _/ _ \/ __|   Enter the name of the")
        print(r"   | || (_) \__ \   website or app to open it.")
        command2 = input(r"   |_| \___/|___/   >> ").lower()
    
        if command2 == create_name:
            print(f"                    || open {create_name}.. ||")
            web.open(create_link)
    
        if command2 == "stop":
            exit
        if command2 == "exit":
            exit
            
    # ========= add app =========
    if command == "add an app":
        create_app_name = input("\nOkay, enter the app name. \n>> ")
        os.system("cls")
        print(r"  _____ ___  ___ ")
        print(r" |_   _/ _ \/ __|   Enter the name of the")
        print(r"   | || (_) \__ \   website or app to open it.")
        command2 = input(r"   |_| \___/|___/   >> ").lower()
        
        if command2 == create_app_name:
            os.system(f"start {create_app_name}")
            
    # ========= help =========
    if command == "help":
        print('\nTo open an app or website using a command, \nsimply enter its name. If you want to \nfind out the commands, type "commands".')
        print("\n|| Restart the utility. ||\n")
        time.sleep(5)
        
    # -------- commands ---------
    if command == "commands":
        print("Here are all the existing commands.\n")
        print("help\ncommands\nlanguage\nadd an app\nadd a site\nyoutube\nweb telegram\ngithub\nchatgpt\nclaude\ntyperun\ngmail\nvirus total\ngoogle\ntwitch\nkick\npython\njetbrains\nweb spotify\nweb soundcloud\nnotepad\npycharm\ncode\ncmd\nexplorer\ncalculator\nchrome\ndiscord\ntelegram\nsteam\nvisual studio\nspotify\n")
        input("|| Press any key to close. ||  ")
        
    # ========= language =========
    if command == "language":
        print("Choose the language you need \nfrom the options provided.\n")
        print("[+] English\n[+] Русский\n")
        language = input(">> ").lower()
        
        # --------- Russian language ---------
        if language == "русский":
            os.system("cls")
            print(r"  _____ ___  ___ ")
            print(r" |_   _/ _ \/ __|   Введите имя сайта")
            print(r"   | || (_) \__ \   или приложения чтобы открыть его.")
            command3 = input(r"   |_| \___/|___/   >> ").lower()
            
            if command3 == "язык":
                print("\nВыберете язык который вам нужен \nиз предложенных.\n")
                print("[+] Русский\n[+] English\n")
                language = input(">> ").lower()
                
        print("\nИзвините, русский язык не доработан. \nНикакие команды при русском языке не работают.")
        time.sleep(2)
        exit