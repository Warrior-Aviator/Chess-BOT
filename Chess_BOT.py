#!/usr/bin/env python
# coding: utf-8

# In[7]:


import chess as ch
import random as rd

class Engine:
    
    def __init__(self,board,maxDepth,color):
        self.board=board
        self.maxDepth=maxDepth
        self.color=color
    
    def getBestMove(self):
        return self.engine(None,1)
    
    def evalFunt(self):
        compt=0
        for i in range(64):
            compt+=self.sqResPoint(ch.SQUARES[i])
        compt+=self.mate()+self.openning()+0.001*rd.random()
        
    def openning(self):
        if(self.board.fullmove_number<10):
            if(self.board.turn==self.color):
                return 1/30*self.board.legal_moves.count()
            else:
                return -1/30*self.board.legal_moves.count()
        else:
            return 0
        
    def mate(self):
        if(self.board.legal_moves.count()==0):
            if(self.board.trun==self.color):
                return -999
            else:
                return 999
        else:
            return 0
        
    #Takes square as input and returns corresponding Han's Berliner's system value of its resident
    
    def sqResPoint(self,square):
        pieceValue=0
        if(self.board.piece_type_at(square)==ch.PAWN):
            pieceValue=1
        elif(self.board.piece_type_at(square)==ch.ROOK):
            pieceValue=5.1
        elif(self.board.piece_type_at(square)==ch.BISHOP):
            pieceValue=3.33
        elif(self.board.piece_type_at(square)==ch.KNIGHT):
            pieceValue=3.2
        elif(self.board.piece_type_at(square)==ch.QUEEN):
            pieceValue=8.8
    
    def engine(self,candidate,depth):
        
        if (depth==self.maxDepth or self.borad.legal_moves.count()==0):
            return self.evalFunc()
        
        else:
            #get list of legal moves of current position
            
            moveList=list(self.board.legal_moves)
            
            #initialise newCandidate
            
            newCandidate=None
            
            if(depth%2!=0):
                newCandidate=float("-infinity")
            else:
                newCandidate=float("infinity")
                
            for i in moveList:
                #Play move i
                
                self.board.push(i)
                
                #Get the value of move i
                
                value=self.engine(newCandidate,depth+1)
                
                #Basic minmax algo
                
                #if maximising (engine's turn)
                
                if(value>newCandidate and depth%2!=0):
                    newCandidate=value
                    if(depth==1):
                        move=i
                
                #if minimising (human's turn)
                
                elif(value<newCandidate and depth%2==0):
                    newCandidate=value
                    
                #Alpha-beta pruning cuts:
                
                #if previous move was made by engine
                
                if(candidate!=None and value<candidate and depth%2==0):
                    self.board.pop()
                    break
                    
                #if previous move was made by human
                
                elif(candidate!=None and value>candidate and depth%2!=0):
                    self.board.pop()
                    break
        
        if(depth>1):
            
            #return value of node in tree
            
            return newCandidate
        else:
            return move


# In[ ]:




