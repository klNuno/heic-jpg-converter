from PIL import Image
import pillow_heif
import os
import time


import colorama
from colorama import Fore
colorama.init()

def credits():
    print(Fore.GREEN + """
 ____________________________________________________________________________________________
|                                                                                            |     
|  __                __                   __                                       by klNuno |
| /  |              /  |                 /  |                                                |
| $$ |____   ______ $$/  _______        _$$ |_    ______               __  ______   ______   |
| $$      \ /      \/  |/       |      / $$   |  /      \             /  |/      \ /      \  |
| $$$$$$$  /$$$$$$  $$ /$$$$$$$/       $$$$$$/  /$$$$$$  |            $$//$$$$$$  /$$$$$$  | |
| $$ |  $$ $$    $$ $$ $$ |              $$ | __$$ |  $$ |            /  $$ |  $$ $$ |  $$ | |
| $$ |  $$ $$$$$$$$/$$ $$ \_____         $$ |/  $$ \__$$ |            $$ $$ |__$$ $$ \__$$ | |
| $$ |  $$ $$       $$ $$       |        $$  $$/$$    $$/             $$ $$    $$/$$    $$ | |
| $$/   $$/ $$$$$$$/$$/ $$$$$$$/          $$$$/  $$$$$$/         __   $$ $$$$$$$/  $$$$$$$ | |
|                                                              /  \__$$ $$ |     /  \__$$ |  |
|                                                              $$    $$/$$ |     $$    $$/   |
|                                                               $$$$$$/ $$/       $$$$$$/    |
|____________________________________________________________________________________________|
          """ + Fore.RESET)
    
def createFolders() -> None :
    try:
        print("Creating Input and Output...")
        os.mkdir("./input")
        os.mkdir("./output")
    except:
        print(Fore.YELLOW + "Warning : Input and Output already exists" + Fore.RESET)
        
def checkInput(folder : list) -> None :
    if folder == [] :
        print('')
        print(Fore.RED + 'ERROR : Input Folder empty, exiting...' + Fore.RESET)
        time.sleep(3)
        quit()
    for e in folder:
        if e[-5:].lower() != ".heic":
            print('')
            print(Fore.RED + 'ERROR : All files MUST be .heic !!' + Fore.RESET)
            time.sleep(3)
            quit()
            
def checkOutput() -> None :
    if os.listdir("./output") != []:
        print('')
        print(Fore.RED + 'ERROR : Output Folder not empty, exiting...' + Fore.RESET)
        time.sleep(3)
        quit()
    

def main():
    credits()
    createFolders()
    print('')
    input('Copy your .HEIC files into the input folder and press ENTER')
        
    pillow_heif.register_heif_opener()
    
    inputFolder = os.listdir("./input")
    
    checkInput(inputFolder)
    checkOutput()
    
    
        
    a=0
    while not (a == "Y" or a == "y" or a == "N" or a == "n"):
        a=input('Do you want to keep original .HEIC ? Y / N : ')
    
    i=0
    feur=" " * 50
    print('')
    if (a == "Y" or a == "y"):
        for e in inputFolder:
            i+=1
            print('\r{}'.format(f'[{i}/{len(inputFolder)}] Converting "{e}"'+feur), end="")
            Image.open('./input/' + e).save('./output/' + e[:-5] + '.jpg', quality=100)
            
            
    else:
        for e in inputFolder:
            i+=1
            print('\r{}'.format(f'[{i}/{len(inputFolder)}] Converting "{e}"'+feur), end="")
            Image.open('./input/' + e).save('./output/' + e[:-5] + '.jpg', quality=100)
            os.remove('./input/' + e)
        
    input("\n\n" + Fore.GREEN + 'Finished !' + Fore.RESET)


main()
















