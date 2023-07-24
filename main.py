from deck import Deck
from player import Player


def deal(player1, player2, deck):
    deck.shuffle()
    for i in range(52):
        card_to_deal = deck.deal_one()
        if i % 2 == 0:
            player1.add_card(card_to_deal)
        else:
            player2.add_card(card_to_deal)


if __name__ == '__main__':
    game_on = True
    round_number = 0
    player_one = Player('Player1')
    player_two = Player('Player2')
    new_deck = Deck()
    deal(player_one, player_two, new_deck)

    while game_on:
        round_number += 1
        print(f'Round: {round_number}')
        if len(player_one.all_cards) == 0:
            print(f'{player_one.name} is out of cards! {player_two.name} wins!')
            game_on = False
            break
        elif len(player_two.all_cards) == 0:
            print(f'{player_two.name} is out of cards! {player_one.name} wins!')
            game_on = False
            break

        player_one_cards = [player_one.play_card()]
        player_two_cards = [player_two.play_card()]

        at_war = True
        while at_war:
            if player_one_cards[-1].value > player_two_cards[-1].value:
                player_one.add_card(player_one_cards)
                player_one.add_card(player_two_cards)
                player_one_cards = []
                player_two_cards = []
                at_war = False

            elif player_two_cards[-1].value > player_one_cards[-1].value:
                player_two.add_card(player_two_cards)
                player_two.add_card(player_one_cards)
                player_one_cards = []
                player_two_cards = []
                at_war = False

            else:
                print('WAR!!!')
                if len(player_one.all_cards) < 5:
                    game_on = False
                    print(f'{player_one.name} unable to declare war')
                    print(f'{player_two.name} wins!')
                    break

                elif len(player_two.all_cards) < 5:
                    game_on = False
                    print(f'{player_two.name} unable to declare war')
                    print(f'{player_one.name} wins!')
                    break

                else:
                    for i in range(5):
                        player_one_cards.append(player_one.play_card())
                        player_two_cards.append(player_two.play_card())


