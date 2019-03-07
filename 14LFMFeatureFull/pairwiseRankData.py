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



# 1316	7	6	24	12	8071902	932499579353755649	cloud#n move#n|#photo#n by#o|#photo#n KUxFOFO1#n|cloud#n #photo#n|

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

def readDependIdText(dependFile,dependIdText):
    fin = open(dependFile,"r")    
    count = 0
    num = 1
    for current in fin:
        count += 1
        data = current.replace('\n','')
        curL = data.split('\t')
        tweetId = curL[4]
        text = curL[5]
        dependIdText[tweetId] = text 
          
def readText(inFile,wordDict,dependIdText):
    fin = open(inFile,"r")    
    count = 0
    num = 1
    for current in fin:
        count += 1
        data = current.replace('\n','')
        curL = data.split('\t')
        #tweetId = curL[6]
        text = dependIdText[curL[4]]
        
        dependGroup = text.split('|')
        for oneGroup in dependGroup:  
                oneWord = oneGroup.split(' ')
                for word in oneWord:
                    wordPos = word.split('*')  
                    one2 = wordPos[0].lower()
                    if(not wordDict.has_key(one2)):
                            wordDict[one2] = num
                            num += 1                    
        
        
        
        
        
def readNeiFeature(inFile2,neighborFeature,tweetIdCount):
    fin = open(inFile2)
    for current in fin:
        data = current.replace('\n','')
        data2 = data.strip('\t')
        curL = data2.split('\t')
        tweetId = curL[0]
        neighborFeature[tweetId] = ''
        for ii in range(len(curL) -1):
            
            if(not tweetIdCount.has_key(tweetId)):
                continue
            idValue = curL[ii+1].split(':')
            neighborFeature[tweetId] +=  str(tweetIdCount[idValue[0]])+':' + str(idValue[1]) + '\t'
            
            
        neighborFeature[tweetId] = '\t' + neighborFeature[tweetId]
def readTweetIdCount(inFile,tweetIdCount):
    fin = open(inFile,"r")    # 
    count = 0
    for current in fin:
        count += 1
        data = current.replace('\n','')
        curL = data.split('\t')
        tweetId = curL[4]
        tweetIdCount[tweetId] = count 
        
        
        
        
def readData(inFile,outFile,wordDict,dependIdText,neighborFeature):
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

        
        #tweetId = curL[6]
        text = dependIdText[curL[4]]  #    Brown#n Chris#n|Pays#v Brown#n|Heartbreak#n For#o|Pays#v Heartbreak#n|Cake#n On#o|Pays#v Cake#n|
        
        nounGroup = 0
        verbGroup = 0
        groupType = {}  # groupType[word] = 'n' or 'v'
        text2 = text.strip('|')
        dependGroup = text2.split('|')    # dependGroup = [Brown#n Chris#n,  Pays#v Brown#n,  Heartbreak#n For#o ...]
        for oneGroup in dependGroup:      # compute the amount of nounGroup and verGroup
            gType = 'n'                   
            oneWord = oneGroup.split(' ') # oneGroup = Pays#v Brown#n
            for word in oneWord:          # word = Pays#v
                wordPos = word.split('*') 
                if(wordPos[1] == 'v'):
                    gType = 'v'
            if(gType == 'n'):
                nounGroup += 1
            else:
                verbGroup += 1
            groupType[oneGroup] = gType

        wordWeight = {}
        for oneGroup in dependGroup:
            oneWord = oneGroup.split(' ')
            for word in oneWord:
                wordPos = word.split('*')
                if(not wordWeight.has_key(wordPos[0])):
                    wordWeight[wordPos[0]] = 0
                if(groupType[oneGroup] == 'n'):
                    wordWeight[wordPos[0]] = 2 # round(2/float(nounGroup),4)
                elif(groupType[oneGroup] == 'v'):
                    wordWeight[wordPos[0]] = 1 #round(1/float(verbGroup),4)
                else:
                    wordWeight[wordPos[0]] = 0.4
        
        countWord = len(wordWeight)
        textFeature = ''
        for (u,v) in wordWeight.items():
            #textFeature += str(u) + ':' + str(v) + '\t'
            #textFeature += str(wordDict[u.lower()]) + ':' + str(v) + '\t'
            textFeature += str(wordDict[u.lower()]) + ':' + str(v * 1) + '\t'
        
        
        
        
        tweetId = curL[4]
        if(not neighborFeature.has_key(tweetId)):
            continue
        globalNum = neighborFeature[tweetId].count(':')
            
            
        firstData = curL[6]     # ---------------------------------for identifying training and test set--------------------------------------
        #fout.write(str(label) +'\t'+ '0\t1\t2' +'\t'+ str(tweetIDNum) + ':1' +'\t'+ str(hourTime1) + ':1' +'\t'+ str(hourTime2) + ':-1' +'\n')
        fout.write(str(numRT1) +'\t'+ str(globalNum) +'\t'+ str(countWord) +'\t'+'1'+'\t'+ neighborFeature[tweetId] + '\t'+ textFeature + str(hourTime1) + ':1' +'\t'+firstData +'\n')

def main(argv):
    inFile = argv[1]    # TweetTimeRtSparseTxt
    outFile = argv[2]   # pairwiseRankData 
    beginTime = datetime.datetime.now()

    dependFile = 'TweetTimeRtSparseCleanDepend'
    dependIdText = {} # dependIdText[tweetId] = text
    readDependIdText(dependFile,dependIdText)
    
    wordDict = {} # wordDict[word] = num
    readText(inFile,wordDict,dependIdText)
    
    
    
    tweetIdCount = {}
    readTweetIdCount(inFile,tweetIdCount)  
    inFile2 = "NeighborFeature"
    neighborFeature = {}
    readNeiFeature(inFile2,neighborFeature,tweetIdCount)
    
    
    readData(inFile,outFile,wordDict,dependIdText,neighborFeature)
    
    
    #printTime(beginTime)       
    #print "\a"
    #print 'finish' 

    
if __name__ == "__main__":
    #ִmain fuction
    main(sys.argv)
