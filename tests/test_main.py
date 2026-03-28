import unittest
from unittest.mock import MagicMock
from unittest.mock import patch
from main import get_ai_response
from main import parse_args


class TestParseArgs(unittest.TestCase):
    def test_basic_prompt(self):
        with patch("sys.argv", ["main.py", "hello world"]):
            args = parse_args()
            self.assertEqual(args.user_prompt, "hello world")
            self.assertFalse(args.verbose)

    def test_verbose_flag(self):
        with patch("sys.argv", ["main.py", "hello world", "--verbose"]):
            args = parse_args()
            self.assertEqual(args.user_prompt, "hello world")
            self.assertTrue(args.verbose)

    def test_missing_prompt_exits(self):
        with patch("sys.argv", ["main.py"]):
            with self.assertRaises(SystemExit):
                parse_args()


class TestAI(unittest.TestCase):
    def test_get_ai_response(self):
        mock_response = MagicMock()
        mock_response.text = "Helo, I am fake AI."
        mock_response.usage_metadata.prompt_token_count = 5
        mock_response.usage_metadata.candidates_token_count = 10

        mock_client = MagicMock()
        mock_client.models.generate_content.return_value = mock_response

        prompt = "Who are you?"
        result = get_ai_response(mock_client, prompt)

        self.assertEqual(result.text, "Helo, I am fake AI.")
        self.assertEqual(result.usage_metadata.prompt_token_count, 5)

        call_args = mock_client.models.generate_content.call_args
        self.assertEqual(call_args.kwargs["model"], "gemini-2.5-flash")
        self.assertEqual(call_args.kwargs["contents"], prompt)

if __name__ == "__main__":
    unittest.main()