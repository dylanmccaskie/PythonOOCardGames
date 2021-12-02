from PlayingCard import * 
from ConsoleInput import ConsoleInput

class ginrummy:
    deck = None 
    playing_card = PlayingCard()
    console_input = ConsoleInput()
    
    def makedeck(self):
        return self.playing_card.generate_deck()

    def shuffledeck(self, deck):
       return self.playing_card.shuffle_cards(deck)

    def gethands(self, deck, num_players):
        return self.playing_card.deal_cards(deck, 7, num_players)

    def getplayers(self):
        players = 0
        
        while not players in range(2, 6):
            players = int(input("please enter the number of players(an integer between 2 and 5)"))
            
        return players

    def output_hand(self, hand):
        print(*hand, sep = ' ')

    def main(self):
        self.num_players = self.getplayers()
        self.deck = self.makedeck()
        self.deck = self.shuffledeck(self.deck)

if __name__ == "__main__":
    ginrummy().main()