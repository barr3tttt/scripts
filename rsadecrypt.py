def rsa_decrypt(ciphertext, d, n):
  return pow(ciphertext, d, n)

plaintext = rsa_decrypt(45517729514, 34619990071, 80780754611)
print(plaintext)