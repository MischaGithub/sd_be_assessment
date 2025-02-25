import sys
from collections import defaultdict

def process_results(input_lines):
    scores = defaultdict(int)
    
    for line in input_lines:
        team1, score1, team2, score2 = get_match_details(line)
        
        scores[team1] += 3 if score1 > score2 else 1 if score1 == score2 else 0
        scores[team2] += 3 if score2 > score1 else 1 if score1 == score2 else 0
    
    return calculate_ranking(scores)


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