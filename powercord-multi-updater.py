import os
from time import sleep

print("---> xxxcept | im gonna update your stuff")

try:
    if not os.path.exists(R"src\Powercord\plugins"):
        raise NotADirectoryError("Failed to find powercord directory!")

    if not os.path.exists(R"src\Powercord\themes"):
        raise NotADirectoryError("Failed to find powercord directory!")

    print("Updating Plugins...\n")
    os.chdir("src\Powercord\plugins")

    for plugin in os.listdir():
        if plugin == ".exists":
            break

        os.chdir(plugin)
        os.system("git pull")
        os.chdir("..")

    print("Plugins updated.\n")
    os.chdir("..")

    print("Updating Themes...\n")
    os.chdir("themes")

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
