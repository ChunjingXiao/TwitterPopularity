# -*- coding: utf-8 -*-
# select data from TweetTimeRtSparseClean whose users are in SelectUserOne

# input1: SelectUserOne    
# userID	screen	lang	Follower	Friend	Favourite	Status	List	CreatedAt	UtcOffset	TimeZone
# 15074406	junkdiver	ja	214	158	339	88872	30	2008-06-10 15:59:07	32400	Tokyo
# 0              1      2        3              4       5               6       7       8                9               10

# input2: TweetTimeRtSparseClean  # 
# tweetIDNum	hourTime1	rtLabel	userID		tweetID			text1   firstDate
# 1		19		8	12815132	713065384270815233	t1	20171119
# 2		13		27	12815132	711522813199384578	t2	20171119
# 0		1		2	3		4			5	6

# output: TweetTimeRtSparseSelect
# tweetIDNum	hourTime1	rtLabel	userID		tweetID			text1   firstDate
# 1		19		0	12815132	713065384270815233	t1	20171119
# 2		13		1	12815132	711522813199384578	t2	20171119
# 0		1		2	3		4			5	6

import urllib2
import urllib
import cookielib
import re
import datetime
import time
import sys
import os
import traceback
from urllib2 import HTTPError, Request, urlopen, URLError
import difflib
#import adodbapi
#import minjson


def printTime(beginTime):
    endTime = datetime.datetime.now() #calculate time
    print ("------------consumed-----------time-----------begin-----------")
    print ("consumed time:" + str(endTime - beginTime) )
    print ("------------consumed-----------time-----------end-------------")


def readSelectUsers(inFile1,userIdDictTW):
    fin = open(inFile1) 
    count =0
    for current in fin:
        count += 1
        data = current.replace('\n','')
        curL = data.split('\t')
        twitterID = curL[0]
        UtcOffset = int(curL[9])/3600
        userIdDictTW[twitterID] = UtcOffset
    #print '----readSelectUsers------len(userIdDictTW)----' + str(len(userIdDictTW)) + '----'
    #print '----readFacebookTwitter finished------len(userIdDictFB)----' + str(len(userIdDictFB)) + '----'
    fin.close()
    
def readTweetFile(inFile2,userIdDictTW,outFile):
    fout = open(outFile,"w")
    count =0
    fin = open(inFile2)
    for current in fin:
        count += 1
        data = current.replace('\n','')
        curL = data.split('\t')
        userId = curL[3]
        if(not userIdDictTW.has_key(userId)):
            continue
        
        fout.write(current)
    
    
def main(argv):
    inFile1 = argv[1]  # SelectUserOne 
    inFile2 = argv[2]  # TweetTimeRtSparseClean
    outFile = argv[3]  # TweetTimeRtSparseSelect
    reload(sys)
    sys.setdefaultencoding('utf-8')
    beginTime = datetime.datetime.now() 
    
    
    userIdDictTW = {}   # userIdDictTW[idTW] = timezone
    readSelectUsers(inFile1, userIdDictTW)
    
    readTweetFile(inFile2,userIdDictTW,outFile)
    
    #printTime(beginTime)       
    #print "\a"
    #print 'finish' 

    
if __name__ == "__main__":
    #ִmain fuction
    main(sys.argv)
