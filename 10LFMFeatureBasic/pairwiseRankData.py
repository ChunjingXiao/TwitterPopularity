# -*- coding: utf-8 -*-
# this will 

# input: TweetTimeRtSparseSelect
# tweetIDNum	hourTime1	#RT1	hourTime2	tweetID			text1   firstDate
# 1		19		8	12		713065384270815233	t1	20171119
# 2		13		27	19		711522813199384578	t2	20171031
# 0		1		2	3		4			5	6

# tweetIDNum	hourTime1	#RT1	userID		tweetID			text1   firstDate
# 1		19		8	12815132	713065384270815233	t1	20171119
# 2		13		27	12815132	711522813199384578	t2	20171119
# 0		1		2	3		4			5	6

# output1: pairwiseRankData
# classLabel	#globleFeature	#userFeature	#itemsFeature	userFeature	itemFeature1	itemFeature2	firstDate
# -5	0	1	2	3:1	3:1	23:-1								20171119
# -11	0	1	2	4:1	20:1	10:-1								20171031
# 7	0	1	2	5:1	1:1	23:-1								20171031


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
def readData(inFile,outFile):
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

        firstData = curL[6]     # ---------------------------------for identifying training and test set--------------------------------------
        #fout.write(str(label) +'\t'+ '0\t1\t2' +'\t'+ str(tweetIDNum) + ':1' +'\t'+ str(hourTime1) + ':1' +'\t'+ str(hourTime2) + ':-1' +'\n')
        fout.write(str(numRT1) +'\t'+ '0\t1\t1' +'\t'+ str(count) + ':1' +'\t'+ str(hourTime1) + ':1'  +'\t'+firstData+'\n')

def main(argv):
    inFile = argv[1]    # TweetTimeRtSparseTxt
    outFile = argv[2]   # pairwiseRankData 
    beginTime = datetime.datetime.now()

    
    readData(inFile,outFile)
    
    
    #printTime(beginTime)       
    #print "\a"
    #print 'finish' 

    
if __name__ == "__main__":
    #ִmain fuction
    main(sys.argv)
