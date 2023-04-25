import random
from typing import List


    


#Model Class 
class Model:
    def __init__(self):
        self.players = 4
        self.cards_per_player = 13
        self.hearts_value = 1
        self.queen_of_spades_value =13
        self.suits = ["H","S","D","C"] #h = hearts, s = spades, d = diamonds, and c= clubs
        self.cards = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"] #j=jack, Q=queen, k=king, A=Ace
        self.deck = self.build_deck()
        # Shuffle Deck
        self.face_cards = ["J", "Q", "K"]
        
        
    def build_deck(self) -> List[str]:
        deck = []
        for suit in self.suits:
            for card in self.cards:
                c = f"{suit}{card}"
                deck.append(c) 
        return deck


    #Function to calculate score
    def  calculate_score(self, cards):
    # def  calculate_score(cards):
        score = 0
        for card in cards:
            if card[0] == "S":
                score += self.model.hearts_value 
            elif card == "qs":
                score += self.queen_of_spades_value
            elif card [0] == "s":
                pass
            score += 1
        return score 

    def show(self):
        for i in self.cards:
            i.show()


    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            random = random.randint(0, i)
            

    #Function to deal cards
    def deal_cards(self):
        cards = {}
        for i in range(self.players):
            cards.update({i:[]}) 
        # {0:[], 1: [], 2: [] ....}
        for i in range(self.cards_per_player):
            for player_num in cards:
                current_card = self.deck.pop()
                cards[player_num].append(current_card)
        return cards



    #Function to play game
    def play_game(self):
        cards = self.deal_cards()
        player_scores = [0] * players
        current_player = 0
        while len(cards) > 0:
            break
        #current player plays a card 
        card_played = input("Player" + str(current_player))

#Function to  update score

def update_score(player: int, score: int):
    player_scores[player] += score

    print("Player" +str(player) + "score:" + str(player_scores[player]))

#Function to check validity of cards
def is_valid_hearts_card(card):
    valid_suits = [ 'H','S','D','C']
    valid_values = [2,3,4,5,6,7,8,9,10,11,12,13,14,]
    if card[0] in valid_suits and card [1] in valid_values:
        return True 
    else:
        return False 

#funtion to update score everytime a player takes a trick
def update_score_on_trick(player):
    score = 0
    trick = []
    for card in trick:
        if card[0] == "H":
            score += hearts_value
        elif card[0] == "QS":
            score += queen_of_spades_value
        elif card [0] == "S":
            pass
    update_score(player,score)


#Function to check if the player has won the game
def has_player_won(player):
    if player_scores[player] == min(player_scores):
        return True
    else:
        return False
    print (player, "Is the Winner!")


#Function to check if game is over
def is_game_over():
    if len(cards) == 0:
        return True
    else: 
        return False 


#Functions to determine which player goes first
def is_player_first(player):
    for card in player_cards[player]:
        if card == "C2":
            return True
    return False 


#View class
class View:
    def __init__(self):
        pass

    def  dislpay_game_data(self, model):
        print("Players:", model.players)
        print("Cards per player:", model.player_scores)
        print("Hearts value:", model.hearts_value)
        print("Queen of Spades value:", model.queen_of_spades_value)
        print("Player Scores:")

def main():
    m = Model()
    #print(m.deck)



if __name__ == '__main__':
    main()