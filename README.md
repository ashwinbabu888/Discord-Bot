# Discord-Bot
A powerful, multipurpose Discord bot programmed using the Discord API and Python 3 that can do tasks such as keep time, respond to messages, organize servers, etc. Created for the DNHS Debate Discord server to automate and ease tasks on Discord as well as give more control over different functions in Discord.

**Note: Original code was written in JavaScript, but later rewritten in Python. Therefore, the "index.js" file is outdated and not used.
        Additionally, the Discord API token listed in this repository is not the same one being used to run the bot (for security
        reasons); it has been regenerated.**

## Passive Abilities
- Prints "Bot has been initialized." when initialized and ready to be used.
- Returns the name of a member who leaves or joins the server along with a message.

```
Commands list:

!ping - Returns your current device's ping in milliseconds

!kick name#0000 reason - Kicks the inputted member from the server and writes the inputted reason in the server audit logs

!ban name#0000 reason - Bans the inputted member from the server and writes the inputted reason in the server audit logs

!unban name#0000 - Searches through the server ban logs for the inputted member's name/tag and unbans them.

!clear # - Clears the inputted number of messages (including the clear statement); defaults to 5 messages without an inputted number

!echo + message (!copy works too) - Prints the message that the user inputted and clears the user's !echo/!copy statement.

!flip - Returns heads or tails. Useful for pre-rounding in Public Forum debate.

!decide - Randomly decides the side and order for a Public Forum debate.

!8ball + question - Returns your question as well as an answer to it (much like a Magic 8Ball)
```
