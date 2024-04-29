import unittest
from unittest.mock import patch, Mock
import mongodb
import datetime

# Unit test for MongoDB insertion
class TestMongoDBInsertion(unittest.TestCase):
    @patch('mongodb.collection.insert_one')  # Mock MongoDB insert function
    def test_save_to_mongodb_success(self, mock_insert_one):
        # Test data
        sensor_data = {
            "sensor_id": "sensor_22",
            "timestamp": datetime.datetime.utcnow(),
            "temperature": 21.5,
            "humidity": 40,
            "pressure": 1111,
        }
        # Simulate successful insertion
        mock_insert_one.return_value = Mock(inserted_id='12345')
        # Test the 'save_to_mongodb' function
        result = mongodb.save_to_mongodb(sensor_data)
        # Ensure insertion was successful
        self.assertTrue(result)
        mock_insert_one.assert_called_with(sensor_data)  # Validate data was inserted


if __name__ == "__main__":
    unittest.main()
