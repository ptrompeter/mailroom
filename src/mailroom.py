# _*_ coding: utf-8 _*_

import operator
import pdb

SAMPLE_DATA = {('Roberts', 'John'): [20.00, 15.00],
        ('Edwards', 'Mary'): [5.00, 30.50],
        ('asdf', 'brice'): [2.35],
        }

USR_REQUESTS = {
    'name': "Please enter full name, first name first, or type 'list': ",
    'amount': "Please enter donation amount: ",
    'menu': "Enter 1 to send a thank you or 2 to print a report: ",
    }

#USER INPUT FUNCTION

def get_prompt(prompt, function):
    """Accept user input subject to validation."""
    user_input = None
    while user_input == None:
        user_input = function(input(prompt))
    return user_input

#VALIDATORSa
def donation_check(user_input):
    """Reject non-numbers."""
    try: 
        float(user_input)
        return float(user_input)
    except ValueError:
        print('Sorry, please enter a number')   

def menu_check(user_input):
    """Reject strings other than 1, 2, q, or quit"""
    if user_input == '1' or user_input == '2' or user_input == 'q' or user_input == 'quit':
        return user_input
    else:
        print('Sorry, invalid selection')

def name_check(user_input):
    """Reject name with numeric characters."""
    for index in user_input:
        if index.isnumeric():
            print("Names cannot contain numbers.")
            return None
    return user_input 


#CONTROL FUNCTION
def main(data):
    """Manage general program flow through function calls"""
    selection = menu_prompt(get_prompt(USR_REQUESTS['menu'], menu_check))
    if selection == 'quit' or selection == 'q':
        return 'done'
    if selection == '1':
        name = get_name(get_prompt(USR_REQUESTS['name'], name_check))
        while name == 'list':
            name_list(data)
            name = get_name(get_prompt(USR_REQUESTS['name'], name_check))
        donation = get_donation(get_prompt(USR_REQUESTS['amount'], donation_check))
        update_data(name, donation, data)
        write_email(name, donation)
        main(data)

    elif selection == '2':
        generate_report(sort_by_donation(data), data)

    else:
        print("invalid selection")
        main(data)

#FUNCTIONS RUN BY MAIN
def menu_prompt(prompt):
    """Display menu prompt and accept selection"""
    user_input = prompt
    return user_input


def get_name(name):
    """Return a full name entered by user."""
    user_input = name
    if user_input == 'list':
        return user_input
    else:
        name = (user_input.split()[-1], user_input.split()[0],)
        return name


def get_donation(string_of_num):
    """Return a float based on user input."""
    donation = string_of_num
    return float(donation)


def update_data(name, amount, data):
    """Finds and updates or creates entry in data based on user input."""
    data.setdefault(name, []).append(amount)


def write_email(name, amount):
    print("Dear {} {}, thank you for your generous donation of {} dollars.  We are grateful for your continued support.  The mailroom.".format(name[1], name[0], amount))


def name_list(data):
    """Print a list of donors and re-run main."""
    for key in data:
        print(("{0}, {1}".format(key[0], key[1])))
    main(data)


def sort_by_donation(data):
    """Create a dictionary with summed donation and return a list sorted by donation."""
    sum_dict = {}
    for key in data:
        sum_dict[key] = sum(data[key])
    sorted_list = sorted(sum_dict.items(), key=operator.itemgetter(1))
    return sorted_list


def generate_report(sorted_list, data):
    """Prints a report of all names, summed donations, number of donations, and average donations"""
    print('{:<20} {:<10} {:<15} {:<10}'.format('Name', 'Total', 'No. Donations', 'Average'))
    for index in sorted_list:
        name = index[0]
        string_name = index[0][0] + ", " + index[0][1]
        total = index[1]
        num = len(data[name])
        avg = total / num
        print("{:<20} {:<10} {:<15} {:<10}".format(string_name, total, num, avg))
    main(data)


if __name__ == '__main__':
    main(SAMPLE_DATA)
