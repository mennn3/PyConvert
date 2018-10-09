#
#
import youtube_dl
from termcolor import colored, cprint

#menu dari program
def menu():
    print("\n")
    print("=============================================================")
    print("|  __ \        / ____|                        | |           ")
    print("| |__) |   _  | |     ___  _ ____   _____ _ __| |_ ___ _ __ ")
    print("|  ___/ | | | | |    / _ \| '_ \ \ / / _ \ '__| __/ _ \ '__|")
    print("| |   | |_| | | |___| (_) | | | \ V /  __/ |  | ||  __/ |   ")
    print("|_|    \__, |  \_____\___/|_| |_|\_/ \___|_|   \__\___|_|   ")
    print("        __/ |                                               ")
    print("        |___/       ",(colored("Author:@naufaalrmd   [v1.0]", "green", attrs=['bold', 'blink'])))#Don't change it, noob!
    print("=============================================================")
    print("\n")
    print(colored("[1]",'red', attrs=['bold']),"\tConvert to MP4")
    print(colored("[2]",'red', attrs=['bold']),"\tConvert to MP3")
    print(colored("[3]",'red', attrs=['bold']),"\tExit.")
    print("\n")
    user_input = str(input("Choose a number between [1 - 3] = "))
    if user_input == "1":
                options1 = {
                "format" : "best[height<=?1080]",
                'extractaudio' : True,    
                'videoformat' : 'mp4',     
                }
                ydl_opts = {}
                with youtube_dl.YoutubeDL(options1) as ydl:
                    wir = str(input("Input url : ")) #user memasukan url dari yt
                    ydl.download([wir])     
                    ulang()
                    
    elif user_input == "2":
        options = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        }
        with youtube_dl.YoutubeDL(options) as ydl:
            wir = str(input("Input url : "))
            ydl.download([wir])
            
            ulang()
    elif user_input == "3":
        SystemExit("Bye-Byee ...")
    else:
        ulang()

def ulang():
    user_input = str(input("Again ? \t[Y/N] "))
    if user_input.lower() == "y":
        menu()
    elif user_input.lower() == "t":
        SystemExit()
menu()
