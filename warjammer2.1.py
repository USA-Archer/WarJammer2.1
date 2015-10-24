# WarJammer Ver2.1 Copyright 2015 USA~Archer
# This program spams PvPGN players with unsquelchable messages
# Email: archer@usa-archer.com

# USED FOR SLEEP
import time

# USED FOR TCP IP COMMUNICATION
import socket

# USED FOR EXTERNAL IP CHECK
import urllib
import json

# USED FOR RANDOM CLAN TAG GENERATOR
import string
import random

# RANDOM TAG GENERATOR FUNCTION
def RANDOM_CLAN_TAG(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

# USED TO FETCH EXTERNAL IP ADDRESS
try:
    EXT_IP = json.loads(urllib.urlopen("https://api.ipify.org?format=json").read())

except:
    try:
        EXT_IP = json.loads(urllib.urlopen("http://ip.jsontest.com/").read())
    except:
        pass
    pass




# BANNER
print ("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print ''' _    _  ___  ______   ___  ___  ___  ______  ___ ___________
| |  | |/ _ \ | ___ \ |_  |/ _ \ |  \/  ||  \/  ||  ___| ___ \\
| |  | / /_\ \| |_/ /   | / /_\ \| .  . || .  . || |__ | |_/ /
| |/\| |  _  ||    /    | |  _  || |\/| || |\/| ||  __||    / 
\  /\  / | | || |\ \/\__/ / | | || |  | || |  | || |___| |\ \ 
 \/  \/\_| |_/\_| \_\____/\_| |_/\_|  |_/\_|  |_/\____/\_| \_|
THE UNSQUELCHABLE PvPGN SPAMMER.          Ver2.1 by USA~Archer         '''
print ("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n") 
print "http://USA-Archer.com/\n"
print "# WarJanmmer Ver2.1 by USA~Archer"
print "# Email: archer@usa-archer.com"
print "# This program spams PvPGN players with unsquelchable messages\n"
print "DISCLAIMER: Please do not use in military or secret service organizations or"
print "for illegal purposes.\n"

# TRY TO GET EXT_IP, IF FAIL PRINT AS UNKOWN
try:
    print "Current External IP Address: %s\n\n" % EXT_IP["ip"]
except:
    print "Current External IP Address: Unknown\n\n" 
    
# USER SUPPLIED VARIABLES
print "SPAMBOT LOGIN INFO\n"

# GET USERNAME OF SPAMBOT
while True:

    BOT_USERNAME = (raw_input("Username: "))
    if BOT_USERNAME == '':
        print "\n[!] ERROR: Please enter a valid username.\n"
        continue

    break
# GET PASSWORD OF SPAMBOT
while True:

    BOT_PASSWORD = (raw_input("Password: "))
    if BOT_PASSWORD == '':
        print "\n[!] ERROR: Please enter a valid password.\n"
        continue

    break
# GET SERVER
while True:

    SERVER = (raw_input("PvPGN Server Name or IP: "))
    if SERVER == '':
        print "\n[!] ERROR: Please enter a valid server name.\n"
        continue

    break

print "\nATTACK INFO\n"
# GET USERNAME TO ATTACK
while True:

    ATTACK_USERNAME = (raw_input("Username to attack: "))
    if ATTACK_USERNAME == '':
        print "\n[!] ERROR: Please enter a valid username.\n"
        continue

    break
# ATTACK WITH /f a /f r OR CLAN INVITE
print '''
[1] Friend List Attack
[2] Clan Invite Attack
'''
while True:
    try:
        ATTACK_COMMAND = (raw_input("Attack Mode: "))
        if ATTACK_COMMAND == '':
            print "\n[!] ERROR: Please enter a valid selection.\n"
            continue
    except:
        print "\n[!] ERROR: Please enter a valid selection.\n"
        continue

    break
# ATTACK UNTIL OFFLINE OR X NUMBER OF TIMES?
print '''
[1] Attack until offline
[2] Attack x number of times
'''
while True:
    try:
        ATTACK_TYPE = (raw_input("Duration Mode: "))
        if ATTACK_TYPE == '':
            print "\n[!] ERROR: Please enter a valid selection.\n"
            continue
    except:
        print "\n[!] ERROR: Please enter a valid selection.\n"
        continue

    break
while True:
    try:
        SLEEP_NUMBER = int((raw_input("Number of seconds between commands: ")))
        if SLEEP_NUMBER == '':
            print "\n[!] ERROR: Please enter a valid selection.\n"
            continue
    except:
        print "\n[!] ERROR: Please enter a valid selection.\n"
        continue

    break
    
    
# HARD CODED VARIABLES
BUFFER_SIZE = 2048
PORT = 6112

####################################
# FRIEND LIST ATTACK UNTIL OFFLINE #
####################################


if ATTACK_COMMAND == '1' and ATTACK_TYPE == '1':
    ATTACK_NUMBER = 0
    print '''\nWarJammer: FRIEND LIST ATTACKING '%s' UNTIL OFFLINE\n''' % ATTACK_USERNAME
    while True:
        # TRY TO LOG IN
        try:
            # DEFINE SOCKET AS TCP IP
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # CONNECT TO SERVER
            s.connect((SERVER, 6112))
            # LOG IN: HIT ENTER TO INTERACT WITH THE TERMINAL
            s.send("\r\n")
            # TYPE USERNAME
            s.send(BOT_USERNAME)
            # HIT ENTER TO SEND USERNAME
            s.send("\r\n")
            # TYPE PASSWORD
            s.send(BOT_PASSWORD)
            # HIT ENTER TO SEND PASSWORD
            s.send("\r\n")
            # RECIEVE DATA BACK
            data = s.recv(BUFFER_SIZE)
            data = s.recv(BUFFER_SIZE)

            # IF SERVER SAYS LOGIN FAILED
            if "failed" in data:
                s.close()
                print "\n[!] ERROR: Username/password incorrect. Try again.\n"

                # GET USERNAME AGAIN
                while True:

                    BOT_USERNAME = (raw_input("Username: "))
                    if BOT_USERNAME == '':
                        print "\n[!] ERROR: Please enter a valid username.\n"
                        continue

                    break

                # GET PASSWORD AGAIN
                while True:

                    BOT_PASSWORD = (raw_input("Password: "))
                    if BOT_PASSWORD == '':
                        print "\n[!] ERROR: Please enter a valid password.\n"
                        continue

                    break
                continue
            
            elif "no bot" in data:
                print "\n[!] ERROR: Server says 'Account has no bot access'\n"
                raw_input("\n\nPress Enter to Continue ...")
                continue
            

            # IF NO ERROR OCCURRED, EXIT THE 'while True' LOOP
            break

        # IF ERROR OCCURED EITHER WHILE CONNECTING OR RECEVING DATA BACK, DO THIS
        except:

            # PRINT ERROR MESSAGE
            print "\n[!] ERROR: Could not connect to server: %s \nCheck if the server name above is correct and online and try again.\n" % SERVER
            # TRY TO GET EXT_IP, IF FAIL PRINT AS UNKOWN

            # GET SERVER AGAIN
            while True:

                SERVER = (raw_input("PvPGN Server Name or IP: "))
                if SERVER == '':
                    print "\n[!] ERROR: Please enter a valid server name.\n"
                    continue

                break
	
    # ADVERTISE
    s.send("/m %s .:Starting WarJammer Ver2.0 by USA~Archer:. Download at http://USA-Archer.com" % ATTACK_USERNAME)
    # HIT ENTER TO SEND
    s.send("\r\n")
    time.sleep(SLEEP_NUMBER)
	
    while True:
        # TYPE /whois TO CHECK IF USER ONLINE OR EXISTS
        s.send("/whois %s" % ATTACK_USERNAME)
        # HIT ENTER TO SEND
        s.send("\r\n")
        data0 = s.recv(2048)
        # SLEEP TO EVADE FLOOD DISC
        time.sleep(SLEEP_NUMBER)
        
        # TYPE /f a
        s.send("/f a %s" % ATTACK_USERNAME)
        # HIT ENTER TO SEND
        s.send("\r\n")
        data1 = s.recv(2048)
        # SLEEP TO EVADE FLOOD DISCONNECT
        time.sleep(SLEEP_NUMBER)

        # TYPE /f r
        s.send("/f r %s" % ATTACK_USERNAME)
        # HIT ENTER TO SEND
        s.send("\r\n")
        data2 = s.recv(2048)
        # SLEEP FOR x SECONDS TO AVOID FLOOD DISCONNECT
        time.sleep(SLEEP_NUMBER)
        ATTACK_NUMBER = ATTACK_NUMBER + 1
        
        # THESE '<from' and '>' elif STATEMENTS PROTECT AGAINST BAD DATA BEING
        # READ - FOR EXAMPLE, PREVIOUSLY A USER COULD WHISPER OR SAY IN CHAT
        # 'OFFLINE' AND WarJammer WOULD THINK THAT CAME FROM THE SERVER
        # AND QUIT. NOW IT IGNORES ALL DATA FROM USERS AND CONTINUES LOOP
        # THIS ALSO LETS YOU SEE WHAT IS BEING SAID BACK TO THE BOT ;)
        
        if "<from" in data1:
            print "\nWarJammer: RECEIVED MSG WHISPERED TO BOT\n"
            print data1
            continue

        elif "<from" in data2:
            print "\nWarJammer: RECEIVED MSG WHISPERED TO BOT\n"
            print data2
            continue

        elif "<from" in data1 and data2:
            print "\nWarJammer: RECEIVED MSG WHISPERED TO BOT\n"
            print data1
            print data2
            continue

        elif ">" in data1:
            print "\nWarJammer: RECEIVED MSG IN CHAT CHANNEL\n"
            print data1
            continue

        elif ">" in data2:
            print "\nWarJammer: RECEIVED MSG IN CHAT CHANNEL\n"
            print data2
            continue

        elif ">" in data1 and data2:
            print "\nWarJammer: RECEIVED MSG IN CHAT CHANNEL\n"
            print data1
            print data2
            continue

        elif "ERROR: Your message quota has been exceeded!" in data2:
            s.close()
            print "\n[!] ERROR: You've been disconnected by the server for flooding."
            print "Try again with a higher number of seconds between attacks"
            raw_input("\n\nPress Enter to exit ...")
            break

        elif "offline" in data1:
            print '''\nWarJammer: TANGO DOWN. User signed off\n'''
            s.close()
            raw_input("\n\nPress Enter to exit ...")
            break

        elif "Unknown" in data1:
            print '''\n[!] ERROR: Cannot attack user - user does not exist.\n'''
            s.close()
            raw_input("\n\nPress Enter to exit ...")
            break

        # THIS IS WHAT WE WANT
        elif "Added" in data2:
            print "STATUS No. %s SUCCESS! Sent %s: '%s added you to his/her friends list.'\n" % (ATTACK_NUMBER, ATTACK_USERNAME, BOT_USERNAME)
            continue
            
        else:
            print "[!] ERROR: Did not receive a valid response.\nTry increasing number of seconds between commands."
            s.close()
            raw_input("\n\nPress Enter to exit ...")
            break



########################################
# FRIEND LIST ATTACK X NUMBER OF TIMES #
########################################


if ATTACK_COMMAND == '1' and ATTACK_TYPE == '2':
    ATTACK_NUMBER_INITIAL = 0
    
    while True:
        try:
            # GET NUMBER OF ATTACKS
            ATTACK_NUMBER = (raw_input("Number of attacks: "))
            ATTACK_NUMBER = int(ATTACK_NUMBER)
            if ATTACK_NUMBER == '':
                print "\n[!] ERROR: Please enter a valid selection.\n"
                continue
        except:
            print "\n[!] ERROR: Please enter a number.\n"
            continue
        
        break
    ATTACK_NUMBER_INITIAL = ATTACK_NUMBER

    print '''\nWarJammer: FRIEND LIST ATTACKING '%s' %s TIMES\n''' % (ATTACK_USERNAME, ATTACK_NUMBER_INITIAL)
    while True:
        # TRY TO LOG IN
        try:
            # DEFINE SOCKET AS TCP IP
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # CONNECT TO SERVER
            s.connect((SERVER, 6112))
            # LOG IN: HIT ENTER TO INTERACT WITH THE TERMINAL
            s.send("\r\n")
            # TYPE USERNAME
            s.send(BOT_USERNAME)
            # HIT ENTER TO SEND USERNAME
            s.send("\r\n")
            # TYPE PASSWORD
            s.send(BOT_PASSWORD)
            # HIT ENTER TO SEND PASSWORD
            s.send("\r\n")
            # RECIEVE DATA BACK
            data = s.recv(BUFFER_SIZE)
            data = s.recv(BUFFER_SIZE)

            # IF SERVER SAYS LOGIN FAILED
            if "failed" in data:
                s.close()
                print "\n[!] ERROR: Username/password incorrect. Try again.\n"

                # GET USERNAME AGAIN
                while True:

                    BOT_USERNAME = (raw_input("Username: "))
                    if BOT_USERNAME == '':
                        print "\n[!] ERROR: Please enter a valid username.\n"
                        continue

                    break

                # GET PASSWORD AGAIN
                while True:

                    BOT_PASSWORD = (raw_input("Password: "))
                    if BOT_PASSWORD == '':
                        print "\n[!] ERROR: Please enter a valid password.\n"
                        continue

                    break
                continue
            # THIS CHECKS THE 'AUTH_BOT_LOGIN' PvPGN BNET DATABASE SETTING
            elif "no bot" in data:
                print "\n[!] ERROR: Server says 'Account has no bot access'\n"
                raw_input("\n\nPress Enter to Continue ...")
                continue

        # IF ERROR OCCURED EITHER WHILE CONNECTING OR RECEVING DATA BACK, DO THIS
        except:

            # PRINT ERROR MESSAGE
            s.close()
            print "\n[!] ERROR: Could not connect to server: %s \nCheck if the server name above is correct and online and try again.\n" % SERVER
            # TRY TO GET EXT_IP, IF FAIL PRINT AS UNKOWN

            # GET SERVER AGAIN
            while True:

                SERVER = (raw_input("PvPGN Server Name or IP: "))
                if SERVER == '':
                    print "\n[!] ERROR: Please enter a valid server name.\n"
                    continue

                break
		
        # ADVERTISE
        s.send("/m %s .:Starting WarJammer Ver2.0 by USA~Archer:. Download at http://USA-Archer.com" % ATTACK_USERNAME)
        # HIT ENTER TO SEND
        s.send("\r\n")
        time.sleep(SLEEP_NUMBER)

        while ATTACK_NUMBER > 0:
            # TYPE /whois
            s.send("/whois %s" % ATTACK_USERNAME)
            # HIT ENTER TO SEND
            s.send("\r\n")
            data0 = s.recv(BUFFER_SIZE)

            # SLEEP TO EVADE FLOOD DISC
            time.sleep(SLEEP_NUMBER)

            # TYPE /f a
            s.send("/f a %s" % ATTACK_USERNAME)
            # HIT ENTER TO SEND
            s.send("\r\n")
            data1 = s.recv(BUFFER_SIZE)

            # SLEEP TO EVADE FLOOD DISCONNECT
            time.sleep(SLEEP_NUMBER)

            # TYPE /f r
            s.send("/f r %s" % ATTACK_USERNAME)
            # HIT ENTER TO SEND
            s.send("\r\n")
            data2 = s.recv(BUFFER_SIZE)

            # SLEEP FOR x SECONDS TO AVOID FLOOD DISCONNECT
            time.sleep(SLEEP_NUMBER)

            # THESE '<from' and '>' elif STATEMENTS PROTECT AGAINST BAD DATA BEING
            # READ - FOR EXAMPLE, PREVIOUSLY A USER COULD WHISPER OR SAY IN CHAT
            # 'OFFLINE' AND WarJammer WOULD THINK THAT CAME FROM THE SERVER
            # AND QUIT. THIS ALSO LETS YOU SEE WHAT IS BEING SAID BACK TO THE BOT ;)

            if "<from" in data1:
                print "\nWarJammer: RECEIVED MSG WHISPERED TO BOT\n"
                print data1
                continue

            elif "<from" in data2:
                print "\nWarJammer: RECEIVED MSG WHISPERED TO BOT\n"
                print data2
                continue

            elif "<from" in data1 and data2:
                print "\nWarJammer: RECEIVED MSG WHISPERED TO BOT\n"
                print data1
                print data2
                continue

            elif ">" in data1:
                print "\nWarJammer: RECEIVED MSG IN CHAT CHANNEL\n"
                print data1
                continue

            elif ">" in data2:
                print "\nWarJammer: RECEIVED MSG IN CHAT CHANNEL\n"
                print data2
                continue

            elif ">" in data1 and data2:
                print "\nWarJammer: RECEIVED MSG IN CHAT CHANNEL\n"
                print data1
                print data2
                continue

            elif "ERROR: Your message quota has been exceeded!" in data2:
                s.close()
                print "\n[!] ERROR: You've been disconnected by the server for flooding."
                print "Try again with a higher number of seconds between attacks"
                raw_input("\n\nPress Enter to exit ...")
                break

            elif "offline" in data1:
                print '''\nWarJammer: TANGO DOWN. User signed off.\n'''
                s.close()
                raw_input("\n\nPress Enter to exit ...")
                break

            elif "Unkown" in data1:
                print '''\n[!] ERROR: Cannot attack user - user does not exist.\n'''
                s.close()
                raw_input("\n\nPress Enter to exit ...")
                break

            # THIS IS WHAT WE WANT
            elif "Added" in data2:
                ATTACK_NUMBER = ATTACK_NUMBER - 1
                CURRENT_ATTACK_NUMBER = ATTACK_NUMBER_INITIAL - ATTACK_NUMBER
                print "STATUS (%s/%s) SUCCESS! Sent %s: '%s added you to his/her friends list.'\n" % (CURRENT_ATTACK_NUMBER, ATTACK_NUMBER_INITIAL, ATTACK_USERNAME, BOT_USERNAME)
                continue
                
            else:
                print "[!] ERROR: Did not receive a valid response.\nTry increasing number of seconds between commands."
                s.close()
                raw_input("\n\nPress Enter to exit ...")
                break
                
        s.close()
        
        print "\nDone!"
        raw_input("\n\nPress Enter to exit ...")
        break
        
        
####################################
# CLAN INVITE ATTACK UNTIL OFFLINE #
####################################


if ATTACK_COMMAND == '2' and ATTACK_TYPE == '1':
    
    # GENERATE RANDOM CLAN TAG
    CLAN_TAG = RANDOM_CLAN_TAG()
    
    # GET CLAN NAME, IF OVER 23 CHARS PvPGN WILL AUTO TRUNCATE
    while True:
        try:
           CLAN_NAME = (raw_input("Clan Name [Max 23 chars]: "))
           if CLAN_NAME == '':
               print "\n[!] ERROR: Please enter a valid selection.\n"
               continue
        except:
           print "\n[!] ERROR: Please enter a name.\n"
           continue
        break
    
    ATTACK_NUMBER = 0
    
    print '''\nWarJammer: CLAN INVITE ATTACKING '%s' UNTIL OFFLINE\n''' % ATTACK_USERNAME
    while True:
        # TRY TO LOG IN
        try:
            # DEFINE SOCKET AS TCP IP
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # CONNECT TO SERVER
            s.connect((SERVER, 6112))
            # LOG IN: HIT ENTER TO INTERACT WITH THE TERMINAL
            s.send("\r\n")
            # TYPE USERNAME
            s.send(BOT_USERNAME)
            # HIT ENTER TO SEND USERNAME
            s.send("\r\n")
            # TYPE PASSWORD
            s.send(BOT_PASSWORD)
            # HIT ENTER TO SEND PASSWORD
            s.send("\r\n")
            # RECIEVE DATA BACK
            data = s.recv(BUFFER_SIZE)
            data = s.recv(BUFFER_SIZE)
      

            # IF SERVER SAYS LOGIN FAILED
            if "failed" in data:
                s.close()
                print "\n[!] ERROR: Username/password incorrect. Try again.\n"

                # GET USERNAME AGAIN
                while True:

                    BOT_USERNAME = (raw_input("Username: "))
                    if BOT_USERNAME == '':
                        print "\n[!] ERROR: Please enter a valid username.\n"
                        continue

                    break

                # GET PASSWORD AGAIN
                while True:

                    BOT_PASSWORD = (raw_input("Password: "))
                    if BOT_PASSWORD == '':
                        print "\n[!] ERROR: Please enter a valid password.\n"
                        continue

                    break
                continue
            
            elif "no bot" in data:
                print "\n[!] ERROR: Server says 'Account has no bot access'\n"
                raw_input("\n\nPress Enter to Continue ...")
                continue
            

            # IF NO ERROR OCCURRED, EXIT THE 'while True' LOOP
            break

        # IF ERROR OCCURED EITHER WHILE CONNECTING OR RECEVING DATA BACK, DO THIS
        except:

            # PRINT ERROR MESSAGE
            print "\n[!] ERROR: Could not connect to server: %s \nCheck if the server name above is correct and online and try again.\n" % SERVER
            # TRY TO GET EXT_IP, IF FAIL PRINT AS UNKOWN

            # GET SERVER AGAIN
            while True:

                SERVER = (raw_input("PvPGN Server Name or IP: "))
                if SERVER == '':
                    print "\n[!] ERROR: Please enter a valid server name.\n"
                    continue

                break
                
	
    # ADVERTISE
    s.send("/m %s .:Starting WarJammer Ver2.0 by USA~Archer:. Download at http://USA-Archer" % ATTACK_USERNAME)
    # HIT ENTER TO SEND
    s.send("\r\n")
    time.sleep(SLEEP_NUMBER)
    
    while True:

        # TYPE COMMAND TO DISBAND ANY PREVIOUS CLAN
        s.send("/clan disband yes")
        # HIT ENTER TO SEND
        s.send("\r\n")
        data0 = s.recv(BUFFER_SIZE)
        
        # SLEEP TO AVOID FLOOD DISCONNECT
        time.sleep(SLEEP_NUMBER)
        
        # TYPE COMMAND TO CREATE CLAN
        s.send("/clan create %s %s" % (CLAN_TAG, CLAN_NAME))
        # HIT ENTER TO SEND
        s.send("\r\n")
        data1 = s.recv(BUFFER_SIZE)
        
        # SLEEP TO AVOID FLOOD DISCONNECT
        time.sleep(SLEEP_NUMBER)


 
        # TYPE COMMAND TO INVITE
        s.send("/clan invite %s" % ATTACK_USERNAME)
        # HIT ENTER TO SEND
        s.send("\r\n")
        data2 = s.recv(BUFFER_SIZE)
        

        # THESE '<from' and '>' elif STATEMENTS PROTECT AGAINST BAD DATA BEING
        # READ - FOR EXAMPLE, PREVIOUSLY A USER COULD WHISPER OR SAY IN CHAT
        # 'OFFLINE' AND WarJammer WOULD THINK THAT CAME FROM THE SERVER
        # AND QUIT. THIS ALSO LETS YOU SEE WHAT IS BEING SAID BACK TO THE BOT ;)
        
        if "<from" in data0:
            print "\nWarJammer: RECEIVED MSG WHISPERED TO BOT\n"
            print data0
            continue

        elif "<from" in data1:
            print "\nWarJammer: RECEIVED MSG WHISPERED TO BOT\n"
            print data1
            continue

        elif "<from" in data0 and data1:
            print "\nWarJammer: RECEIVED MSG WHISPERED TO BOT\n"
            print data0
            print data1
            continue
        
        # THIS IS JUST FOR THE FIRST LOOP, THERE IS NO ERROR CHECKING BUT
        # AT LEAST IT DOESNT CATCH THE ADVERTISEMENT AS A WHISPER. IT
        # WILL CHECK FOR ERRORS NEXT TIME.             
        if "<to" in data0:
            # SLEEP TO AVOID FLOOD DISCONNECT
            time.sleep(SLEEP_NUMBER) 

            ATTACK_NUMBER = ATTACK_NUMBER + 1
            print "STATUS No. %s SUCCESS! Sent %s: 'You are invited to %s by %s'\n" % (ATTACK_NUMBER, ATTACK_USERNAME, CLAN_NAME, BOT_USERNAME)
            continue
            continue

        elif ">" in data0:
            print "\nWarJammer: RECEIVED MSG IN CHAT CHANNEL\n"
            print data0
            continue

        elif ">" in data1:
            print "\nWarJammer: RECEIVED MSG IN CHAT CHANNEL\n"
            print data1
            continue

        elif ">" in data0 and data1:
            print "\nWarJammer: RECEIVED MSG IN CHAT CHANNEL\n"
            print data0
            print data1
            continue

        elif "ERROR: Your message quota has been exceeded!" in data0:
            s.close()
            print "\n[!] ERROR: You've been disconnected by the server for flooding."
            print "Try again with a higher number of seconds between attacks"
            raw_input("\n\nPress Enter to exit ...")
            break

        elif "not online" in data0:
            print '''\nWarJammer: TANGO DOWN. User signed off [or already in a clan]\n'''
            # AFTER FINISHING THE LOOP, WE WANT TO DISBAND THE CLAN SO IT CAN BE USED AGAIN BY ANOTHER USERNAME
            # TYPE COMMAND TO DISBAND ANY PREVIOUS CLAN
            s.send("/clan disband yes")
            # HIT ENTER TO SEND
            s.send("\r\n")
            # CLOSE SOCKET
            s.close()
            raw_input("\n\nPress Enter to exit ...")
            break
        
        # CHECK IF CLAN CREATE IS SUPPORTED

        elif "You are not in a clan!" in data0:
            print "[!] ERROR: Unable to create clan. Not supported on this server"
            s.close()
            raw_input("\n\nPress Enter to exit ...")
            break

        elif "Please choice another one." in data0:
            print "[!] ERROR: Clan already exists."
            s.close()
            raw_input("\n\nPress Enter to exit ...")
            break
        
        # THIS IS WHAT WE WANT TO HAPPEN ->
        elif "was invited to your clan" in data0:
            
            # SLEEP TO AVOID FLOOD DISCONNECT
            time.sleep(SLEEP_NUMBER) 

            ATTACK_NUMBER = ATTACK_NUMBER + 1
            print "STATUS No. %s SUCCESS! Sent %s: 'You are invited to %s by %s'\n" % (ATTACK_NUMBER, ATTACK_USERNAME, CLAN_NAME, BOT_USERNAME)
            continue
        
        else:
            print "[!] ERROR: Did not receive a valid response.\nTry increasing number of seconds between commands."
            s.close()
            raw_input("\n\nPress Enter to exit ...")
            break
        
    # AFTER FINISHING THE LOOP, WE WANT TO DISBAND THE CLAN SO IT CAN BE USED AGAIN BY ANOTHER USERNAME
    # TYPE COMMAND TO DISBAND ANY PREVIOUS CLAN
    s.send("/clan disband yes")
    # HIT ENTER TO SEND
    s.send("\r\n")
    s.close()

    print "\nDone!"
    raw_input("\n\nPress Enter to exit ...")
    
    

########################################          
# CLAN INVITE ATTACK X NUMBER OF TIMES #
########################################


if ATTACK_COMMAND == '2' and ATTACK_TYPE == '2':
    ATTACK_NUMBER_INITIAL = 0
    
    while True:
        try:
            
            ATTACK_NUMBER = (raw_input("Number of attacks: "))
            ATTACK_NUMBER = int(ATTACK_NUMBER)
            if ATTACK_NUMBER == '':
                print "\n[!] ERROR: Please enter a valid selection.\n"
                continue
        except:
            print "\n[!] ERROR: Please enter a number.\n"
            continue
        
        break
        
    CLAN_TAG = RANDOM_CLAN_TAG()
    
    while True:
       try:
           CLAN_NAME = (raw_input("Clan Name [Max 23 chars]: "))
           if CLAN_NAME == '':
               print "\n[!] ERROR: Please enter a valid selection.\n"
               continue
       except:
           print "\n[!] ERROR: Please enter a tag.\n"
           continue

       break
    ATTACK_NUMBER_INITIAL = ATTACK_NUMBER

    print '''\nWarJammer: CLAN INVITE ATTACKING '%s' %s TIMES\n''' % (ATTACK_USERNAME, ATTACK_NUMBER_INITIAL)
    while True:
        # TRY TO LOG IN
        try:
            # DEFINE SOCKET AS TCP IP
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # CONNECT TO SERVER
            s.connect((SERVER, 6112))
            # LOG IN: HIT ENTER TO INTERACT WITH THE TERMINAL
            s.send("\r\n")
            # TYPE USERNAME
            s.send(BOT_USERNAME)
            # HIT ENTER TO SEND USERNAME
            s.send("\r\n")
            # TYPE PASSWORD
            s.send(BOT_PASSWORD)
            # HIT ENTER TO SEND PASSWORD
            s.send("\r\n")
            # RECIEVE DATA BACK
            data = s.recv(2048)
            data = s.recv(2048)
     
         

            # IF SERVER SAYS LOGIN FAILED
            if "failed" in data:
                s.close()
                print "\n[!] ERROR: Username/password incorrect. Try again.\n"

                # GET USERNAME AGAIN
                while True:

                    BOT_USERNAME = (raw_input("Username: "))
                    if BOT_USERNAME == '':
                        print "\n[!] ERROR: Please enter a valid username.\n"
                        continue

                    break

                # GET PASSWORD AGAIN
                while True:

                    BOT_PASSWORD = (raw_input("Password: "))
                    if BOT_PASSWORD == '':
                        print "\n[!] ERROR: Please enter a valid password.\n"
                        continue

                    continue
            
            
            elif "no bot" in data:
                print "\n[!] ERROR: Server says 'Account has no bot access'\n"
                raw_input("\n\nPress Enter to Continue ...")
                continue

        # IF ERROR OCCURED EITHER WHILE CONNECTING OR RECEVING DATA BACK, DO THIS
        except:

            # PRINT ERROR MESSAGE
            s.close()
            print "\n[!] ERROR: Could not connect to server: %s \nCheck if the server name above is correct and online and try again.\n" % SERVER
            # TRY TO GET EXT_IP, IF FAIL PRINT AS UNKOWN

            # GET SERVER AGAIN
            while True:

                SERVER = (raw_input("PvPGN Server Name or IP: "))
                if SERVER == '':
                    print "\n[!] ERROR: Please enter a valid server name.\n"
                    continue

                break
		
        # ADVERTISE
	s.send("/m %s .:Starting WarJammer Ver2.0 by USA~Archer:. Download at http://USA-Archer.com" % ATTACK_USERNAME)
        # HIT ENTER TO SEND
        s.send("\r\n")
        time.sleep(SLEEP_NUMBER)

        while ATTACK_NUMBER > 0:

            # TYPE COMMAND TO DISBAND ANY PREVIOUS CLAN
            s.send("/clan disband yes")
            # HIT ENTER TO SEND
            s.send("\r\n")
            data0 = s.recv(BUFFER_SIZE)

            # SLEEP TO AVOID FLOOD DISCONNECT
            time.sleep(SLEEP_NUMBER)

            # TYPE COMMAND TO CREATE CLAN
            s.send("/clan create %s %s" % (CLAN_TAG, CLAN_NAME))
            # HIT ENTER TO SEND
            s.send("\r\n")
            data1 = s.recv(BUFFER_SIZE)
            
            # SLEEP TO AVOID FLOOD DISCONNECT
            time.sleep(SLEEP_NUMBER)



            # TYPE COMMAND TO INVITE
            s.send("/clan invite %s" % ATTACK_USERNAME)
            # HIT ENTER TO SEND
            s.send("\r\n")
            data2 = s.recv(BUFFER_SIZE)
            
            # THESE '<from' and '>' elif STATEMENTS PROTECT AGAINST BAD DATA BEING
            # READ - FOR EXAMPLE, PREVIOUSLY A USER COULD WHISPER OR SAY IN CHAT
            # 'OFFLINE' AND WarJammer WOULD THINK THAT CAME FROM THE SERVER
            # AND QUIT. THIS ALSO LETS YOU SEE WHAT IS BEING SAID BACK TO THE BOT ;)

            if "<from" in data0:
                print "\nWarJammer: RECEIVED MSG WHISPERED TO BOT\n"
                print data0
                continue

            elif "<from" in data1:
                print "\nWarJammer: RECEIVED MSG WHISPERED TO BOT\n"
                print data1
                continue

            elif "<from" in data0 and data1:
                print "\nWarJammer: RECEIVED MSG WHISPERED TO BOT\n"
                print data0
                print data1
                continue
            
            # THIS IS JUST FOR THE FIRST LOOP, THERE IS NO ERROR CHECKING BUT
            # AT LEAST IT DOESNT CATCH THE ADVERTISEMENT AS A WHISPER. IT
            # WILL CHECK FOR ERRORS NEXT TIME.
            if "<to" in data0:
                # SLEEP TO AVOID FLOOD DISCONNECT
                time.sleep(SLEEP_NUMBER) 
                ATTACK_NUMBER = ATTACK_NUMBER - 1
                CURRENT_ATTACK_NUMBER = ATTACK_NUMBER_INITIAL - ATTACK_NUMBER
                print "STATUS (%s/%s) SUCCESS! Sent %s: 'You are invited to %s by %s'\n" % (CURRENT_ATTACK_NUMBER, ATTACK_NUMBER_INITIAL, ATTACK_USERNAME, CLAN_NAME, BOT_USERNAME)
                continue
                
            elif ">" in data0:
                print "\nWarJammer: RECEIVED MSG IN CHAT CHANNEL\n"
                print data0
                continue

            elif ">" in data1:
                print "\nWarJammer: RECEIVED MSG IN CHAT CHANNEL\n"
                print data1
                continue

            elif ">" in data0 and data1:
                print "\nWarJammer: RECEIVED MSG IN CHAT CHANNEL\n"
                print data0
                print data1
                continue

            elif "ERROR: Your message quota has been exceeded!" in data0:
                s.close()
                print "\n[!] ERROR: You've been disconnected by the server for flooding."
                print "Try again with a higher number of seconds between attacks"
                raw_input("\n\nPress Enter to exit ...")
                break

            elif "not online" in data0:
                print '''\nWarJammer: TANGO DOWN. User signed off [or already in a clan]\n'''
                # AFTER FINISHING THE LOOP, WE WANT TO DISBAND THE CLAN SO IT CAN BE USED AGAIN BY ANOTHER USERNAME
                # TYPE COMMAND TO DISBAND ANY PREVIOUS CLAN
                s.send("/clan disband yes")
                # HIT ENTER TO SEND
                s.send("\r\n")
                # CLOSE SOCKET
                s.close()
                raw_input("\n\nPress Enter to exit ...")
                break

            # CHECK IF CLAN CREATE IS SUPPORTED

            elif "You are not in a clan!" in data0:
                print "[!] ERROR: Unable to create clan. Not supported on this server"
                s.close()
                raw_input("\n\nPress Enter to exit ...")
                break

            elif "Please choice another one." in data0:
                print "[!] ERROR: Clan already exists."
                s.close()
                raw_input("\n\nPress Enter to exit ...")
                break

            elif "was invited to your clan" in data0:
                # SLEEP TO AVOID FLOOD DISCONNECT
                time.sleep(SLEEP_NUMBER) 
                ATTACK_NUMBER = ATTACK_NUMBER - 1
                CURRENT_ATTACK_NUMBER = ATTACK_NUMBER_INITIAL - ATTACK_NUMBER
                print "STATUS (%s/%s) SUCCESS! Sent %s: 'You are invited to %s by %s'\n" % (CURRENT_ATTACK_NUMBER, ATTACK_NUMBER_INITIAL, ATTACK_USERNAME, CLAN_NAME, BOT_USERNAME)
                continue

            else:
                print "[!] ERROR: Did not receive a valid response.\nTry increasing number of seconds between commands."
                s.close()
                raw_input("\n\nPress Enter to exit ...")
                break

        # AFTER FINISHING THE LOOP, WE WANT TO DISBAND THE CLAN SO IT CAN BE USED AGAIN BY ANOTHER USERNAME
        # TYPE COMMAND TO DISBAND ANY PREVIOUS CLAN
        s.send("/clan disband yes")
        # HIT ENTER TO SEND
        s.send("\r\n")
        s.close()
        
        print "\nDone!"
        raw_input("\n\nPress Enter to exit ...")
        break