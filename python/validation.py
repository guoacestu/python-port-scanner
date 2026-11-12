
#check if input is a number 
def number_valid(user_input):
    try:
        user_input=int(user_input)
        return True
    except:
        return False

