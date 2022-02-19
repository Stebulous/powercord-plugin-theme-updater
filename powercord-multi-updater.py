import os
from time import sleep
from tkinter import Tk, filedialog

print(r"Powercord Theme/Plugin Updater")

root = Tk()
root.withdraw()

chosendir = filedialog.askdirectory(parent=root,initialdir="/",title='Please select your Powercord root directory')

try:
    powercord_dir = os.path.join(chosendir, r"src\Powercord")
    themes_dir = os.path.join(powercord_dir, "themes")
    plugins_dir = os.path.join(powercord_dir, "plugins")
    
    if not (os.path.exists(themes_dir) and os.path.exists(plugins_dir)):
        raise NotADirectoryError("Failed to find powercord directory!")

    print("Updating Plugins...\n")
    os.chdir(plugins_dir)

    for plugin in os.listdir():
        if plugin == ".exists":
            break

        os.chdir(plugin)
        os.system("git pull")
        os.chdir("..")

    print("Plugins updated.\n")
    os.chdir("..")

    print("Updating Themes...\n")
    os.chdir(themes_dir)

    for theme in os.listdir():
        if theme == ".exists":
            break

        os.chdir(theme)
        os.system("git pull")
        os.chdir("..")

    print("Themes updated.\n")
except Exception as err:
    print(err)
    sleep(5)
    quit(1)
