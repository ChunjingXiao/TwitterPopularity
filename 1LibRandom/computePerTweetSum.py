# -*- coding: utf-8 -*-
# 

# input: pairwiseRankDataTest
# classLabel globleFeature #user #items userFeature itemFeature1 itemFeature2
# 1	0	1	2	2:1	170:1	180:-1
# 0	0	1	2	2:1	523:1	533:-1
# 1	0	1	2	3:1	123:1	133:-1

# input2: pred.txt
# 0.421134
# 0.401046
# 0.663426

# output: 
#

import sys
import datetime
import math

def printTime(beginTime):
    endTime = datetime.datetime.now() #calculate time
    print ("------------consumed-----------time-----------begin-----------")
    print ("consumed time:" + str(endTime - beginTime) )
    print ("------------consumed-----------time-----------end-------------")
    
def readUserId(inFile1,userIdCount):
    try:
        fin = open(inFile1)
        for current in fin:
            data = current.replace('\n','')
            curL = data.split('\t')
            userId = curL[0]
            if(not userIdCount.has_key(userId)):
                userIdCount[userId] = 0
            userIdCount[userId] += 1
    except:
        return '11'
    
def computeAccuracy(inFile1,userIdCount,output):
    fout = open(output,'w')
        
    fin = open(inFile1,"r")   # 
    rowCount = 0
    positiveSample = 0
    negativeSample = 0    
    correctCountAll = 0
    correctCountPos = 0
    correctCountNeg = 0
    writeCache = ''
    for current in fin:
        rowCount += 1
        data = current.replace('\n','')
        curL = data.split('\t')
        userId = curL[0]
        classLabel = int(curL[1])    
        predictLabel = int(curL[2])    
        if(classLabel < 0.5):   # if classLabel < 0.5, then negative 0
            negativeSample += 1
            if( classLabel == predictLabel):
                correctCountNeg += 1
                correctCountAll += 1
        else:
            positiveSample += 1
            if(  classLabel == predictLabel):
                correctCountPos += 1
                correctCountAll += 1


    
    if(rowCount == 0 or positiveSample == 0 or  negativeSample == 0):
        accurate = -1
        posRatio = -1 
        sensitivity = -1
        specificity = -1
        gMean = -1
    else:
        accurate = round(correctCountAll/float(rowCount),4)
        posRatio = round(positiveSample/float(rowCount),4)
        
        sensitivity = round(correctCountPos/float(positiveSample),4)
        specificity = round(correctCountNeg/float(negativeSample),4)
        gMean =  round(math.sqrt(sensitivity * specificity),4)
        
    print 'Accuracy--------' + str(accurate) + '--------'
    
    if(rowCount != 0):        
        fout.write('0000' + '\t'+ str(sensitivity)+'\t'+ str(specificity)+'\t'+ str(gMean)+'\n')
    
    
    '''
    if(count >= 10):
        posRatio = round(positive/float(count),4)
        if( posRatio >= 0.4 and posRatio <= 0.6):    
            pass
    '''
    
    
        
def main(argv):
    inFile1 = argv[1]  # pairwiseRankDataTest 
    output = argv[2]   # pred.txt 
    reload(sys)
    sys.setdefaultencoding('utf-8')
    beginTime = datetime.datetime.now() 

    userIdCount = {} # userIdCount[userID] = tweetCount
    readUserId(inFile1,userIdCount)
    computeAccuracy(inFile1,userIdCount,output)
    
    #printTime(beginTime)       
    #print "\a"
    #print 'finish' 

if __name__ == "__main__":
    #ִmain fuction
    main(sys.argv)
    
    