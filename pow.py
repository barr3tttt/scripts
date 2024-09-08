ciphertext = [7427, 126, 126, 9196, 7367, 126, 6642, 4744]
exponent = 8743
modulus = 10403

# Decrypt each ciphertext number
decrypted_text = ''
for num in ciphertext:
    decrypted_num = pow(num, exponent, modulus)
    decrypted_text += chr(decrypted_num)

print(decrypted_text)