import unittest
from league_rankings import calculate_ranking_results, get_match_details

class TestLeagueRanking(unittest.TestCase):
    
   
    def test_basic_ranking(self):
        # Defining a list of match results for testing.
        matches = [
            "Lions 3, Snakes 3",
            "Tarantulas 1, FC Awesome 0",
            "Lions 1, FC Awesome 1",
            "Tarantulas 3, Snakes 1",
            "Lions 4, Grouches 0"
        ]

         # Defining the expected ranking output.
        expected_output = (
            "1. Tarantulas, 6 pts\n"
            "2. Lions, 5 pts\n"
            "3. FC Awesome, 1 pt\n"
            "3. Snakes, 1 pt\n"
            "5. Grouches, 0 pts"
        )
        
        # Assert that the calculated ranking matches the expected output.
        self.assertEqual(calculate_ranking_results(matches), expected_output)

    def test_tiebreaker_in_order(self):
        
        # Test ranking with all teams tied, ensuring alphabetical order.
        matches = [
            "TeamA 2, TeamB 2",
            "TeamC 1, TeamD 1"
        ]
        
        expected_output = (
            "1. TeamA, 1 pt\n"
            "1. TeamB, 1 pt\n"
            "1. TeamC, 1 pt\n"
            "1. TeamD, 1 pt"
        )
        
        self.assertEqual(calculate_ranking_results(matches), expected_output)

    def test_invalid_input(self):
        # Test handling of invalid input by checking for a ValueError.
        with self.assertRaises(ValueError):
            get_match_details("Invalid Data Here")
    
    def test_empty_input(self):
        # Test handling of empty input, expecting an empty result.
        self.assertEqual(calculate_ranking_results([]), "")

if __name__ == "__main__":
    unittest.main()