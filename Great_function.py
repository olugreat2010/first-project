def password ( correct_password  = "admin"):
    if password == correct_password:
        return True
    else:
        return False
    
def valid_email(email):
    if '@' in email and '.' in email:
        return True
    else:
        return False
    
def len_password(password):
    if len (password) > 6:
        return True
    else:
        return False
def sum(balance,deposit_amount):
    return balance + deposit_amount

def subtract(balance,withdrawal_amount):
    return balance - withdrawal_amount

def pin(default_pin = 2010):
    if pin == default_pin:
        return True
    else:
        return False

#def uppercase(password):
#    for k in password ():