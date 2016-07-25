class Hand(Deck):
    def __init__(self, name=""):
       self.cards = []
       self.name = name
       
    def add(self, card):
        self.cards.append(card)
        
    def deal(self, hands, num_cards=999):
        num_hands=len(hands)
        for i in range(num_hands):
            if self.is_empty(): break
            card=self.pop()
            hand=hands[i % num_hands]
            hand.add(card)