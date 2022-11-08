from unittest import mock, TestCase

from e import fs

class TestExamples(TestCase):
    @mock.patch('e.fs.check_output', return_value=b' foo\nbar\n')
    def test_print_contents_of_cwd_success(self, mock_check_output):
        actual_result: list[bytes] = fs.print_contents_of_cwd()

        expected_directory = b'foo'
        self.assertIn(expected_directory, actual_result)