#helpers are pulled from the python-exercises repo for ease of use
def handle_commas(comma_num):
    # the string that will be converted to the output
    ret_str = ""
    # the flag that tracks the decimal place
    dec_point_flag = False
    for c in comma_num:
        #check if c is a decimal place and that one has not already appeared in the string
        if c == '.' and not dec_point_flag:
            #set the flag to true to indicate a decimal place has been added
            dec_point_flag = True
            #adds the character to the string
            ret_str += c
        #checks if the character is a digit and, if it is, adds it to the string
        elif c.isdigit():
            ret_str += c
        # if the character is a comma, skip over it
        elif c == ',':
            continue
        else:
            #throws an error if the number isn't valid
            raise ValueError("Not a valid number")
    # if the number contains a decimal point, returns it as a float
    if dec_point_flag:
        return float(ret_str)
    # otherwise returns it as an int
    else:
        return int(ret_str)

def get_letter_grade(score):
    if score >= 90:
        return 'A'
    elif score >=80:
        return 'B'
    elif score >=70:
        return 'C'
    elif score >=60:
        return 'D'
    else:
        return 'F'