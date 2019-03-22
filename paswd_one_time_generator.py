'''Python one-time password generator'''
'''Dont use this for financial transactions'''

import random
import string

def generate_otp(size):
    otp = ''.join([random.choice(string.digits)
            for n in range(size)])
    return otp
generate_otp(4)
generate_otp(6)