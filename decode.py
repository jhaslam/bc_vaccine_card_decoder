#! /usr/bin/env python
from decode_utils import extract_payload, to_yaml_str

qr_code = input('Paste your QR Code here: ')
payload = extract_payload(qr_code)
pretty_payload = to_yaml_str(payload)
print('\n\nYour decoded Vaccine Card data is as follows:\n\n', pretty_payload)