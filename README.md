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

Run the script in two ways:

1. **Using a file:**
   ```sh
   python league_ranking.py input.txt
   ```
   Example `input.txt`:
   ```
   Liverpool 3, Madrid 3
   Aston Villa 1, Man Utd 0
   Liverpool 1, Man Utd 1
   Aston Villa 3, Madrid 1
   Liverpool 4, Man City 0
   ```

2. **Manually enter data:**
   ```sh
   python league_ranking.py
   ```
   Then type the match results and press `Ctrl+D` (Linux/Mac) or `Ctrl+Z` (Windows) when done.

## Running Tests
To check if everything works, run:
```sh
python -m unittest test_league_ranking.py
```

## Expected Output
Example:
```
1. Liverpool, 7 pts
2. Aston Villa, 6 pts
3. Madrid, 4 pts
4. Man Utd, 1 pt
5. Man City, 0 pts
```

## Notes
- This is a simple project to learn how to handle input, sorting, and ranking.
- Feel free to improve it!
