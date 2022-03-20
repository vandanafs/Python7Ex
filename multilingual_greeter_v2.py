from typing import Dict
def add_langauage(lang_options: Dict[int, str]) -> None:
    lang_options[4]='Kannada'

def update_greeting_existing_lang(greetings_options: Dict[int, str], lang_choice: int) ->None :
    greetings_options.update(lang_choice,'Hola')