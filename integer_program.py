print
print "###########################################################"
print "### Is your integer increasing, decreasing, or neither? ###"
print "###########################################################"
print

flag = 0
flag_list = []

def all_same(items):
    return all(x == items[0] for x in items)

#Check user input
while True:
    user_input = raw_input("Please enter an integer: ")

    if user_input.lower() == "end":
        print "\n=== SESSION TERMINATED ===\n"
        break
    else:
        try:
            cleaned_user_input = abs(int(user_input))
        except ValueError:
            print "--> You did not enter a valid integer. Please try again.\n"
            continue

    #Compare values that comprise the integer, assign flag, and add flag to flag_list
    while (cleaned_user_input > 0):
        d1 = cleaned_user_input % 10
        cleaned_user_input /= 10
        d2 = int(cleaned_user_input % 10)

        if d1 > d2:
            flag = 1
        elif d1 < d2:
            flag = 2
        else:
            flag = 3

        flag_list.append(flag)

    #Remove the last item in flag_list to avoid off-by-one error
    flag_list.pop()

    #Print appropriate statement
    if all_same(flag_list):
        if flag_list[0] == 1:
            print "--> Your integer is increasing.\n"
        elif flag_list[0] == 2:
            print "--> Your integer is decreasing.\n"
        else:
            print "--> Your integer is neither increasing nor decreasing.\n"
    else:
        print "--> Your integer is neither increasing nor decreasing.\n"

    #Clear flag_list
    del flag_list[:]
