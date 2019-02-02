#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 12:47:22 2018

@author: uxac007
"""

import copy
from Card import Card, Hand, Deck

class ThreeCardPokerDeck(Deck):
    """
    Three-Card Poker deck
    """
    
    def deal_hand(self, name=""):
        """
        Creates a new instance of ThreeCardPokerHand
        hand and initializes it with 3 cards from the deck.
        An optional name argument can be used to specify the 
        name of the player.
        Returns the instance of ThreeCardPokerHand thus created
        """
        hand = ThreeCardPokerHand(self.pop_cards(3), name)
        return hand

class ThreeCardPokerHand(Hand):
    """
    Three-Card Poker hand
    """
    
    all_labels = ['Nothing', 'Pair', 'Flush', 'Straight', 'Three of a Kind',
                  'Straight Flush']
    
#   Question 2
    def _compute_rank(self):
        """
        self, this instance of ThreeCardPokerHand
        Computes the ranking of self and stores it 
        in the self.rank attribute according to the 
        rules described in Question 2 of the project brief.
        Returns None
        """
#        print(Card((self.ranks[0]),self.suits[0]))
#        print(Card((self.ranks[1]),self.suits[1]))
#        print(Card((self.ranks[2]),self.suits[2]))
#        print(Card.ranks[self.ranks[0]])
#        #print(Card.ranks[self.ranks[0]+1])
#        print(self.ranks[1])
#        print(Card.suits[self.suits[1]])
        a = ['Ace','2','3']
        newlist =[self.ranks[0],self.ranks[1],self.ranks[2]]
        newlist = sorted(newlist)
        if(Card.suits[self.suits[0]] == Card.suits[self.suits[1]] == Card.suits[self.suits[2]]):
            #a = ['Ace','2','3']
            if(Card.ranks[self.ranks[0]] in a) and (Card.ranks[self.ranks[1]] in a) and (Card.ranks[self.ranks[2]] in a):
                self.rank=5
            else:
                if(newlist[1] - newlist[0]) == 1 and (newlist[2]-newlist[1])==1:
                #StraightFlush
                    self.rank=5
                else:
                #Flush
                    self.rank=2
                          
        #Threeofakind
        elif (Card.ranks[self.ranks[0]] == Card.ranks[self.ranks[1]] == Card.ranks[self.ranks[2]]):
            self.rank=4
       #Pair
        elif(Card.ranks[self.ranks[0]]==Card.ranks[self.ranks[1]] or Card.ranks[self.ranks[0]]==Card.ranks[self.ranks[2]] or Card.ranks[self.ranks[1]]==Card.ranks[self.ranks[2]] or Card.ranks[self.ranks[2]]==Card.ranks[self.ranks[1]]):
            self.rank=1  
         #Straight
        elif(((newlist[1] - newlist[0]) == 1) and (newlist[2]-newlist[1])==1):
            self.rank=3
            
        elif((Card.ranks[self.ranks[0]] in a) and (Card.ranks[self.ranks[1]] in a) and (Card.ranks[self.ranks[2]] in a)):
            if(Card.ranks[self.ranks[0]] != Card.ranks[self.ranks[1]] != Card.ranks[self.ranks[2]]):
            #if((Card.ranks[self.ranks[0]] != Card.ranks[self.ranks[1]]) and (Card.ranks[self.ranks[0]]!= Card.ranks[self.ranks[2]])and (Card.ranks[self.ranks[1]]!= Card.ranks[self.ranks[2]])):
                self.rank=3

        else:
            self.rank=0
        #pass

#   Question 3    
    def _compare(self, other):
        """
        self, this instance of ThreeCardPokerHand
        other, an instance of ThreeCardPokerHand
        Implements the comparison rules for two ThreeCardPoker
        hands as per the description in Question 3 of the project brief.
        Returns -1 if other is a winning hand, 1 if self is the winning hand,
        and 0 if self and other are tied up.
        """                
        if(self.rank==other.rank):
            if (self.rank == 5 and other.rank==5) or (self.rank ==3 and other.rank==3):
                maxself = max(self.ranks) 
                maxother = max(other.ranks)
                if(maxself>maxother):
                    if(Card.ranks[maxself]=='Ace' or Card.ranks[maxother] == 'Ace'):
                        maxself1 = sorted(self.ranks,reverse=True)
                        maxself1 = maxself1[1]
                        maxother1 = sorted(other.ranks,reverse=True)
                        maxother1 = maxother1[1]
                        if(maxself1>maxother1):
                            return 1
                        else:
                            return 0
                else:
                    if(Card.ranks[maxself]=='Ace' or Card.ranks[maxother] == 'Ace'):
                        maxself1 = sorted(self.ranks,reverse=True)
                        maxself1 = maxself1[1]
                        maxother1 = sorted(other.ranks,reverse=True)
                        maxother1 = maxother1[1]
                        if(maxself1<maxother1):
                            return -1
                        else:
                            return 0
                    
            if (self.rank == 4 and other.rank==4):
                maxself = max(self.ranks) 
                maxother = max(other.ranks)
                if(maxself>maxother):
                    return 1
                else:
                    return -1
            if (self.rank ==2 and other.rank==2) or (self.rank ==0 and other.rank==0):
                newself = sorted(self.ranks,reverse=True)
                newother = sorted(other.ranks,reverse=True)
                maxsel = max(newself)
                maxoth = max(newother)
                if(maxsel>maxoth):
                    return 1
                elif(maxsel<maxoth):
                    return -1
                else:
                    maxsel1= newself[1]
                    maxoth1 = newother[1]
                    if(maxsel1>maxoth1):
                        return 1
                    elif(maxsel1<maxoth1):
                        return -1
                    else:
                        maxsel2= newself[2]
                        maxoth2 = newother[2]
                        if(maxsel2>maxoth2):
                            return 1
                        elif(maxsel2<maxoth2):
                            return -1
                        else:
                            return 0
            if self.rank ==1 and other.rank==1:
                pairwali1 = {}
                pairwali2={}
                for i in range(0,3):
                    if other.ranks[i] not in pairwali1:
                        pairwali1[other.ranks[i]] = 1
                    else:
                        pairwali1[other.ranks[i]]= pairwali1[other.ranks[i]]+1
                    if self.ranks[i] not in pairwali2:
                        pairwali2[self.ranks[i]] = 1
                    else:
                        pairwali2[self.ranks[i]] = pairwali2[self.ranks[i]]+1
                t = list(pairwali1.keys())[list(pairwali1.values()).index(2)]
                r = list(pairwali2.keys())[list(pairwali2.values()).index(2)]
                if t!=r:
                    if t>r:
                        return -1
                    elif t<r:
                        return 1
                elif t==r:
                    t= list(pairwali1.keys())[list(pairwali1.values()).index(1)]
                    r = list(pairwali2.keys())[list(pairwali2.values()).index(1)]
                    if t>r:
                        return -1
                    elif t<r:
                        return 1
                else:
                    return 0

        else:
            if(self.rank>other.rank):
                return 1
            else:
                return -1
#        pass            
        
    
    def get_rank(self):
        """
        getter method for the 
        rank attribute
        Returns 0, 1, 2, 3, 4, 5 if the
        self's rank is respectively Nothing, 
        Pair, Flush, Straight, Three of a Kind, and Straight Flush
        """
        return self.rank
    

    def __init__(self, cards, name=""):
        Hand.__init__(self, name)
        self.cards = copy.deepcopy(cards)
        self.ranks = [card.get_rank() for card in self.cards]
        self.ranks.sort(reverse = True)
        self.suits = [card.get_suit() for card in self.cards]
        self._compute_rank()

    def __lt__(self, other):
        return True if self._compare(other) < 0 else False
    
    def __le__(self, other):
        return True if self._compare(other) <= 0 else False

#   Question 3
    def __gt__(self, other):
        """
        self, this instance of ThreeCardPokerHand
        other, an instance of ThreeCardPokerHand
        Returns True if self is the winning hand, False otherwise
        """
        return True if self._compare(other) > 0 else False
#        pass
    
#   Question 3    
    def __ge__(self, other):
        """
        self, this instance of ThreeCardPokerHand
        other, an instance of ThreeCardPokerHand
        Returns True if self is the winning hand or
        self and other are tied; False otherwise
        """
        return True if self._compare(other) >= 0 else False
#        pass
    
#   Question 3    
    def __eq__(self, other):
        """
        self, this instance of ThreeCardPokerHand
        other, an instance of ThreeCardPokerHand
        Returns True if self and other are tied; 
        False otherwise
        """
        return True if self._compare(other) == 0 else False
#        pass

#   Question 3    
    def __ne__(self, other):
        """
        self, this instance of ThreeCardPokerHand
        other, an instance of ThreeCardPokerHand
        Returns True if self and other are not tied; 
        False otherwise
        """
        return True if self._compare(other) != 0 else False
#        pass

    def get_label(self):
        """
        self, this instance of ThreeCardPokerHand
        Returns a string representation of self.
        """
        return ThreeCardPokerHand.all_labels[self.rank]
    
    def get_full_label(self):
        """
        self, this instance of ThreeCardPokerHand
        Returns a string representation of self replacing
        the Nothing ranking with the highest ranking card.
        Used internally by __str__().
        """
        return  Card.ranks[self.ranks[0]] + '-High' if self.rank == 0 else \
            self.get_label()
        
    def __str__(self):
        """
        self, this instance of ThreeCardPokerHand
        Returns a string representation of self that 
        includes the list of the cards, and the rank.
        """
        return Hand.__str__(self) + '\nHand Rank: ' + self.get_full_label()
        
          
if __name__ == '__main__':
    """
    Test cases
    """
#   Queen-high
    hand1 = ThreeCardPokerHand([Card(10, 0), Card(1, 1), Card(0, 2)])
#    print(hand1._compare(hand1))
    print(hand1)
    print()

###   Straight Flush
    hand2 = ThreeCardPokerHand([Card(12, 0), Card(1, 0), Card(0, 0)])
    print(hand2)
    print()
#    

    print(hand1 < hand2) # True
    print(hand1 > hand2) # False
    print(hand1 <= hand2) # True
    print(hand1 >= hand2) # False
    print(hand1 == hand2) # False
    print(hand1 != hand2) # True
    print()
##    
###   3-Pair + Jack
    hand1 = ThreeCardPokerHand([Card(1, 0), Card(1, 1), Card(9, 2)])
    print(hand1)
    print()
#
#
###   2-Pair + Ace
    hand2 = ThreeCardPokerHand([Card(12, 0), Card(0, 1), Card(0, 0)])
    print(hand2)
    print()
#    
    print(hand1 < hand2) # False
    print(hand1 > hand2) # True
    print(hand1 <= hand2) # False
    print(hand1 >= hand2) # True
    print(hand1 == hand2) # False
    print(hand1 != hand2) # True
    print()


    deck = ThreeCardPokerDeck()
    deck.shuffle()
    hand = deck.deal_hand()
    print(hand)

##   Straight Flush    
    print()
    hand3 = ThreeCardPokerHand([Card(0, 0), Card(1, 0), Card(12, 0)], 'Ruben')
    print(hand3)
#
##   Straight    
    print()
    hand3 = ThreeCardPokerHand([Card(0, 1), Card(12, 2), Card(1, 0)], 'Greg')
    print(hand3)  
#
###   Straight Flush    
    print()
    hand3 = ThreeCardPokerHand([Card(12, 1), Card(10, 1), Card(11, 1)], 'Dealer')   
    print(hand3)                      
#    
###   Flush
    print()
    hand3 = ThreeCardPokerHand([Card(0, 1), Card(1, 1), Card(11, 1)], 'Player')   
    print(hand3)                      