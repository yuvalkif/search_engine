# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 13:18:51 2018

@author: adam

Parser class 

"""

class Document:
  
  name = ""
  wordDict = {}
  
  def __init__(self,name):
    self.name = name
    
  def addword(self,word):
    self.wordDict[word] = 1 
    return 1
  
  def incfrequency(self,word):
    self.wordDict[word] += 1

  def str(self):
    for key , value in self.wordDict.items():
      print(key,value)
    return 1



class Parser:
  
  docset = set()
  termSet = set()
  
  def __init__(self):
    return None
  
  def parse(self,document):
    
    mode = 'r'
    line = ''
    doc = Document(document)
    index = 0
    
    print("parsing " + document)
    with open(document , mode) as file :
      
      #main loop for parsing each line
      while(line != ""):
        line = file.readline()
        line = line.strip('\n')
        #percents loop
        percentidx = line.find('percent')
        if(percentidx != -1):
          line = self.__handlePercent__(line,percentidx)
        percentidx = line.find('%')
        if(percentidx != -1):
          line = self.__handlePercent__(line,percentidx)
        ##############
        
        #dollars loop
        dollarsignidx = line.find('$')
        if(dollarsignidx != -1):
          self.__handlePrices__(line,dollarsignidx,'$')
        dollarsidx = line.find('Dollars')
        if(dollarsidx != -1):
          self.__handlePrices__(line,dollarsidx,'-')
        
        #complex '-' expressions
        index = line.find('-')
        if(index != -1):
          line = self.__handleCompelx__(line,index)
          
    
    self.docset.add(doc)
    return 1
  
  
  def __handleCompelx__(self,line,index):
    
    startidx = index
    endidx = index
     
    while((line[startidx] != ' ') & (startidx >= 0)):
      startidx -= 1
    startidx += 1
    while((line[endidx] != ' ') & (endidx < len(line))):
      endidx += 1
    
    self.termSet.add(line[startidx : endidx])
    line = line[ : startidx ] + line[endidx : ]
    
    return line
  
  
  def __handlePrices__(self,line,index,sign):
    
    endidx = index
    startidx = index
    done = False
    secondwordstart = 0
    M = 'million'
    B = 'billion'
    T = 'trillion'
    term = ''
    
    if(sign == '$'):
      while(line[endidx] != ' '):
        endidx += 1
      endidx = endidx + 1 
      secondwordstart = endidx
      while(line[endidx] != ' '):
        endidx += 1
        
      endidx += 1
      secondword = line[secondwordstart : endidx]
      if(secondword == M):
        term = line[index+1 : secondwordstart-1] + 'M Dollars'
        self.termSet.add(term)
      elif(secondword == B):
        term = line[index+1 : secondwordstart-1] + 'M Dollars'
        self.termSet.add(term)
      elif(secondword == T):
        term = line[index+1 : secondwordstart-1] + 'M Dollars'
        self.termSet.add(term)
      line = line[ : index] + line[secondwordstart : len(secondword)]
    
    else:
      words = []
      while(done == False):
        while(startidx != ' '):
          startidx -= 1
        endidx = startidx - 1
        if(line[endidx].isdigit() == True):
          done = True
        else:
          startidx = endidx
            
    #now get the number
    startidx = endidx
    while(line[startidx] != ' '):
      startidx -= 1
    words.append(line[startidx+1 : endidx+1])#got the number  
      
    return line
  
  
  def  __numbersHandler__():
    return ""
  
  
  def __regularNumbers__(number):
    
    K = 1000
    M = K * 1000
    B = M * 1000
    
    if number < K:
      return number 
  
    if (number < M) & (number >= K) :
      return str(number/K + "K")
    
    if(number > M ) & (number < B) : 
      return str(number/M + "M")
    
    if(number >= B):
      return str(number/B + "B")
    
    return 0

      
  def __lettersHnadler__():
    return ""

    
  def __handlePercent__(self,line,percentidx,symbol):
    
    number = ''
    index = 0
    
    if(symbol != '%'):
      if(len(line) > percentidx +7):#check for 'age'
        if(line[percentidx+7] == ' '):#so just percent
          if(percentidx == 0):#so the number is in the last line
              print('check last line')
          else:#number is in this line
                index = percentidx - 2
                while(line[index] != ' '):
                  index -= 1
                  number = line[index : percentidx-1] 
                  line = line[0:index] + line[percentidx+7:]
    else:
      index = percentidx-1
      while(line[index] != ' '):
        percentidx -= 1
      number = line[index : percentidx - 1]
      line = line[0 : index ] + line[percentidx + 1 : ]
      
    self.termSet.add(number+'%')
    
    return line


