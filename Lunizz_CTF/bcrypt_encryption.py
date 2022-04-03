import bcrypt
import base64

passw = "wewillROCKYOU".encode('ascii')
b64str = base64.b64encode(passw)
hashAndSalt = bcrypt.hashpw(b64str, bcrypt.gensalt())
print(hashAndSalt)

#hashAndSalt = b'$2b$12$LJ3m4rzPGmuN1U/h0IO55.3h9WhI/A0Rcbchmvk10KWRMWe4me81e'
has=b'$2b$12$PCbvsUmqT6OYx.tXS/2/C.wfCfPlwfOqQ15HYV6gs/6ZggqcaWwmG'

print(bcrypt.checkpw(passw,has))

