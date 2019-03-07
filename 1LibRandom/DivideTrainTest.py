# -*- coding: utf-8 -*-
# this will write the train and test sets into files ----TweetTimeRtSparseTrain, TweetTimeRtSparseTest-------


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
def readContentFeatureLabel(inFile,outFile1,outFile2):
    fin = open(inFile,"r")    # 
    foutTrain = open(outFile1,'w')
    foutTest = open(outFile2,'w')
    count = 0
    for current in fin:
        data = current.replace('\n','') 
        curL = data.split('\t')
        fdate = int(curL[len(curL)-1])
        
        writeCache = ''
        for i in range(0,len(curL)-1):
            writeCache += curL[i] + '\t'
        if(fdate <= 20171121): # ---------------------------------------threshold for train and test set------------------------------
            foutTrain.write(writeCache.strip('\t') + '\n')
        else:
            foutTest.write(writeCache.strip('\t') + '\n')
        
        
        count += 1
        
def main(argv):
    inFile = argv[1]   # TweetTimeRtSparse  
    outFile1 = argv[2]  # TweetTimeRtSparseTrain
    outFile2 = argv[3]  # TweetTimeRtSparseTest
    #modNum = int(argv[4]) # 1 or 2 or 3....9 or 0
    beginTime = datetime.datetime.now() 
    
    testNum = 10
    #modNum = 1
    readContentFeatureLabel(inFile,outFile1,outFile2)
    
    #printTime(beginTime)       
    #print "\a"
    #print 'finish' 

    
if __name__ == "__main__":
    #ִmain fuction
    main(sys.argv)
