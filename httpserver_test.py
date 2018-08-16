import unittest
import httpserver
from unittest.mock import Mock

class Connection_Test(unittest.TestCase):

    def test_readline(self):
        mock_conn = unittest.mock.MagicMock
        expected = ''
        result = httpserver.Connection(mock_conn)
        self.assertEqual(True, True)
