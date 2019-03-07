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
import re
import numpy as np
import csv

def printTime(beginTime):
    endTime = datetime.datetime.now() #calculate time
    print ("------------consumed-----------time-----------begin-----------")
    print ("consumed time:" + str(endTime - beginTime) )
    print ("------------consumed-----------time-----------end-------------")

    

    
def clean_str(string):
    """
    Tokenization/string cleaning for all datasets except for SST.
    Original taken from https://github.com/yoonkim/CNN_sentence/blob/master/process_data.py
    """
    string = re.sub(r"[^A-Za-z0-9(),!?\'\`]", " ", string)
    string = re.sub(r"\'s", " \'s", string)
    string = re.sub(r"\'ve", " \'ve", string)
    string = re.sub(r"n\'t", " n\'t", string)
    string = re.sub(r"\'re", " \'re", string)
    string = re.sub(r"\'d", " \'d", string)
    string = re.sub(r"\'ll", " \'ll", string)
    string = re.sub(r",", " , ", string)
    string = re.sub(r"!", " ! ", string)
    string = re.sub(r"\(", " \( ", string)
    string = re.sub(r"\)", " \) ", string)
    string = re.sub(r"\?", " \? ", string)
    string = re.sub(r"\s{2,}", " ", string)
    return string.strip().lower()

    
def load_data_and_labels(positive_data_file, negative_data_file):
    """
    Loads MR polarity data from files, splits the data into words and generates labels.
    Returns split sentences and labels.
    """
    # Load data from files
    positive_examples = list(open(positive_data_file, "r",encoding ='utf-8').readlines())
    positive_examples = [s.strip() for s in positive_examples]
    negative_examples = list(open(negative_data_file, "r",encoding ='utf-8').readlines())
    negative_examples = [s.strip() for s in negative_examples]
    # Split by words
    x_text = positive_examples + negative_examples
    x_text = [clean_str(sent) for sent in x_text]
    # Generate labels
    positive_labels = [[0, 1] for _ in positive_examples]
    negative_labels = [[1, 0] for _ in negative_examples]
    y = np.concatenate([positive_labels, negative_labels], 0)
    return [x_text, y]
def computeAccuracy(x_text, y_label, textLabel,output):
    fout = open(output,'w')
        
    
    
    rowCount = 0
    positiveSample = 0
    negativeSample = 0    
    correctCountAll = 0
    correctCountPos = 0
    correctCountNeg = 0
    writeCache = ''
    for ii in range(len(x_text)):
        rowCount += 1
        
        classLabel =  int(y_label[ii][1])  
        predictLabel = int(textLabel[x_text[ii]])  
        if(classLabel == 0):   # if classLabel < 0.5, then negative 0
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
        
    print('Accuracy--------' + str(accurate) + '--------')
    
    if(rowCount != 0):        
        fout.write('0000' +'\t'+ str(sensitivity)+'\t'+ str(specificity)+'\t'+ str(gMean)+'\n')
    
    
        
def main(argv):
    inFile1 = argv[1]  # prediction.csv
    inFilePos = argv[2]  # rt-polarity.pos 
    inFileNeg = argv[3]  # rt-polarity.neg 
    output = argv[4]   # pred.txt 
    beginTime = datetime.datetime.now() 


    x_text, y_label = load_data_and_labels(inFilePos, inFileNeg)
    
    textLabel = {}
    with open(inFile1) as f:
        reader = csv.reader(f)
        #print(list(reader))    
        for row in reader:
            if(len(row) > 1):
                textLabel[row[0]] = int(float(row[1]))
                #print(textLabel[row[0]])
    
    computeAccuracy(x_text, y_label, textLabel,output)
    
    #userIdCount = {} # userIdCount[userID] = tweetCount
    #readUserId(inFile1,userIdCount)
    #computeAccuracy(inFile1,userIdCount,output)
    
    #printTime(beginTime)       
    #print "\a"
    #print 'finish' 

if __name__ == "__main__":
    #ִmain fuction
    main(sys.argv)
    
    