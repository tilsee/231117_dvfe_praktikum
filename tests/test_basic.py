import unittest
from unittest.mock import MagicMock, patch
import os
import sys

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Go one directory up
parent_dir = os.path.dirname(current_dir)

# Add the parent directory to the sys path
sys.path.append(parent_dir)

# Go into the formulaone folder
formulaone_dir = os.path.join(parent_dir, 'formulaone')
os.chdir(formulaone_dir)

# Now you can import from the formulaone package
from formulaone.db import get_resource

class TestDynamoResource(unittest.TestCase):
    @patch('db.get_resource')
    def test_get_resource(self, mock_get_resource):
        mock_get_resource.return_value = MagicMock()
        dynamo_resource = get_resource()
        self.assertIsNotNone(dynamo_resource)

    @patch('boto3.dynamodb.conditions.Key')
    @patch('db.get_resource')
    def test_query(self, mock_get_resource, mock_key):
        mock_table = MagicMock()
        mock_get_resource.return_value.Table.return_value = mock_table
        mock_key.return_value.eq.return_value = 'mock_condition'
        dynamo_resource = get_resource()
        movies = dynamo_resource.Table('doc-example-table-movies')
        movies.query(KeyConditionExpression=Key('year').eq(2013))
        mock_table.query.assert_called_with(KeyConditionExpression='mock_condition')

if __name__ == '__main__':
    unittest.main()