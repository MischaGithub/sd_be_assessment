import sys
from collections import defaultdict

def process_results(input_lines):
    scores = defaultdict(int)
    
    for line in input_lines:
        team1, score1, team2, score2 = get_match_details(line)
        
        # Ensure both teams are in the scores dictionary, even if they have 0 points
        scores[team1] += 0
        scores[team2] += 0
        
        if score1 > score2:
            scores[team1] += 3
        elif score1 < score2:
            scores[team2] += 3
        else:
            scores[team1] += 1
            scores[team2] += 1
    
    return generate_ranking(scores)


def get_match_details(match_line):
    # Remove any leading/trailing whitespace and split the line by ", " to separate team-score pairs
    try:
        parts = match_line.strip().split(", ")

        # Check if the line contains exactly two parts (team1 score1, team2 score2)
        if len(parts) != 2:
            raise ValueError(f"Invalid match format: {match_line}")

        # Split the first part (team1 score1) into team name and score
        
        team1, score1 = parts[0].rsplit(" ", 1)  # rsplit ensures splitting from the right

        # Split the second part (team2 score2) into team name and score
        team2, score2 = parts[1].rsplit(" ", 1)

        # Return the extracted details, converting scores from strings to integers
        return team1, int(score1), team2, int(score2)
    
    except ValueError as e:
        # If any error occurs (e.g., invalid format or score conversion), raise a descriptive error
        raise ValueError(f"Invalid match format: {match_line}") from e
    

def generate_ranking(scores):
    sorted_teams = sorted(scores.items(), key=lambda x: (-x[1], x[0]))
    output = []
    
    rank = 0
    prev_score = None
    for i, (team, score) in enumerate(sorted_teams, start=1):
        if score != prev_score:
            rank = i
        output.append(f"{rank}. {team}, {score} pt{'s' if score != 1 else ''}")
        prev_score = score
    
    return "\n".join(output)


def main():
    try:
        input_lines = open(sys.argv[1]).read().strip().split("\n") if len(sys.argv) > 1 else sys.stdin.read().strip().split("\n")
        print(process_results(input_lines))
    except (IndexError, FileNotFoundError):
        print("Error: Please provide a valid input file or enter input through stdin.")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()