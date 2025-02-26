import sys
from collections import defaultdict

def calculate_ranking_results(input_lines):
    # Use defaultdict to track team scores, initializing new teams with 0 points.
    scores = defaultdict(int)

    # Process each match line to extract team names and scores.
    for line in input_lines:
        team1, score1, team2, score2 = get_match_details(line)

        # Ensure both teams are in the scores dictionary.
        scores[team1] += 0
        scores[team2] += 0 

        # Update scores: 3 points for a win, 1 point each for a draw.
        if score1 > score2:
            scores[team1] += 3
        elif score1 < score2:
            scores[team2] += 3
        else:
            scores[team1] += 1
            scores[team2] += 1

    # Generate and return the final ranking by sorting teams based on their scores.
    return create_league_ranking(scores)


def get_match_details(match_line):
    # Split the match line into two parts: team1 score1, team2 score2.
    try:
        parts = match_line.strip().split(", ")

        # Validate that the line contains exactly two parts.
        if len(parts) != 2:
            raise ValueError(f"Invalid match format: {match_line}")
        
        team1, score1 = parts[0].rsplit(" ", 1)  # rsplit ensures splitting from the right

        # Split each part into team name and score.
        team2, score2 = parts[1].rsplit(" ", 1)

        # Return team names and scores as integers.
        return team1, int(score1), team2, int(score2)
    
    except ValueError as e:
        # Raise an error if the format is invalid or scores can't be converted.
        raise ValueError(f"Invalid match format: {match_line}") from e
    

def create_league_ranking(scores):
    # Sort teams by score (descending) and name (ascending).
    sorted_teams = sorted(scores.items(), key=lambda x: (-x[1], x[0]))
    output = []
    
    rank = 0
    prev_score = None
    # Assign ranks, handling ties (teams with the same score get the same rank).
    for i, (team, score) in enumerate(sorted_teams, start=1):
        if score != prev_score:
            rank = i    # Update rank if the score changes.

        # Format the ranking line (e.g., "1. TeamA, 3 pts").
        output.append(f"{rank}. {team}, {score} pt{'s' if score != 1 else ''}")
        prev_score = score

    # Join the formatted lines into a single string with newlines.
    return "\n".join(output)


def main():
    try:
        # Read input from a file (if provided) or stdin, splitting into lines.
        input_lines = open(sys.argv[1]).read().strip().split("\n") if len(sys.argv) > 1 else sys.stdin.read().strip().split("\n")
        
        # Calculate and print the ranking results.
        print(calculate_ranking_results(input_lines))
        
    except (IndexError, FileNotFoundError):
        # Handle missing file or invalid input source.
        print("Error: Please provide a valid input file or enter input through stdin.")
    except Exception as e:
        # Catch and display any unexpected errors.
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()