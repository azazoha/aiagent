import unittest
from unittest.mock import MagicMock
from main import get_ai_response

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