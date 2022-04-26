from base64 import b64encode
from base64 import b64decode

def xor(text, key):
    out = ''
    for i in range(len(text)):
        current = text[i]
        current_key = key[i % len(key)]
        out += chr(ord(current) ^ ord(current_key))
    return out

def encode(text, key):
    return b64encode(xor(text, key).encode("utf-8")).decode()

def decode(text, key):
    return xor(b64decode(text).decode(), key)
