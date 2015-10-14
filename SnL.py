__author__ = 'rfischer'
__author__ = 'rfischer'
# Enter your code here. Read input from STDIN. Print output to STDOUT
_board = []
_rolls = 0
_location = 0
_least_rolls = 50
_path_stack = []


class stackInfo:
    rolls = 0
    location = 0

    def __init__(self, theRolls, theLocation):
        rolls = theRolls
        location = theLocation

def followPath(theLocation, theRolls):
    global _least_rolls

    location = theLocation
    rolls = theRolls
    moves = 0
    while 1:
        # Somehow check for loops and break
        # For now this is only handled by the break when the rolls gets too large

        # Check for end or link before increasing any value

        # Reached end location, see if it is good
        if location == 100:
            if rolls < _least_rolls:
                _least_rolls = rolls+1 if moves else rolls
            return
        if _board[location]:
            for link in _board[location]:
                # If sliding immediately along another snake/ladder don't increase rolls
                followPath(link, rolls+1 if moves else rolls)

        location += 1
        moves += 1

        # If number of locations moved is > 6, need to increment roll
        if moves >= 6:
            moves = 0
            rolls += 1

        # Don't bother checking this path anymore, it is already at least as long as
        # the minimum
        if rolls >= _least_rolls:
            return
    return

T = input()
for i in range(0, T):
    _board = [None] * 100
    S, L = [int(n) for n in raw_input().split(',')]
    ladders = tuple(x for x in raw_input().split(' '))
    snakes = tuple(x for x in raw_input().split(' '))

    # Add the snake pointers
    for snake in snakes:
        a,b = [int(n) for n in snake.split(',')]
        if not _board[a]:
            _board[a] = []
        _board[a].append(b)

    # Add the ladder pointers
    for ladder in ladders:
        a,b = [int(n) for n in ladder.split(',')]
        if not _board[a]:
            _board[a] = []
        _board[a].append(b)

    #print _board

    _least_rolls = 50
    followPath(0, 0)

    print _least_rolls