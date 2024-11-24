#1. What is a class?
#A class is a blueprint for creating objects with specific attributes and methods.

#2. What is an instance?
#An instance is a single object created from a class.

#3. What is encapsulation?
#Encapsulation is  hiding the internal details of an object and exposing only the necessary parts.

#4. What is abstraction?
#Abstraction is hiding the complex details and showing only the essential features of an object.

#5. What is inheritance?
#Inheritance is when a class inherits attributes and methods from another class.

#6. What is multiple inheritance?
#Multiple inheritance is when a class inherits from more than one parent class.

#7. What is polymorphism?
#Polymorphism allows different objects to respond to the same method in their own way.

#8. What is method resolution order (MRO)?
#Method Resolution Order (MRO) is the order in which classes are searched when calling a method in multiple inheritance.


#Part 2:



import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

class Deck:
    def __init__(self):
        self.cards = []
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        
        for suit in suits:
            for value in values:
                self.cards.append(Card(suit, value))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop() if self.cards else None


deck = Deck()
deck.shuffle()

# 5 cards
for _ in range(5):
    card = deck.deal()
    print(f"{card.value} of {card.suit}")
