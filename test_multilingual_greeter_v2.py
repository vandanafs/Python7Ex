from unittest import TestCase
from unittest.mock import patch
from io import StringIO
import multilingual_greeter_v2

class MultilinualGreeterUpdateAdd(TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_add_language(self,stdout_mock):
        languages = {
            1: "English",
            2: "Spanish",
            3: "Portuguese"
        }

        expected = "Please choose a language: \n" \
                   "1: English\n" \
                   "2: Spanish\n" \
                   "3: Portuguese\n" \
                   "4: Kannada \n"

        multilingual_greeter_v2.add_langauage(languages)
        self.assertEqual(expected,stdout_mock.getvalue())
