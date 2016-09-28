import itertools
import base64

cookie = 'ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw='

origin = bytes('{"showpassword":"no","bgcolor":"#ffffff"}'.encode())
target = bytes('{"showpassword":"yes","bgcolor":"#ffffff"}'.encode())

# Remove b64 encoding
encrypted = bytes(base64.b64decode(cookie))

# XOR encrypted string with plaintext
key = bytes([ x^y for x,y in zip(encrypted, origin)])

# Cut to first 4 bytes
key = key[:4]

payload = [ x^y for x,y in zip(target, itertools.cycle(key))]

print(base64.b64encode(bytes(payload)).decode())
