import sys
from collections import defaultdict

def process_results(input_lines):
    scores = defaultdict(int)
    
    for line in input_lines:
        team1, score1, team2, score2 = get_match_details(line)
        
        scores[team1] += 3 if score1 > score2 else 1 if score1 == score2 else 0
        scores[team2] += 3 if score2 > score1 else 1 if score1 == score2 else 0
    
    return calculate_ranking(scores)


def get_match_details(match_line):
    try:
        parts = match_line.rsplit(", ", 1)
        team1, score1 = parts[0].rsplit(" ", 1)
        team2, score2 = parts[1].rsplit(" ", 1)
        return team1, int(score1), team2, int(score2)
    except ValueError:
        raise ValueError(f"Invalid match format: {match_line}")


def calculate_ranking(scores):
    sorted_teams = sorted(scores.items(), key=lambda x: (-x[1], x[0]))
    output = []
    
    rank = 0
    prev_score = None
    for i, (team, score) in enumerate(sorted_teams, start=1):
        rank = i if score != prev_score else rank
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