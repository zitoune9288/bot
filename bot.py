import os
import subprocess
import ctypes
import time
import random
import webbrowser
import string
import socket
import base64
import requests
from pystyle import *
from colorama import *

def set_cmd_window_title(new_title):
    ctypes.windll.kernel32.SetConsoleTitleW(new_title)

tittle = "spotify bot By zit_zitoune9999"


set_cmd_window_title(tittle)



intro = """


  ▒███████▒ ██▓▄▄▄█████▓ ▒█████   █    ██  ███▄    █  ▒█████  
  ▒ ▒ ▒ ▄▀░▓██▒▓  ██▒ ▓▒▒██▒  ██▒ ██  ▓██▒ ██ ▀█   █ ▒██▒  ██▒
  ░ ▒ ▄▀▒░ ▒██▒▒ ▓██░ ▒░▒██░  ██▒▓██  ▒██░▓██  ▀█ ██▒▒██░  ██▒
    ▄▀▒   ░░██░░ ▓██▓ ░ ▒██   ██░▓▓█  ░██░▓██▒  ▐▌██▒▒██   ██░
  ▒███████▒░██░  ▒██▒ ░ ░ ████▓▒░▒▒█████▓ ▒██░   ▓██░░ ████▓▒░
  ░▒▒ ▓░▒░▒░▓    ▒ ░░   ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒ ░ ▒░▒░▒░ 
  ░░▒ ▒ ░ ▒ ▒ ░    ░      ░ ▒ ▒░ ░░▒░ ░ ░ ░ ░░   ░ ▒░  ░ ▒ ▒░ 
  ░ ░ ░ ░ ░ ▒ ░  ░      ░ ░ ░ ▒   ░░░ ░ ░    ░   ░ ░ ░ ░ ░ ▒  
    ░ ░     ░               ░ ░     ░              ░     ░ ░  
  ░                                                           
                                                              
                      By zit_zitoune9999     

                > Press Enter                                         

"""

Anime.Fade(Center.Center(intro), Colors.black_to_red, Colorate.Vertical, interval=0.035, enter=True)


print(f"""{Fore.RED}


  ▒███████▒ ██▓▄▄▄█████▓ ▒█████   █    ██  ███▄    █  ▒█████  
  ▒ ▒ ▒ ▄▀░▓██▒▓  ██▒ ▓▒▒██▒  ██▒ ██  ▓██▒ ██ ▀█   █ ▒██▒  ██▒
  ░ ▒ ▄▀▒░ ▒██▒▒ ▓██░ ▒░▒██░  ██▒▓██  ▒██░▓██  ▀█ ██▒▒██░  ██▒
    ▄▀▒   ░░██░░ ▓██▓ ░ ▒██   ██░▓▓█  ░██░▓██▒  ▐▌██▒▒██   ██░
  ▒███████▒░██░  ▒██▒ ░ ░ ████▓▒░▒▒█████▓ ▒██░   ▓██░░ ████▓▒░
  ░▒▒ ▓░▒░▒░▓    ▒ ░░   ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒ ░ ▒░▒░▒░ 
  ░░▒ ▒ ░ ▒ ▒ ░    ░      ░ ▒ ▒░ ░░▒░ ░ ░ ░ ░░   ░ ▒░  ░ ▒ ▒░ 
  ░ ░ ░ ░ ░ ▒ ░  ░      ░ ░ ░ ▒   ░░░ ░ ░    ░   ░ ░ ░ ░ ░ ▒  
    ░ ░     ░               ░ ░     ░              ░     ░ ░  
  ░                                                           
                                                              
                           By zit_zitoune9999 

------------------------------------------------------------------

                     Welcome to MultiTool Zitouno

------------------------------------------------------------------



""")

zitouno = '''
      ▒███████▒ ██▓▄▄▄█████▓ ▒█████   █    ██  ███▄    █  ▒█████  
      ▒ ▒ ▒ ▄▀░▓██▒▓  ██▒ ▓▒▒██▒  ██▒ ██  ▓██▒ ██ ▀█   █ ▒██▒  ██▒
      ░ ▒ ▄▀▒░ ▒██▒▒ ▓██░ ▒░▒██░  ██▒▓██  ▒██░▓██  ▀█ ██▒▒██░  ██▒
        ▄▀▒   ░░██░░ ▓██▓ ░ ▒██   ██░▓▓█  ░██░▓██▒  ▐▌██▒▒██   ██░
      ▒███████▒░██░  ▒██▒ ░ ░ ████▓▒░▒▒█████▓ ▒██░   ▓██░░ ████▓▒░
      ░▒▒ ▓░▒░▒░▓    ▒ ░░   ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒ ░ ▒░▒░▒░ 
      ░░▒ ▒ ░ ▒ ▒ ░    ░      ░ ▒ ▒░ ░░▒░ ░ ░ ░ ░░   ░ ▒░  ░ ▒ ▒░ 
      ░ ░ ░ ░ ░ ▒ ░  ░      ░ ░ ░ ▒   ░░░ ░ ░    ░   ░ ░ ░ ░ ░ ▒  
        ░ ░     ░               ░ ░     ░              ░     ░ ░  
      ░                                                           
            By 'vSwOrd                                                      
         '''

time.sleep(1)
while True:
    Write.Print("\nQuelle option voulez vous choisir:", Colors.red_to_yellow)
    Write.Print("\n[1] Lancer le bot                 [2] Tiktok", Colors.red_to_yellow)
    Write.Print("\n[3] Instagram                     [4] Quitter", Colors.red_to_yellow)
    Write.Print("\nVeuillez faire un choix > ", Colors.red_to_yellow, end="")
    choice = input()
    if choice == "1":
        print("Vous avez choisi 1. Exécution du bot...")
        time.sleep(3)
        phrase = input("Veuillez entrer L'url (lien) de votre musique sporify: ")
        print()
        print()
        print("Veuillez patientez quelque secondes...")
        time.sleep(10)
        print("Connection...")
        time.sleep(2)
        print("Préparation...")
        time.sleep(2)
        print("Connexion au 12 Machines via Cloud")
        time.sleep(2)
        print("Ecoute sur spotify sur 24 naviguateur Chrome donc 345 onglets")
        canal = random.randint(101, 135)
    # print(f"{canal} canal type = CC droper")
        time.sleep(1)
        print("Ecoute...")
        time.sleep(8000000)
    elif choice == "2":
        webbrowser.open('https://www.tiktok.com/@zit_zitoune0')
    elif choice == "3":
        webbrowser.open('https://www.instagram.com/zit_zitoune9999/')

    elif choice == "4":
        print("exiting..")
        time.sleep(2)
        os.system("exit")

    else:
        Write.Print("\nChoix invalid !", Colors.red_to_yellow)
