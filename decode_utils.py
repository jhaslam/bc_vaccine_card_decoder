import base64
import json
import zlib

import yaml

def extract_numeric(qr_code: str) -> str:
    # Strip off the beginning 'shc:/' from the QR code string, if it is 
    # present. It is just there to indicate MIME type. 
    # This produces a "numeric" encoded string
    numeric_encoded = qr_code
    if qr_code[:5] == 'shc:/':
      numeric_encoded = qr_code[5:]
    return numeric_encoded

def numeric_to_jws(numeric_encoded: str) -> str:
    # Convert a numeric encoded string to a JWS encoded string:
    #     1) Split the numeric string into pairs of numbers, each of which 
    #         represents a single JWS character.
    #     2) From the decimal value of each of these pairs, add 45
    #     3) Convert the result of each decimal value to UTF-8.
    pairs = [numeric_encoded[i:i+2] for i in range(0, len(numeric_encoded), 2)]
    decimal_vals = [int(val) for val in pairs]
    shifted_vals = [val + 45 for val in decimal_vals]
    characters = [chr(val) for val in shifted_vals]
    return ''.join(characters)

def extract_jws_payload(jws: str) -> str:
    # Extracts the payload from a JWS encoded string.
    # JWS encoded strings consist of three fields delimited by a dot '.':
    # "JWS Protected Header", "JWS Payload", and "JWS Signature"
    # The payload portion is encoded with zip and base64 encoding
    extracted_payload =  jws.split('.')[1]
    decoded_payload = base64_decode(extracted_payload)
    return decompress(decoded_payload)

def base64_decode(encoded: str) -> bytes:
    # JWS encodes binary data using base64URL rather than standard base64
    # Padding needs to be recovered or decode will fail
    padded = encoded + ('=' * (-len(encoded) % 4))
    return base64.urlsafe_b64decode(padded)

def decompress(zipped: bytes) -> str:
    # JWS compresses payload data using the "RFC 1951 Deflate" data format
    inflated_bytes = zlib.decompress(zipped, wbits = -zlib.MAX_WBITS)
    return inflated_bytes.decode("utf-8")

def to_yaml_str(payload) -> str:
    # JWS payloads are in JSON.
    # Convert this to YAML for pretty-printing purposes
    return yaml.dump(payload)

def extract_payload(qr_code: str):
    # Main entrypoint to the payload extraction process
    numeric = extract_numeric(qr_code)
    jws = numeric_to_jws(numeric)
    jws_payload = extract_jws_payload(jws)
    return json.loads(jws_payload)
