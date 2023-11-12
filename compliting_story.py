import os

print("""
\033[1;32m
▄▄▄█████▓ ▒█████  ▒██   ██▒ ██▓ ▄████▄  
▓  ██▒ ▓▒▒██▒  ██▒▒▒ █ █ ▒░▓██▒▒██▀ ▀█  
▒ ▓██░ ▒░▒██░  ██▒░░  █   ░▒██▒▒▓█    ▄ 
░ ▓██▓ ░ ▒██   ██░ ░ █ █ ▒ ░██░▒▓▓▄ ▄██▒
  ▒██▒ ░ ░ ████▓▒░▒██▒ ▒██▒░██░▒ ▓███▀ ░
  ▒ ░░   ░ ▒░▒░▒░ ▒▒ ░ ░▓ ░░▓  ░ ░▒ ▒  ░
    ░      ░ ▒ ▒░ ░░   ░▒ ░ ▒ ░  ░  ▒   
  ░      ░ ░ ░ ▒   ░    ░   ▒ ░░        
             ░ ░   ░    ░   ░  ░ ░      
                               ░        

\033[0;31m════════════════════════════════════════════
\033[0;34mTOOLS UPDATE COMPLETED
\033[0;31m════════════════════════════════════════════
\033[32;1m┌──────────────────────────────────────────┐
\033[32;1m│ [✓] AUTHOR   : 𝐌𝐃 𝐒𝐀𝐌𝐈𝐔𝐑 𝐑𝐀𝐇𝐌𝐀𝐍 𝐓𝐀𝐍𝐈𝐌    │
\033[33;1m│ [✓] GITHUB   : 𝐌𝐒𝐑𝐓𝐚𝐧𝐢𝐦                  │
\033[34;1m│ [✓] WHATSAPP : +𝟖𝟖𝟎𝟏𝟓𝟕𝟓𝟏𝟐𝟎𝟔𝟖𝟐            │
\033[35;1m│ [✓] VERSION  : 3.0                       │
\033[36;1m│ [✓] POWER BY : \033[1;32m𝐓𝐎𝐗𝐈𝐂 𝐂𝐘𝐁𝐄𝐑 SECURITY \033[1;37m     │
\033[37;1m└──────────────────────────────────────────┘        
\033[0;31m════════════════════════════════════════════""")

def menu():
    print("\33[34;1m [1] Install Packages")
    print("\33[34;1m [2] Completing  Story")
    print("\33[34;1m [3] Paragraph")
    print("\33[34;1m [4] Follow Owner")
    print("\33[34;1m [0] Exit the program \n")


menu()
option = int(input(" Enter the option: "))

while option != 0:
    if option == 1:
        print("Pacgakes Installing")
        # Basic Packages Addable...

    elif option == 2:
        def menu():
            print("\33[32;1m [1] Honesty is the best policy")
            print("\33[32;1m [2] Slow and steady wins the race")
            print("\33[32;1m [0] Exit")
        
        menu()
        option = int(input("Enter the Option: "))

        while option !=0:
            if option == 1:
                print("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.")

            elif option == 2:
                print("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.")

            else:
                print("Invalid Option Selected")

            menu()
            option = int(input("Enter your option: "))
        print("Thanks for using this program. Have a great time!...")
    elif option == 3:
        print("Updating Soon... \n")
    
    elif option == 4:
        os.system("xdg-open https://www.facebook.com/msrtanim.py ")

    menu()
    option = int(input("Enter your option: "))
print("Thanks for using this Program. Have a Great time!")
