# -*- coding: utf-8 -*-
# this will 

# input: TweetTimeRtSparseTxt
# tweetIDNum	hourTime1	#RT1	userID		tweetID			text1   firstDate
# 1		19		8	12815132	713065384270815233	t1	20171119
# 2		13		27	12815132	711522813199384578	t2	20171119
# 0		1		2	3		4			5	6

# output1: pairwiseRankData
# classLabel	#globleFeature	#userFeature	#itemsFeature	userFeature	itemFeature1	itemFeature2
# -5	0	1	2	3:1	3:1	23:-1
# -11	0	1	2	4:1	20:1	10:-1
# 7	0	1	2	5:1	1:1	23:-1


import re
import datetime
import time
import sys
import os
import traceback

def printTime(beginTime):
    endTime = datetime.datetime.now() #calculate time
    print ("------------consumed-----------time-----------begin-----------")
    print ("consumed time:" + str(endTime - beginTime) )
    print ("------------consumed-----------time-----------end-------------")
    
def readText(inFile,wordDict):
    fin = open(inFile,"r")    
    count = 0
    num = 1
    for current in fin:
        count += 1
        data = current.replace('\n','')
        curL = data.split('\t')
        text = curL[5]
        reSplit = re.compile('[\s]+')
        wordList = reSplit.split(text)
        for one in wordList:
            one2 = one.lower()
            if(not wordDict.has_key(one2)):
                wordDict[one2] = num
                num += 1
            
        
def readData(inFile,outFile,wordDict):
    fin = open(inFile,"r")    # 
    fout = open(outFile,'w')
    count = 0
    for current in fin:
        count += 1
        data = current.replace('\n','')
        curL = data.split('\t')
        tweetIDNum = curL[0]
        hourTime1 = curL[1]
        numRT1 = int(curL[2])      

        
        text = curL[5]
        reSplit = re.compile('[\s]+')
        wordList = reSplit.split(text)
        countWord = len(wordList)
        textFeature = ''
        for one in wordList:
            one2 = one.lower()
            #textFeature += str(wordDict[one2]) + ':' + str(round(1/float(countWord),4)) + '\t'
            textFeature += str(wordDict[one2]) + ':' + '1' + '\t'
        firstData = curL[6]     # ---------------------------------for identifying training and test set--------------------------------------
        #fout.write(str(label) +'\t'+ '0\t1\t2' +'\t'+ str(tweetIDNum) + ':1' +'\t'+ str(hourTime1) + ':1' +'\t'+ str(hourTime2) + ':-1' +'\n')
        fout.write(str(numRT1) +'\t'+'0'+'\t'+ str(countWord) +'\t'+'1'+'\t'+ textFeature + str(hourTime1) + ':1' +'\t'+firstData +'\n')

def main(argv):
    inFile = argv[1]    # TweetTimeRtSparseTxt
    outFile = argv[2]   # pairwiseRankData 
    beginTime = datetime.datetime.now()

    wordDict = {} # wordDict[word] = num
    readText(inFile,wordDict)
    
    readData(inFile,outFile,wordDict)
    
    
    #printTime(beginTime)       
    #print "\a"
    #print 'finish' 

    
if __name__ == "__main__":
    #ִmain fuction
    main(sys.argv)
