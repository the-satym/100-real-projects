import random

def otp_generator():
    return ''.join(map(str, random.sample(range(10),6)))

print(otp_generator())

print("OTP generated successfully")
user_input = input("To generate another OTP, press 'y':  ").upper().strip()
while user_input == 'Y':
    print(otp_generator())
    user_input = input("To generate another OTP, press 'y':  ").upper().strip()
if user_input == 'N':
    print("Exiting the OTP generator.")
