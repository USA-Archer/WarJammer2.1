$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
 _    _  ___  ______   ___  ___  ___  ______  ___ ___________
| |  | |/ _ \ | ___ \ |_  |/ _ \ |  \/  ||  \/  ||  ___| ___ \
| |  | / /_\ \| |_/ /   | / /_\ \| .  . || .  . || |__ | |_/ /
| |/\| |  _  ||    /    | |  _  || |\/| || |\/| ||  __||    / 
\  /\  / | | || |\ \/\__/ / | | || |  | || |  | || |___| |\ \ 
 \/  \/\_| |_/\_| \_\____/\_| |_/\_|  |_/\_|  |_/\____/\_| \_|
THE UNSQUELCHABLE PvPGN SPAMMER.          Ver2.1 by USA~Archer
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

http://USA-Archer.com/

# WarJammer Ver2.1 by USA~Archer
# Email: archer@usa-archer.com
# This program spams PvPGN players with unsquelchable messages


DISCLAIMER: Please do not use in military or secret service organizations or
for illegal purposes.


DESCRIPTION:
- WarJammer has 2 attack modes: Friend List Attack, and Clan Invite Attack
- Both can be used to flood a PvPGN user's screen with messages sent by
- the PvPGN server. These messages CANNOT be silenced by '/ignore' or
- '/squelch' commands. 
- Message sent by Friend List Attack:
- '<SPAMBOT_USERNAME> added you to his/her friends list.'This is just a spammer, not a DDoS tool.
- Message sent by Clan Invite Attack:
- 'You are invited to <CLAN_NAME> by <SPAMBOT_USERNAME>'
- Each attack mode has 2 Duration Modes: 'Attack Until Offline' or 'Attack X Number of Times'

TIPS:
- 1. Clan Invite Attacks only work on PvPGN 1.99 and later. WarJammer will let you know if it
- is supported on your server.
- 2. Friend List Attacks are faster than Clan Invite Attacks because they require less commands
- 3. On a server with no flood protection, '0' can be used as the 'Number of seconds between
- commands.'
- 4. Jammer is best used with a maximum length username [15chars] suchas '@@@@SPAMBOT@@@@'
- 5. Some PvPGN server admins have manually patched these spam loopholes. Test on your own
- accounts first to determine which if any attack modes work on your server
- 6. If Friend List Attack works on your server, but anti-flooding is enabled, you can still
- spam an entire screen by loading multiple Friend List Attacks (multiple WarJammer windows)
- simultaneously. However this multi loading technique does not work as well with the Clan
- Invite Attack because a user can only be invited to one clan at a time, whereas mulitple
- users can send Friend List notifications simlutaneously.

INSTRUCTIONS:
- [Install WarJammer2.0]
- [Run WarJammer2.0]
- Follow command prompts to configure your settings

KNOWN ISSUES:
- Make sure your SPAMBOT account is not already logged into the server before using WarJammer.
- Else WarJammer will report 'Login Failed.'

RELEASE NOTES:
Ver 2.1
- New feature: If the SPAMBOT is whispered to or if there is chatter in its channel, it will
- display those messages to the console. This is a security enhancement over Ver2.0 because
- previously whisper or chat data could have been interpreted as a server communication.
- For example, if someone whispered or said in chat channel 'flooding', it could have been
- interpreted as disconnect due to flooding. Ver2.1 filters whisper and chat by users out,
- displays the messages to the console, ignores them, and restarts the loop.

Ver 2.0
- Added new attack mode: Clan Invite with user supplied variable for Clan Name. Clan Tag
- is randomly generated. Clans are auto disbanded at end of use. 
- Added new duration mode to both attack modes: 'Until Offline'
- Added flood protection with user supplied variable: 'Number of seconds between commands'
- Error checking

Ver 1.0
- Initial working version, Friend List Attack with duration variable 'X Number of Times'