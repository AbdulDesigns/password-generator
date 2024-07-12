import random
import string

password_len = 10
password = ""
base_characters =  string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.digits

# looping over collection to generate random password
for i in range(password_len):
  password += random.choice(base_characters)

print("generated random password:",password)  

