
import unittest
from src.data_preprocessing import preprocess_data  # Adjust this based on actual module

class TestPreprocessing(unittest.TestCase):
    def test_preprocess_data(self):
        sample_data = {
            "tenure": [1, 2],
            "MonthlyCharges": [29.85, 56.95],
            "Contract": ["Month-to-month", "One year"]
        }
        # This should be replaced with an actual DataFrame and expected behavior
        # df = pd.DataFrame(sample_data)
        # processed = preprocess_data(df)
        # self.assertIsNotNone(processed)

if __name__ == "__main__":
    unittest.main()
