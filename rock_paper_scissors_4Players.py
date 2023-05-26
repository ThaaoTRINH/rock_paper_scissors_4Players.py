import random

moves = ['rock', 'paper', 'scissors']

class Player:
    @staticmethod
    def move():
        return 'rock'

    def learn(self, my_move, their_move):
        pass

class HumanPlayer(Player):
    @staticmethod
    def human_move():
        step_move = input('Rock, paper, scissors? > ')
        return step_move

class RandomPlayer(Player):
    @staticmethod
    def random_move():
        return random.choice(moves)

class ReflectPlayer(Player):
    @staticmethod
    def reflect_move(your_move):
        return your_move

class CyclePlayer(Player):
    @staticmethod
    def cycle_move(your_move):
        if your_move.upper() == 'ROCK':
            result = 'paper'
        elif your_move.upper() == 'PAPER':
            result = 'scissors'
        else:
            result = 'rock'
        return result

def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))

def winner_round(one, two):
    if beats(one, two):
        return one
    else:
        return two

def get_score(one, two):
    if one == two:
        score1 = score2 = 0
    elif beats(one, two):
        score1 = 1
        score2 = 0
    else:
        score1 = 0
        score2 = 1
    return score1, score2


""" Player 1: the user
    player 2: random 
    player 3: reflect from the last round of player 2
    player 4: cycle (get the next one of the user)

Solution based on the comparing from the score of 4 players: 
    . step1: player 1 - player 2 --> winner 1
    . step1: player 3 - player 4 --> winner 2
    __________________
    . step2: winner 1 - winner 2
    score +1 for being a winner each step 
    __________________
    Finally, the WINNER is who got the highest score.
"""


class Game:
    def __init__(self, p1, p2, p3, p4):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
        self.score1 = 0
        self.score2 = 0
        self.score3 = 0
        self.score4 = 0
        self.round = 1

    def play_round(self):
        while True:
            move1 = self.p1.human_move()
            if move1.lower() in moves:
                break
            else:
                print('Invalid. rock/paper/scissors? > ')
        move2 = self.p2.random_move()
        move3 = self.p3.reflect_move(move2)
        move4 = self.p4.cycle_move(move1)
        print(f'Player 1 : {move1} | Player 2 : {move2} | Player 3 : {move3} | Player 4 : {move4}')
        score1, score2 = get_score(move1, move2)
        score3, score4 = get_score(move3, move4)
        score_list = [score1, score2, score3, score4]

        move_list = [move1, move2, move3, move4]

        winner1 = winner_round(move1, move2)
        winner2 = winner_round(move3, move4)
        round_winner = winner_round(winner1, winner2)
        for i in range(len(move_list)):
            if move_list[i] == round_winner:
                score_list[i] += 1

        self.score1 += score_list[0]
        self.score2 += score_list[1]
        self.score3 += score_list[2]
        self.score4 += score_list[3]
        print(f'Score 1 : {score_list[0]} | Score 2 : {score_list[1]} | Score 3 : {score_list[2]} '
              f'| Score 4 : {score_list[3]}')
        print('==========================================================================')
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        self.p3.learn(move3, move4)
        self.p4.learn(move4, move3)

    def winner_game(self):
        new_score_list = [self.score1, self.score2, self.score3, self.score4]
        for i in range(4):
            if new_score_list[i] == max(new_score_list):
                print(f'The WINNER is : Player {i+1}')

    def play_game(self):
        print()
        print("Game start!".upper())
        print('==========================================================================')

        while True:
            print(f"Round {self.round}:")
            self.play_round()
            button = input('Continue or Q to quit? >')
            if button.upper() == 'Q':
                break
            self.round += 1

        print('==========================================================================')
        print(f'Player 1 : {self.score1} | Player 2 : {self.score2} | Player 3 : {self.score3}'
              f' | Player 4 : {self.score4}')
        self.winner_game()
        print("Game over!".upper())
        print('==========================================================================')


if __name__ == '__main__':
    game = Game(HumanPlayer(), RandomPlayer(), ReflectPlayer(), CyclePlayer())
    game.play_game()
