print
print "###########################################################"
print "### Is your integer increasing, decreasing, or neither? ###"
print "###########################################################"
print

increasing = "--> Your integer is increasing."
decreasing = "--> Your integer is decreasing."
neither = "--> Your integer is neither increasing nor decreasing."
error = "--> You did not enter a valid integer. Please try again."

history_user_input = []
history_classification = []

while True:
    user_input = raw_input("\nPlease enter an integer: ")
    if user_input.lower() == "end":
        print "\n=== SESSION TERMINATED ===\n"
        break
    elif user_input.lower() == "history":
        if history_user_input == [] or history_classification == []:
            print "--> There is no history."
        else:
            for i, j in zip(history_user_input, history_classification):
                print i, j
    else:
        try:
            user_input = abs(int(user_input)) #Attempts to convert user_input into a positive int
            history_user_input.append(user_input)
        except ValueError: #Displays an error if user_input can't be converted into a positive int
            print error
            continue

    flag = 0
    old_flag = 0

    while flag == old_flag and user_input != "history":

        first_num = user_input % 10
        user_input /= 10
        if user_input < 1: #If user_input / 10 is less than 1, the program exits the loop; this prevents an off-by-one error
            break
        second_num = user_input % 10

        #Compares the numbers that comprise the integer and assigns an appropriate flag
        if first_num > second_num:
            flag = 1
        elif second_num > first_num:
            flag = 2
        else:
            flag = 3

        if flag != old_flag and old_flag != 0: #If flag and old_flag are not equal, the integer is neither increasing nor decreasing so the program exits the loop
            break
        else:
            old_flag = flag

    #Prints appropriate statement given flag
    if flag == 1 and old_flag == 1:
        history_classification.append(increasing)
        print increasing
    elif flag == 2 and old_flag == 2:
        history_classification.append(decreasing)
        print decreasing
    else:
        if user_input == "history":
            continue
        else:
            history_classification.append(neither)
            print neither
