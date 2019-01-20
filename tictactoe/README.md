# Tic Tac Toe Challenge

## Setup and run:
    pip install -U .
    python tictactoe/app.py

## Playing
Create a game:
```
requests.post('http://localhost:5000/api/games', headers={'content-type': 'application/json'}, data=json.dumps({'player1': 'foo', 'player2': 'bar'}))
```

Which returns you back a newly created game with an ID and who will go first:

```
 {'id': 31,
 'circle': 'bar',
 'cross': 'foo',
 'board': [[None, None, None], [None, None, None], [None, None, None]],
 'next_turn': 'cross',
 'closed': False,
 'winner': None}
```

You can then post to make your move. Game spaces are ordered by passing a coordinate value. Coordinates for the board:
```
(0, 0) | (0, 1) | (0, 2)
------------------------
(1, 0) | (1, 1) | (1, 2)
------------------------
(2, 0) | (2, 1) | (2, 2)
```

```
requests.post('http://localhost:5000/api/games/31', headers={'content-type': 'application/json'}, data=json.dumps({'player': 'foo', 'x': 2, 'y': 1})); resp.status_code, resp.json()
```

Which will return you the game state:

```
 {'id': 31,
  'circle': 'bar',
  'cross': 'foo',
  'board': [[None, None, None], [None, None, None], [None, 1, None]],
  'next_turn': 'circle',
  'closed': False,
  'winner': None}
```
