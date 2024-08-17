'''
You are given a list of dictionaries matches where each element of the list would correspond to a match result. Each match result contains the team involved, the winner, and the goals scored by the winner team. One of the entry is given below for your reference:

```
{'team1': 'Brazil', 'team2': 'Argentina', 'goals1': 2, 'goals2': 1}
```
Define a function named `get_leaderboard` that takes matches as input and returns the leaderboard.

Teams are sorted by their total points. Points are awarded as follows:
Win: 2 pts.
Draw: 1 pt.
Loss: 0 pts.

If the teams have the same points, then they should be sorted on the basis of the number of goals scored.

NOTE
* `goals1`: This variable holds the number of goals scored by team1.
* `goals2`: This variable holds the number of goals scored by team2.


SAMPLE INPUT
matches = [
    {"team1": "Brazil", "team2": "Argentina", "goals1": 2, "goals2": 1},
    {"team1": "Germany", "team2": "France", "goals1": 1, "goals2": 2},
    {"team1": "Brazil", "team2": "Germany", "goals1": 3, "goals2": 2},
    {"team1": "Argentina", "team2": "France", "goals1": 1, "goals2": 1},
    {"team1": "Brazil", "team2": "France", "goals1": 1, "goals2": 0},
    {"team1": "Argentina", "team2": "Germany", "goals1": 2, "goals2": 0},
    {"team1": "Germany", "team2": "France", "goals1": 0, "goals2": 1}
]

OUPTPUT: list of tuple(TeamName, Points, GoalScored)
Output : [('Brazil', 6, 6), ('France', 5, 4), ('Argentina', 3, 4), ('Germany', 0, 3)]
'''

def get_leaderboard(matches: list) -> list:
    """
    Given a list of dictionaries, generate a leaderboard based on points and goal scored.
    The output should be a list of tuples starting from the top team to bottom one.
    
    Args:
    matches : list[dict]
    
    Returns:
    list of tuples - where each entry should be in format: (TeamName, Points, GoalScored)
    sorted from top team to bottom.
    """
    ...
