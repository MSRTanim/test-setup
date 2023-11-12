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
option = int(input(" Enter the option: \33[1;97m"))

while option != 0:
    if option == 1:
        print("Pacgakes Installing")
        # Basic Packages Addable...

    elif option == 2:
        def menu():
            print("\33[32;1m [1] Honesty is the best policy")
            print("\33[32;1m [2] A friend in need is a friend indeed")
            print("\33[32;1m [0] Exit")
        
        menu()
        option = int(input(" Enter the Option: \33[1;97m"))

        while option !=0:
            if option == 1:
                print("\033[0;34m 𝗛𝗢𝗡𝗘𝗦𝗧𝗬 𝗜𝗦 𝗧𝗛𝗘 𝗕𝗘𝗦𝗧 𝗣𝗢𝗟𝗜𝗖𝗬 \n")
                print("\33[34;1m Once there lived a woodcutter in a village. One day he was cutting wood near a river in a forest. Suddenly his axe fell into the river. The river was very deep. The woodcutter also did not know how to swim or dive. So, he was sitting beside the river and cried loudly. Then a wonderful thing happened. A beautiful fairy appeared before the woodcutter. She asked the woodcutter in a sweet voice, “Why are you crying loudly? Why are you not cutting wood?” Then the woodcutter said her everything. After hearing everything, the fairy dive into the river and came with an axe which was made of gold. The fairy showed the axe and asked if it was his axe. The woodcutter replied in the negative. Then the fairy again dive into the river and came with the silver axe. In this time the woodcutter again replied in the negative and said that his axe was made of iron and a wooden handle. Then the fairy again dive into the river and came with his axe. After seeing the axe, the woodcutter became very happy and he thanked the fairy. After that the fairy gave him the axes which was made of gold and silver as a reward of his honesty. \n \n \n")

            elif option == 2:
                print("\033[0;34m 𝗔 𝗙𝗥𝗜𝗘𝗡𝗗 𝗜𝗡 𝗡𝗘𝗘𝗗 𝗜𝗦 𝗔 𝗙𝗥𝗜𝗘𝗡𝗗 𝗜𝗡𝗗𝗘𝗘𝗗 \n")
                print("\33[34;1m There were two close friends in a village. They promised that they would help each other at every time of danger. One day they were passing through a deep forest. Suddenly, a bear came in front of them. So, both of them were afraid. One of them knew how to climb up a tree. He climbed up a nearby tree. The other friend was fatty and did not know how to climb up a tree. He gave up the hope of his life. But suddenly an idea came to his mind. He knew that a bear does not touch a dead body. So, he fell flat on the ground like a dear body. He stopped breathing also. The bear came near him. It smells all over the body.  The bear thought him to be a dead man. So, it did not touch him. It went away slowly and gently. The friend who was on the tree saw everything. He got down from the free. He went to his friend and asked him eagerly, “Oh dear, what did the bear whisper into your ear?” In reply the friend said, “It advise me not to trust a false friend. It also said that don’t mix with those friends who leave you in time of danger. \n \n \n")


            else:
                print("Invalid Option Selected")

            menu()
            option = int(input("Enter your option: "))
        print("Thanks for using this program. Have a great time!...")
    elif option == 3:
        print("Updating Soon... \n")
    
    elif option == 4:
        os.system("xdg-open https://www.facebook.com/msrtanim.py ")

    else:
        print("Invalid Option Selected \n")
        print("Please Select Correct Option")

    menu()
    option = int(input("Enter your option: "))
print("Thanks for using this Program. Have a Great time!")
