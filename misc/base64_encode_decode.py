import base64 
from urllib.parse import quote, urlparse, urlunparse

#Encoder for Base64
def base64_encoder(msg):
    msg_bytes=msg.encode('ascii')
    base64_bytes=base64.b64encode(msg_bytes)
    base64_str=base64_bytes.decode('ascii')
    return base64_str

#Decoder for Base64
def base64_decoder(msg_base64):
    base64_bytes = msg_base64.encode("ascii") 
    msg_bytes = base64.b64decode(base64_bytes) 
    msg_string = msg_bytes.decode("ascii") 
    return msg_string


