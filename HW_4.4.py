from pathlib import Path
import math

def find_dictionary_by_name(phone_info:list , target_name:str):   
    for dictionary in phone_info:
        if "name" in dictionary and dictionary["name"] == target_name:
            return dictionary
    return None

def get_phones_info(file_path:Path):
    try:
        user_dict= {}
        phones_list=[]
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                try:
                    line = line.strip()
                    user_str = line.split(",")
                    user_dict = {
                        'name': user_str[0],
                        'phone': user_str[1].strip()
                        }
                    phones_list.append(user_dict)
                except Exception as ex:
                    print(f"mistake in data structure: {ex}, line: {line}")
    except FileNotFoundError as ex:
        print(f"{ex}")
    return phones_list

def save_to_file(phones_info:list, file_path:Path):
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            for dictionary in phones_info:
                file.write(f"{dictionary.get("name")},{dictionary.get("phone")}\n")
    except Exception as ex:
        print(f"{ex}")

def add_contact(phones_info:list,name_to_add:str, phone_to_add:str)->str:
    try:
        phones_info.append({"name": name_to_add, "phone": phone_to_add})
        message = "data added"
    except Exception as ex:
        print(f"{ex}")
        message = ex
    return message

def change_contact(phones_info:list,name_to_change:str,new_phone:str)->str:
    dict_to_change = {}
    dict_to_change = find_dictionary_by_name(phones_info,name_to_change)
    if dict_to_change != None:
        dict_to_change.update({'name': name_to_change, 'phone': new_phone})
        message = f"data updated! name:{dict_to_change.get("name")}, phone:{dict_to_change.get("phone")}"
    else:    
        message = "No such name in a list"
    return message

def show_phone(phones_info:list, name_to_find:str)->str:
    dict_to_find = find_dictionary_by_name(phones_info,name_to_find)
    if dict_to_find != None:
        message = f"Phone number of {dict_to_find.get("name")} is {dict_to_find.get("phone")}"
    else:    
        message = "No such name in a list"
    return message

def show_all(phones_info:list):
    symbol = " "
    i = 1
    print(" №  |          name          |         phone")
    for line in phones_info:
        move_name = math.trunc(12-len(line["name"])/2)
        move_name_right = move_name if (len(line["name"]) % 2) == 0  else move_name+1
        move_phone = math.trunc(12-len(line["phone"])/2)
        print(f" {i}{symbol*math.trunc(3-len(str(i))/2)}|{symbol*move_name}{line["name"]}{symbol*(move_name_right)}|{symbol*move_phone}{line["phone"]}")
        i+=1

def parse_input(user_input):
    cmd, *args = user_input.split('-')
    cmd = cmd.strip().lower()
    args = [arg.strip() for arg in args]
    return cmd, args

def main():
    file_path = Path("phones.txt")
    phones_info = get_phones_info(file_path)
    
    print("Welcome to the assistant bot!")
    while True:
        message = ""
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input) 
        command = command.lower()
       
        match command:
            case "close"|"exit":
                print("Good bye!")
                break
            
            case "hello":
                print("How can I help you?")
            
            case "add"|"add contact":
                message = add_contact(phones_info, args[0],args[1])

            case "change contact"|"change":
                message = change_contact(phones_info, args[0],args[1])
                
            case "show contacts"|"all":
                show_all(phones_info)

            case "show phone"|"phone":
                message = show_phone(phones_info, args[0])

            case "save to file"|"save":
                save_to_file(phones_info,file_path)

            case "help"|"?"|"/?":
                print("""available command of bot is:  
                      "hello" - to say hello to bot   
                      "close" or "exit" - to stop bot
                      commands for contacts: 
                          "add contact" or "add" with arguments "-Name" and "-Phone" will add contact to database (DB). for example add -NewName -NewPhone
                          "change contact" or "change" with arguments "-Name" and "-Phone" will change contact in DB
                          "show contacts" or "all" - to show all contacts in DB
                          "show phone" or "phone" - with argument "-Name" will show the phone of contact
                          "save to file" or "save" - save names and phones to file
                    """)
            case _:
                print("Invalid command. is you need assistance please enter: help")

        if len(message)>0: print(message)

if __name__ == "__main__":
    main()
