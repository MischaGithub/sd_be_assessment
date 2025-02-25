import unittest
from league_ranking import process_results, get_match_details

def test_invalid_input(self):
        with self.assertRaises(ValueError):
            get_match_details("Invalid Data Here")
    
def test_empty_input(self):
        self.assertEqual(process_results([]), "")
        

if __name__ == "__main__":
    unittest.main()