# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 13:18:51 2018

@author: adam

Parser class 

"""

class stringSet:
  
  stringset = None
  
  def __init__(self):
    self.stringset = set()
  
  def addword(self,word):
    self.stringset.add(word)

class document:
  
  name = ""
  wordset = None
  flist = []
  
  def __init__(self,name):
    self.name = name
    self.wordset = stringSet()
    
  def addword(self,word):
    self.wordset.addword(word)
    self.incfrequency(self.wordlist.size()-1)
    return 1
  
  def incfrequency(self,inedx):
    self.flist[inedx] += 1

  def toString(self):
    print(self.name + " , " + self.wordset + " , "  + self.flist)
    return 1



class Parser:
  
  
  def __init__(self):
    
    return None
  
  def parse(self,document):
    mode = 'r'
    line = "1"
    
    print("parsing " + document)
    with open(document , mode) as file :
      while(line != ""):
        line = file.readline()
        wordslist = line.strip(',').split(' ')
        print (wordslist)
        
    return 1
  
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
    
  def __handlePercent__():
    
    return ""


