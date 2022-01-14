# British Columbia Vaccine Card Decoder

## Disclaimer
I am in no way associated with the province of British Columbia, except
for the fact that I happen to live here. I am simply a software engineer
scratching a curiosity itch.

## Description
British Columbia Vaccine passports display a QR code.
If you are curious, and use an off-the-shelf QR code reader on your celphone
(such as Google Lens) to look into the text that it encodes, you will just
see a long series of numbers that look something like this:

```
shc:/5762958976377857575700784227.....
```

This project simply deciphers these numbers back into a human-readable form 
so that the average person with some computer knowledge can be informed on 
what information is being revealed whenever they present their BC Vaccine Card.

## Working with this Decoder
This project is implemented in the Python Programming Language and works 
entirely from the command prompt. There is no fancy GUI.

- Install Python >= 3.9
- Fetch contents of this project. From the command prompt:
  - `git init`
  - `git pull https://github.com/jhaslam/bc_vaccine_card_decoder.git`
- Fetch this project's dependency closure. From the command prompt:
  - `python -m venv venv`
  - `source ./project_env/Scripts/activate`
  - `python -m pip install -r requirements.txt` 

## Running the Decoder
- From this project's directory, run:  
  `python -m shc_decode`
- Paste the encoded QR code ```sch:\57629...``` numbers provided by your
  off-the-shelf QR-Code reader into the prompt.

## Technical Discussion
A bit of digging reveals that British Columbia is using the **"Smart Health 
Cards"** framework, which encodes this data using **"Compact Serialization JSON 
Web Signatures (JWS)"**. The data is signed but not encrypted so if we want to 
look, we just need to decode according to published spec.

## References
https://spec.smarthealth.cards/  
https://datatracker.ietf.org/doc/html/rfc7515


