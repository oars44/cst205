# Blackjack hand logic functions #

# By Oliver Stringer <ostringer@csumb.edu>
# CST 205
# Description: Determines numerical value of hands and suggests best move


# assign a numerical value based on a cards rank
def value(rank):
    card_value = 0
    k = 0
    for Rank in ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven',

                 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']:
        if rank == Rank:
            if k < 9:  # Ace through 9 are numbered 1 through 9
                card_value = k + 1
            else:  # Ten through King are all valued at 10
                card_value = 10
        k += 1

    return card_value


# Compare the dealer and players hands and determine whether to Hit, Stand, or DoubleDown
def compare(dealer_hand, player_hand, ace):
    """Based off of a simplified table of Blackjack hands assuming the dealer is using
        a single deck and stands at a soft 17". Does not support splitting"""

    over, message = game_over(dealer_hand, player_hand)

    if over:  # First check for win and bust conditions for both sides
        return message

    if not ace:  # Decision logic for hands without an Ace
        if player_hand > 16:
            message = "STAND"  # If above 16 always stand
        elif player_hand > 12:
            if dealer_hand < 7:
                message = "STAND"  # Stand if dealer upcard is six or less, since they are likely to bust
            else:
                message = "HIT"  # Hit if dealer upcard is 7 or greater
        elif player_hand > 9:
            message = "DOUBLE DOWN!!!"  # Double down on 9, 10, 11
        else:
            message = "HIT"  # If lower than 9, hit
    else:  # Decision logic for hands with an Ace
        if (player_hand - 1) == 10:  # Find the value of the players other cards by subtracting the value of the Ace (1)
            message = "BLACKJACK"  # Ace and any 10 value card is blackjack
        elif (player_hand - 1) > 7:
            message = "STAND"  # Stand at 19 and above
        elif (player_hand - 1) == 7:
            if 2 < dealer_hand < 7:
                message = "DOUBLE DOWN"  # At 18, double down if dealer is between 2 and 7...
            else:
                message = "STAND"  # ...else stand
        elif (player_hand - 1) > 3:
            if 3 < dealer_hand < 7:
                message = "DOUBLE DOWN"  # If between 15 and 17, double down if dealer between 3 and 7...
            else:
                message = "HIT"  # ...else hit
        else:
            if 4 < dealer_hand < 7:
                message = "DOUBLE DOWN"  # When below 15, double down if dealer between 4 and 7...
            else:
                message = "HIT"  # ... else hit

    if player_hand < 1:  # Check if player has at lest two cards in hand...
        message = ""  # ... if not, don't give advice

    return message


# Check if an Ace is present in a hand
def ace_check(cards):
    ace = False

    for card in cards:
        if card.best_rank_match == 'Ace':
            ace = True

    return ace


# Determine which cards belong to the dealer and which belong to the player
def separate_hands(cards):
    play_hnd = []
    deal_hnd = []

    for card in cards:
        if card.best_suit_match == "Dealers' ":
            deal_hnd.append(card)
        else:
            play_hnd.append(card)

    return deal_hnd, play_hnd


# Checks game to see if either the player or dealer has won
def game_over(deal_hnd, play_hnd):
    over = False

    if deal_hnd == 21 or play_hnd > 21:  # Dealer blackjack or player bust
        move = "DEALER WINS"
        over = True
        return over, move

    if (16 < deal_hnd < 21) and (deal_hnd > play_hnd):  # Dealer stands (at soft 17) at greater value than player
        move = "DEALER WINS"
        over = True
        return over, move

    if play_hnd == 21 or deal_hnd > 21:  # Player blackjack or dealer bust
        move = "PLAYER WINS"
        over = True
        return over, move

    if play_hnd > deal_hnd and 16 < deal_hnd < 21:  # Dealer stands (at soft 17) at lower value than player
        move = "PLAYER WINS"
        over = True
        return over, move

    move = ""
    return over, move


# Determine the optimal move for the player to make
def best_move(qcards):
    dealer_hand, player_hand = separate_hands(qcards)  # Separate found cards between dealer and player
    dealer_val, player_val = 0, 0
    ace = ace_check(player_hand)  # Check if player has an Ace up their sleeve

    for card in dealer_hand:  # Create hand values for dealer and player
        rank = card.best_rank_match  # Dealer hand starts as only a single card, but still needs
        dealer_val += value(rank)  # to be monitored to determine if/when they bust

    for card in player_hand:
        rank = card.best_rank_match
        player_val += value(rank)

    move = compare(dealer_val, player_val, ace)  # Determine best move for player
    return move, dealer_val, player_val
