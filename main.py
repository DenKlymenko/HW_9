contact_dict = {'Tom': '89375983',
                'Michael': '674374983',
                }

def process(list_of_commands):
    #print(list_of_commands)
    if len(list_of_commands) == 1:
        if list_of_commands[0] == 'hello':
            print('How can I help you?')
        elif list_of_commands[0] == 'close' or list_of_commands[0] == 'exit':
            print('Good bye!')
            exit()
    elif len(list_of_commands) == 2:
        if list_of_commands[0] == 'good' and list_of_commands[1] == 'bye':
            print('Good bye!')
            exit()
        elif list_of_commands[0] == 'show' and list_of_commands[1] == 'all':
            for key, value in contact_dict.items():
                print(f'{key}: {value}')
        elif list_of_commands[0] == 'phone':
            print(contact_dict[list_of_commands[1]])
    elif len(list_of_commands) == 3:
        if list_of_commands[0] == 'add':
            contact_dict.update({list_of_commands[1]: list_of_commands[2]})
        elif list_of_commands[0] == 'change':
            contact_dict[list_of_commands[1]] = list_of_commands[2]

    else:
        print('I can\'t understand you')

def input_error(func):
    def validate_user_input():
        user_input = func()
        #print('input error', user_input)
        try:
            if user_input[0] == '':
                raise Exception('string cannot be empty')
            elif user_input[0] == 'add':
                if len(user_input) < 3:
                    raise Exception('operator add error: name or phone number were missed')
                elif len(user_input) > 3:
                    raise Exception('operator add error: too much args')
            elif user_input[0] == 'hello' and len(user_input) > 1:
                raise Exception('operator hello error: hello must be a single operator')
            elif user_input[0] == 'change':
                if len(user_input) < 3:
                    raise Exception('operator change error: name or phone number were missed')
                elif len(user_input) > 3:
                    raise Exception('operator change error: too much args')
            elif user_input[0] == 'phone':
                if len(user_input) < 2:
                    raise Exception('operator phone error: name was missed')
                elif len(user_input) > 2:
                    raise Exception('operator phone error: too much args')
            elif user_input[0] == 'show' and user_input[1] == 'all':
                #print('input error, show all')
                if len(user_input) > 2:
                    raise Exception('operator show all error: show all must be a single operator')

            #print('input error, False')
            process(user_input)

        except Exception as e:
            print(e)
            return True
        except KeyError:
            return True
        except ValueError:
            return True
        except IndexError:
            return True

    return validate_user_input

@input_error
def parcer():
    user_input = input('>>> ').split(' ')
    return user_input

def main():
    while True:
        parcer()

main()