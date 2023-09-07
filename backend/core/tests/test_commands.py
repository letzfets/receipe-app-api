"""
Test custom Django management commands
"""
# mock behavior of database:
from unittest.mock import patch

# OperationalError is thrown when the database connection is not available:
from psycopg2 import OperationalError as Psycopg2Error


# importing tha actual function to be tested:
from django.core.management import call_command

# another Error, thrown when database connection is ready,
# but database is not created yet:
from django.db.utils import OperationalError

# Use SimpleTestCase instead of TestCase because
# we don't need a database and its content for this test:
from django.test import SimpleTestCase


# this is the command for mocking the database errors:
@patch("core.management.commands.wait_for_db.Command.check")
# Code for testing:
class CommandTest(SimpleTestCase):
    """Test commands"""

    def test_wait_for_db_ready(self, patched_check):
        """Test waiting for db when db is available"""
        # mocking the database is ready response:
        patched_check.return_value = True

        # actually calling the function to be tested:
        call_command("wait_for_db")

        # checking if the function was called once with the correct database:
        patched_check.assert_called_once_with(databases=["default"])

    # check database -> wait a few seconds -> check again
    # but in test, we don't want to wait - for not slowing the test down
    @patch("time.sleep")
    def test_wait_for_db_delay(self, patched_sleep, patched_check):
        """Test waiting for db when getting OperationalError"""
        # side effect allows to pass in an exception:
        # first 2 times Psychopg2 Error and then 3 times OperationalError
        # due to different stages of database initialization
        # typically Psychopg2 Error is thrown when connection not ready
        # and OperationalError is thrown when database not ready
        # 2 and 3 are arbitrary numbers
        # 6 time True is returned
        patched_check.side_effect = (
            [Psycopg2Error] * 2 + [OperationalError] * 3 + [True]
        )

        # actually calling the function to be tested:
        call_command("wait_for_db")

        # after calling the database 6 times it should be ready:
        self.assertEqual(patched_check.call_count, 6)

        # checking if the function was called with the correct database
        # but now its called multiple (6) times:
        patched_check.assert_called_with(databases=["default"])
