#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import sys, json, os
import re
import requests

from src import InstaBot
from src.check_status import check_status
from src.feed_scanner import feed_scanner
from src.follow_protocol import follow_protocol
from src.unfollow_protocol import unfollow_protocol
from src import readWriteCSV

completedFollows=0
updateCounter=0
usersFollowed = 0
i = 0

credentials = [
    {'login':"followerforever69",'password':"YDCdmnc3kC4GpZrHLPA(pgTrpDpApRDC+7Cx4LsVjzKgZXZFXPtPdQhLKuK4pLrv"},
    {'login':"followerforever70",'password':"LqRKtB24GXJKWbiJnnu2LAGosYBqBzvmdN2PQEdZd7nrdPeD$GyAeEyGLtq>ocMF"}
]

# make an empty array/
# that will be filled with instances of logged in accounts
bots = []

#Fill bots array with logged in instances of InstaBot
for i in range(0,len(credentials)):

    bots.append(
            InstaBot(
            login=credentials[i]['login'],
            password=credentials[i]['password'],
            log_mod=0,
            proxy=''
            )
        )

def nameToID(theUserName):

        textArray = []
        rawHTML = requests.get("https://www.instagram.com/"+theUserName)
        textArray = rawHTML.text
        thisID = re.compile(r'(?<=profilePage_)\d+',0).search(textArray).group(0)
        print("The ID for User %s is %s"%(theUserName,thisID))
        return(thisID)


######Find and return the oldest new name since the last request
def followNewUser(currentCount):

        nextUserPos = currentCount + 1 #next user in list
        nextUser = readWriteCSV.searchForUserName(nextUserPos) #get name at next pos
        print(nextUser)
        nextID = nameToID(nextUser) #change that to an ID

        #TODO check if I already follow that person

        #send that ID through the bots to follow it
        for currentBot in bots:

            currentBot.follow(nextID)
            print("I should be following this person right now: %s?" %nextID)
            time.sleep(1)

            #if !result:
                #TODO somehting like bot.login()

        return(nextUser)

while True:

    mode = 0

    #ask what the current count is
    print("I have followed this many people: %d" %usersFollowed)

    writtenNames = readWriteCSV.countUserNames()

    print("the CSV says there are this many names: %d" %writtenNames)

    #check to see if the current avail names is longer than it was last time
    if writtenNames > usersFollowed:
            print("there's a new row!")
            latestFollow = followNewUser(usersFollowed)
            print("I have now finished following: %s" %latestFollow)

            usersFollowed+=1

    if writtenNames == usersFollowed:
        print("I'm all caught up!")
        time.sleep(5)
        print("I need to ask that the CSV is reread")
        readWriteCSV.checkCSV()

    print("nap time")
    time.sleep(1)
