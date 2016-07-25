class Card:
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    ranks = ["narf", "Ace", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "Jack", "Queen", "King"]



    def __init__(self, suit=0, rank=0):
        self.suit=suit
        self.rank=rank
        
    def __str__(self):
        return (self.ranks[self.rank] +" of " + self.suits[self.suit])
        
    def __cmp__(self, other):
        # check the suits
        if self.suit > other.suit: return 1
        if self.suit < other.suit: return -1
        # suits are the same... check ranks
        if self.rank==1 and other.rank!=1: return 1
        if self.rank!=1 and other.rank==1: return -1
        if self.rank==1 and other.rank==1: return 0
        if self.rank > other.rank: return 1
        if self.rank < other.rank: return -1
        # ranks are the same... it's a tie
    
        return 0
    
    
class Deck:
    def __init__(self):
        self.cards=[]
        for suit in range(4):
            for rank in range(1,14):
                self.cards.append(Card(suit,rank))
                
    def print_deck(self):   
        for card in self.cards:
            print card
            
    def __str__(self):
        s = ""
        for i in range(len(self.cards)):
            s = s + " " * i + str(self.cards[i]) + "\n"
        return s
        
    def shuffle(self):
        import random
        num_cards = len(self.cards)
        for i in range(num_cards):
            j = random.randrange(i, num_cards)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]
            
    def remove(self, card):
        if card in self.cards:
            self.cards.remove(card)
            return True
        else:
            return False
            
    def pop(self):
        return self.cards.pop()
        
    def is_empty(self):
        return (len(self.cards) == 0)
        
        
    def deal(self, hands, num_cards=999):
        num_hands=len(hands)
        for i in range(num_cards):
            if self.is_empty(): break
            card=self.pop()
            hand=hands[i % num_hands]
            hand.add(card)        
        
class Hand(Deck):
    def __init__(self, name=""):
       self.cards = []
       self.name = name
       
    def add(self, card):
        self.cards.append(card)
        
    def __str__(self):
        s = "Hand " + self.name
        if self.is_empty():
            s = s + " is empty\n"
        else:
            s = s + " contains\n"
        return s + Deck.__str__(self)    
