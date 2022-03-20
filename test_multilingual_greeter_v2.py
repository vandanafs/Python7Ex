from unittest import TestCase
from unittest.mock import patch
from io import StringIO
import multilingual_greeter_v2
from io import StringIO
class MultilinualGreeterUpdateAdd(TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_add_language(self,stdout_mock):
        languages = {
            1: "English",
            2: "Spanish",
            3: "Portuguese"
        }

        #expected = "Please choose a language: \n" \
        expected = "1: English\n" \
                   "2: Spanish\n" \
                   "3: Portuguese\n" \
                   "4: Kannada\n"


        multilingual_greeter_v2.add_langauage(languages)
        self.assertEqual(expected, stdout_mock.getvalue())


    #@patch('sys.stdout', new_callable=StringIO)
    def test_update_existing_lang_greeting(self):
        greetings_dict = {
            1: 'Hello',
            2: 'Namaskar',
            3: 'Namaste'
        }

        expected=" 1: Hello\n"\
                 "2: Hola\n"\
                 "3: Namaste\n"
        actual={}
        actual= multilingual_greeter_v2.update_greeting_existing_lang(greetings_dict,2)
        for k,v in actual.items():
            print(f'{k}:{v}')


