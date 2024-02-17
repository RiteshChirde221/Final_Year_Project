import base64 
from urllib.parse import quote

#Encoder for Base64
def base64_encoder(msg):
    msg_bytes=msg.encode('ascii')
    base64_bytes=base64.b64encode(msg_bytes)
    base64_str=base64_bytes.decode('ascii')
    return base64_str
print(base64_encoder('neeraj'))

#Decoder for Base64
def base64_decoder(msg_base64):
    base64_bytes = msg_base64.encode("ascii") 
    msg_bytes = base64.b64decode(base64_bytes) 
    msg_string = msg_bytes.decode("ascii") 
    return msg_string
print(base64_decoder('bmVlcmFq'))

#Encoder for URL
from urllib.parse import quote, urlparse, urlunparse

def encode_full_url(url):
    parsed_url = urlparse(url)
    encoded_url = urlunparse(
        (
            quote(parsed_url.scheme),
            quote(parsed_url.netloc),
            quote(parsed_url.path),
            quote(parsed_url.params),
            quote(parsed_url.query),
            quote(parsed_url.fragment)
        )
    )
    return encoded_url

# Example usage:
url_to_encode = "https://www.example.com/path with spaces?param1=value 1&param2=value 2"
encoded_url = encode_full_url(url_to_encode)

print("Original URL:", url_to_encode)
print("Encoded URL:", encoded_url)
