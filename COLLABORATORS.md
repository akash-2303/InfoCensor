Hari Krishna Reddy Golamari | Golamari.h@ufl.edu | Helped in debugging basefile filepath errors

spaCy model for names and addresses | en_core_web_trf | https://spacy.io/models/en

DateParser | https://dateparser.readthedocs.io/en/latest/usage.html

Stack Overflow | https://stackoverflow.com/questions/37745801/how-can-i-extract-address-from-raw-text-using-nltk-in-python

PYAP | https://khadkechetan.medium.com/address-extraction-and-parser-with-nlp-4d3db7b9535d

ChatGPT | Generating ranges of regex for dates and email| 
Prompt 1: I need a regex that can identify different formats of date like Mon, 12 January 2021 14:30:00 +0200 (EST)
    12/31/2020
    2020-12-31
    January 1st, 2020
    March 3rd
    Friday 5th March
Reply: (\b(Mon|Tue|Wed|Thu|Fri|Sat|Sun),?\s+)?(0?[1-9]|1[0-2]|[1-9]|[1-2][0-9]|3[01])(st|nd|rd|th)?(\s+|\s*,\s*|\s*-\s*|\s*/\s*)(Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?|[0-9]+)(\s*,?\s*|\s*-\s*|\s*/\s*)(\d{4}|\d{2})(\s+[0-2]?[0-9]:[0-5][0-9]:[0-5][0-9]\s*\+\d{4}\s*\(?\w*\)?)?

Prompt 2: First generate regex pattern for Full date with weekday, including timezone
Reply: \b(Mon|Tue|Wed|Thu|Fri|Sat|Sun),\s(0?[1-9]|[12][0-9]|3[01])\s(January|February|March|April|May|June|July|August|September|October|November|December)\s\d{4}\s[0-2]\d:[0-5]\d:[0-5]\d\s[+-]\d{4}\s\(\w+\)

Prompt 3: Additional patterns for various date formats, including those without explicit day names
Reply: \b(0?[1-9]|1[012])\/(0?[1-9]|[12]\d|3[01])\/(\d{4})\b
\b(\d{4})-(0?[1-9]|1[012])-(0?[1-9]|[12]\d|3[01])\b
\b(January|February|March|April|May|June|July|August|September|October|November|December)\s(0?[1-9]|[12]\d|3[01])(st|nd|rd|th)?,\s\d{4}\b
\b(January|February|March|April|May|June|July|August|September|October|November|December)\s(0?[1-9]|[12]\d|3[01])(st|nd|rd|th)?\b

Prompt 4: I want a regex pattern to identify the username in emails and split into username and domain name
Reply: ^([a-zA-Z0-9._%+-]+)@([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})$


