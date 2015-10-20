print
print "###########################################################"
print "### Is your integer increasing, decreasing, or neither? ###"
print "###########################################################"
print

increasing = "--> Your integer is increasing.\n"
decreasing = "--> Your integer is decreasing.\n"
neither = "--> Your integer is neither increasing nor decreasing.\n"
error = "--> You did not enter a valid integer. Please try again.\n"

while True:
    user_input = raw_input("Please enter an integer: ")
    if user_input.lower() == "end":
        print "\n=== SESSION TERMINATED ===\n"
        break
    else:
        try:
            user_input = abs(int(user_input)) #Attempts to convert user_input into a positive int
        except ValueError: #Displays an error if user_input can't be converted into a positive int
            print error
            continue

    flag = 0
    old_flag = 0

    while flag == old_flag:

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
        print increasing
    elif flag == 2 and old_flag == 2:
        print decreasing
    else:
        print neither
