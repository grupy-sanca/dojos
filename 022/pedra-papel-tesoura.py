"""
https://www.codewars.com/kata/5672a98bdbdd995fad00000f/python
rps('scissors','paper') // Player 1 won!
rps('scissors','rock') // Player 2 won!
rps('paper','paper') // Draw!


>>> rps('scissors','paper')
Player 1 won!
>>> rps('scissors','rock')
Player 2 won!
>>> rps('paper','paper')
Draw!
>>> rps('rock','rock')
Draw!
>>> rps('paper','scissors')
Player 2 won!
>>> rps('paper', 'rock')
Player 1 won!
>>> rps('rock', 'paper')
Player 2 won!
>>> rps('scissors','scissors')
Draw!
>>> rps('rock', 'scissors')
Player 1 won!
"""

def rps(player1, player2):
    if player1 == player2:
        print('Draw!')
    elif player1 == 'scissors' and player2 == 'rock':
        print('Player 2 won!')
    elif player1 == 'paper' and player2 == 'scissors':
        print('Player 2 won!')
    elif player1 == 'rock' and player2 == 'paper':
        print('Player 2 won!')
    else:
        print('Player 1 won!')
