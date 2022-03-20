from typing import Dict

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
    admin_modes=int (input("1: To add languages, 2:update"))
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







def user():
    print("User optiuons")



user_prompt()
