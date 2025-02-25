import unittest
from league_ranking import process_results, get_match_details

class TestLeagueRanking(unittest.TestCase):
    def test_basic_ranking(self):
        matches = [
            "Liverpool 3, Madrid 3",
            "Aston Villa 1, Man Utd 0",
            "Liverpool 1, Man Utd 1",
            "Aston Villa 3, Madrid 1",
            "Liverpool 4, Man City 0"
        ]
        expected_output = (
            "1. Liverpool, 7 pts\n"
            "2. Aston Villa, 6 pts\n"
            "3. Madrid, 4 pts\n"
            "4. Man Utd, 1 pt\n"
            "5. Man City, 0 pts"
        )
        self.assertEqual(process_results(matches), expected_output)
    

def test_invalid_input(self):
        with self.assertRaises(ValueError):
            get_match_details("Invalid Data Here")
    
def test_empty_input(self):
        self.assertEqual(process_results([]), "")
        

if __name__ == "__main__":
    unittest.main()