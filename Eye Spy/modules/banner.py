from colorama import Fore,Back,Style
import platform,os

OsName = platform.uname()[0]

def banner():
    if OsName == "Windows":
      os.system("cls")
    else:
      os.system("clear")
    print(Fore.LIGHTWHITE_EX+" (               )   (       *                (                     )       (")   
    print(Fore.LIGHTWHITE_EX+" )\ )  *   )  ( /(   )\ )  (  `           (   )\ )       (       ( /(       )\ )")  
    print(Fore.LIGHTWHITE_EX+"(()/(` )  /(  )\()) (()/(  )\))(        ( )\ (()/( (     )\      )\()) (   (()/( " )
    print(Fore.LIGHTWHITE_EX+"/(_))( )(_))((_)\   /(_)_)()\       ___  )((_) /(_)))\ ((((_)(  |((_)\  )\   /(_)) ")
    print(Fore.CYAN+" (_)) (_(_())   ((_) (_))  (___()((__)|___|((_)_ (_)) ((_) )\ _ )\ |_ ((_)((_) (_)) "  )
    print(Fore.CYAN+"                 |____|\     / |____|       / __|  |   \ \     /     " )
    print(Fore.CYAN+"                 |__    \   /  |__          \__ \  |   /  \   /      " )
    print(Fore.CYAN+"                 |____|  |_|   |____|       |___/  |__|    |_|       " )
    print(Style.RESET_ALL)

banner()
