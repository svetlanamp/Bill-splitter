print("Enter the number of friends joining (including you):")
number_of_people = int(input())
name_list = []
if number_of_people <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    for _ in range(number_of_people):
        name = input()
        name_list.append(name)
    name_dict = dict.fromkeys(name_list, 0)
    print("Enter the total bill value:")
    total_bill = int(input())
    pay_each = round((total_bill / number_of_people), 2)
    
    name_dict = dict.fromkeys(name_list, pay_each)   

    # if the user wants to use "Who is lucky" feature - pick one name from the dictionary at random; this person's share will be paid by others.
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    answer = input() 
    if answer == "No":
        print("No one is going to be lucky")
        print(name_dict)
    elif answer == "Yes":
        import random
        lucky = random.choice(name_list)
        print(f"{lucky} is the lucky one!")
        pay_each_new = round((total_bill / (number_of_people - 1)), 2)
        name_dict_new = dict.fromkeys(name_list, pay_each_new)
        name_dict_new[lucky] = 0
        print(name_dict_new) 