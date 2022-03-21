from typing import Dict
import multilingual_greeter
lang_dict = {
      1: 'English',
      2: 'Kannada',
      3:'Hindi'

}

name_prompt_dict = {
      1:'What is your name?',
      2:'Nimma hesaru yenu?',
      3:'Aapka naam kya  hai?'
}

greetings_dict = {
    1:'Hello',
    2:'Namaskar',
    3:'Namaste'
}
def add_langauage(lang_options: Dict[int, str]) -> None:
    lang_options[4]='Kannada'
    for k, v in lang_options.items():
        print(f'{k}: {v}')


def update_greeting_existing_lang(greetings_options: Dict[int, str], lang_choice: int) -> Dict[int,str]:
    if lang_choice in greetings_options.keys():
     greetings_options.update({lang_choice:'Hola'})
    return greetings_options

def user_prompt():
    modes=int(input("Please enter 1:admin mode, 2:user mode"))
    if modes == 1:
        admin()
    elif modes ==2 :
        user()
    else :
        print("Please selct proper mode option")
def admin():
    admin_modes=int (input("1: Add  additional languages 2:Update greetings for existing languages"))
    if admin_modes == 1:
        lang_add=input("please enter thr lang to add")#kannaa
        ask_name_phrase=input("please enter what is your name  phrase in that langa") #nimm
        ask_greeting=input("please the greeting in that langusage like Hello") # namaskar

        lang_add={len(lang_dict)+1:lang_add}
        ask_name_add={len(name_prompt_dict)+1:ask_name_phrase}
        ask_greet_add={len(greetings_dict)+1:ask_greeting}

        lang_dict.update(lang_add)
        name_prompt_dict.update(ask_name_add)
        greetings_dict.update(ask_greet_add)
    elif admin_modes ==2:
        for k,v in greetings_dict.items():
            print(f'{k} : {v}')
        greet_key=int(input("Which greeting you would like update?, select key number")) #
        if greetings_dict.get(greet_key) :
            updated_greet=input("Enter the updated greeting") # dhanyaagaoin
            greetings_dict.update({greet_key:updated_greet})
        else :
            print("You entered wrong key")
        for k, v in greetings_dict.items():
            print(f'{k} : {v}')









def user():
    multilingual_greeter.print_language_options(lang_dict)
    lang_num=multilingual_greeter.language_input()
    while multilingual_greeter.language_choice_is_valid(lang_dict,lang_num) is False:
        print("You have enterred wrong selection, try again")
        lang_num = multilingual_greeter.language_input()

    name_lang=multilingual_greeter.get_name_input(name_prompt_dict, lang_num)
    name=multilingual_greeter.name_input(name_lang)
    multilingual_greeter.greet(name,greetings_dict,lang_num)






user_prompt()
