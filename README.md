# League Ranking CLI App

## What This Does
This is a simple command-line app that takes football match results and creates a ranking table based on points:
- Win = 3 points
- Draw = 1 point
- Loss = 0 points

Teams with more points are ranked higher. If teams have the same points, they are sorted alphabetically.

## How to Run
### Prerequisites:
- Install Python 3.x

### Steps:
1. Download or clone this project.
2. Open a terminal and go to the project folder.

Run the script in two ways:

1. **Using a file:**
   ```sh
   python league_ranking.py input.txt
   ```
   Example `input.txt`:
   ```
   Lions 3, Snakes 3
   Tarantulas 1, FC Awesome 0
   Lions 1, FC Awesome 1
   Tarantulas 3, Snakes 1
   Lions 4, Grouches 0
   ```

2. **Manually enter data:**
   ```sh
   python league_ranking.py
   ```
   Then type the match results and press `Ctrl+D` (Linux/Mac) or `Ctrl+Z` (Windows) when done.

## Running Tests
To check if everything works, run:
```sh
python -m unittest test_league_rankings.py
```

## Expected Output
Example:
```
1. Tarantulas, 6 pts
2. Lions, 5 pts
3. FC Awesome, 1 pt
3. Snakes, 1 pt
5. Grouches, 0 pts
```


