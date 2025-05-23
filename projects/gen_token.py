import secrets as sec

token = sec.token_hex(4)
print(token)

token2 = sec.randbits(4)
print(token2)