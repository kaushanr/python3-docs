class Card:

  def __init__(self,suit,value):
    self.suit = suit
    self.value = value

  def __repr__(self):
    return f'{self.value} of {self.suit}'


class Deck:

  def __init__(self):
    self.cards = [Card(suit,value) for value in 
                  ('A','2','3','4','5','6','7','8','9','10','J','Q','K') 
                  for suit in ('Hearts','Diamonds','Clubs','Spades')
                  ]
    print(self.cards)
    self.deck_size = len(self.cards)

  def __repr__(self):
    return f'Deck of {self.deck_size} cards'

  def count(self):
    return len(self.cards)

  def _deal(self,number):
    if not len(self.cards):
      raise ValueError('All cards have been dealt')
    elif len(self.cards) < number:
      self.deal = [self.cards.pop() for num in range(len(self.cards))]
      return self.deal
    self.deal = [self.cards.pop() for num in range(number)]
    return self.deal

  def shuffle(self):
    from random import shuffle as shfl
    if len(self.cards) < 52:
      raise ValueError('Only full decks can be shuffled')
    shfl(self.cards)
    return self.cards

  def deal_card(self):
    return self._deal(1)

  def deal_hand(self,num):
    return self._deal(num)
