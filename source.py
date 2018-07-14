#!/usr/bin/
import praw
import config
import pdb
import os
import textwrap
import datetime

def isBinary(inputString):
    for letter in inputString:
        if letter != '0' and letter != '1':
            return False
    return True
def convertToASCII(inputString):
    stringLength = len(inputString)//8
    outputList = []    
    asciiDict = {i: chr(i) for i in range(255)}
    parts = textwrap.wrap(inputString, 8)
    print(parts)
    with open("log", "a") as logFile:
            logFile.write(str(parts))
    for current in parts:
        outputList.append(asciiDict[int(current, 2)])
    outputString = ''.join(outputList)
    return outputString

reddit = praw.Reddit(username=config.username,
                     password=config.password,
                     user_agent=config.user_agent,
                     client_id=config.public_id,
                     client_secret=config.secret_id)

subreddit = reddit.subreddit("all")
for comment in subreddit.stream.comments():
    commentBody = comment.body.replace(" ", "")
    if len(commentBody) % 8 == 0 and len(commentBody) != 0 and isBinary(commentBody) == True:
        commentBody = convertToASCII(commentBody)
        currentTime = datetime.datetime.now()
        logEntry = "\nThe comment says: \n\n" + commentBody
        logEntry += "\n\nBy: " + comment.author.name + " in r/"
        logEntry += comment.subreddit.display_name + " at "
        logEntry += currentTime.strftime("%Y-%m-%d %H:%M:%S")
        logEntry += " \n\n ------------------ \n\n"
        print(logEntry)
        with open("log", "a") as logFile:
            logFile.write(logEntry)
        reply = "The comment says: \n \n" + commentBody + "\n \n ^I ^am ^a ^bot."
        reply += " ^PM ^my ^[creator](https://reddit.com/user/orangeFluu) ^if ^I ^did ^something ^wrong."
        comment.reply(reply)
