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
    asciiDict = {i: chr(i) for i in range(129)}
    parts = textwrap.wrap(inputString, 8)
    print(parts)
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
    #print(titleString + "\n")
    if len(commentBody) % 8 == 0 and len(commentBody) != 0 and isBinary(commentBody) == True:
        commentBody = convertToASCII(commentBody)
        print("The comment says: \n" + commentBody)
        print("\n By: " + comment.author.name + " in r/" + comment.subreddit.display_name + " at " + str(now) + " \n")
        print("It has " + str(comment.score) + " upvotes.\n")
        print("------------------------------------\n")
        reply = "The comment says: \n \n" + commentBody + "\n \n ^I ^am ^a ^bot."
        reply += " ^PM ^my ^[creator](https://reddit.com/user/romanianRunner) ^if ^I ^did ^something ^wrong."
        comment.reply(reply)
