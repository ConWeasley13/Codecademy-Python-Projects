import sys
import os
os.system('cls' if os.name == 'nt' else 'clear')

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

lowercase_letters = []
for letter in letters:
    lowercase_letters.append(letter.lower())
all_english_letters = letters + lowercase_letters


points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
points = points + points


letter_to_points = {letter: point for letter, point in zip(all_english_letters, points)}
letter_to_points[' '] = 0


def score_word(word):
    point_total = 0
    for letter in word:
        point_total += letter_to_points.get(letter, 0)
    return point_total


game = {'player1': [], 'player2': []}

def play_word(player,word):
    game[player] = game.get(player, []) + [word]
    return game

def game_score():
    player_to_points = {}
    for player, words in game.items():
        player_points = 0
        for word in words:
            player_points += score_word(word)
        player_to_points[player] = player_points
    return player_to_points

play_word('player1', 'pizza')
play_word('player2', 'question')
print(game_score())
play_word('player1', 'fish')
play_word('player2', 'apple')
print(game_score())

#determining score of fake game
#player_to_words = {'player1': ['BLUE', 'TENNIS', 'EXIT'], 'wordNerd': ['EARTH', 'EYES', 'MACHINE'], 'Lexi Con': ['ERASER', 'BELLY', 'HUSKY'], 'Prof Reader': ['ZAP', 'COMA', 'PERIOD']}

#player_to_points = {}

#for player, words in player_to_words.items():
#    player_points = 0
#    for word in words:
#        player_points += score_word(word)
#    player_to_points[player] = player_points
#print(player_to_points)