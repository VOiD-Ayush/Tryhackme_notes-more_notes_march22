from Crypto.Util.number import bytes_to_long, long_to_bytes

username = long_to_bytes(1684630636)

password = long_to_bytes(2457564920124666544827225107428488864802762356)


print(username.decode('ascii'))
print(password.decode('ascii'))

# output
# dill
# n3v3r_@_d1ll_m0m3nt