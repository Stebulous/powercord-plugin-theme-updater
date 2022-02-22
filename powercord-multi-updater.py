import os
from time import sleep
from tkinter import Tk, filedialog

print(r'''  _______ _                             _______  _             _       
 |__   __| |                           / /  __ \| |           (_)      
    | |  | |__   ___ _ __ ___   ___   / /| |__) | |_   _  __ _ _ _ __  
    | |  | '_ \ / _ \ '_ ` _ \ / _ \ / / |  ___/| | | | |/ _` | | '_ \ 
    | |  | | | |  __/ | | | | |  __// /  | |    | | |_| | (_| | | | | |
    |_|  |_| |_|\___|_| |_| |_|\___/_/   |_|    |_|\__,_|\__, |_|_| |_|
         _    _ _____  _____       _______ ______ _____   __/ |        
        | |  | |  __ \|  __ \   /\|__   __|  ____|  __ \ |___/         
        | |  | | |__) | |  | | /  \  | |  | |__  | |__) |              
        | |  | |  ___/| |  | |/ /\ \ | |  |  __| |  _  /               
        | |__| | |    | |__| / ____ \| |  | |____| | \ \               
         \____/|_|    |_____/_/    \_\_|  |______|_|  \_\              
                                                                       
                                                                       ''')

root = Tk()
root.withdraw()

chosendir = filedialog.askdirectory(parent=root,initialdir="/",title='Please select your Powercord root directory')

try:
    powercord_dir = os.path.join(chosendir, r"src\Powercord")
    themes_dir = os.path.join(powercord_dir, "themes")
    plugins_dir = os.path.join(powercord_dir, "plugins")
    
    if not (os.path.exists(themes_dir) and os.path.exists(plugins_dir)):
        raise NotADirectoryError("Failed to find powercord directory!")

    print("Finding Plugins...\n")
    os.chdir(plugins_dir)
    totalplugins = 0

    for plugin in os.listdir():
        if plugin == ".exists":
            continue

        totalplugins += 1

    print('Plugins found:' + str(totalplugins))
    sleep(1)
    print("\nUpdating Plugins!\n")

    for plugin in os.listdir():
        if plugin == ".exists":
            continue

        print("\nUpdating plugin: " + plugin + "...\n")
        os.chdir(plugin)
        os.system("git pull")
        os.chdir("..")

    print(str(totalplugins) + " Plugins updated.\n")
    os.chdir("..")

    print("Finding themes...\n")
    os.chdir(themes_dir)
    
    totalthemes = 0

    for theme in os.listdir():
        if theme == ".exists":
            continue

        totalthemes += 1

    print("Themes found: " + str(totalthemes))
    sleep(1)
    print("\nUpdating Themes!\n")

    for theme in os.listdir():
        if theme == ".exists":
            continue

        print("\nUpdating theme: " + theme + "...\n")
        os.chdir(theme)
        os.system("git pull")
        os.chdir("..")

    print(str(totalthemes) + " Themes updated.\n")
    print("\n\n All done!")
    sleep(5)
except Exception as err:
    print(err)
    sleep(5)
    quit(1)
