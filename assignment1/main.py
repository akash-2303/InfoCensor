import re
import spacy
import pyap
from dateparser import parse

# Load Spacy NLP model
# nlp = spacy.load("en_core_web_lg")
nlp = spacy.load("en_core_web_trf")

def censor_phone_numbers(content):
    patterns = [
        r'\(\d{3}\) \d{3}-\d{4}',  
        r'\d{10}',  
        r'\+\d{1} \(\d{3}\)-\d{3}-\d{4}',  
        r'\+\d{1}\(\d{3}\)-\d{3}-\d{4}'  
    ]
    final_re = re.compile('|'.join(patterns))
    count = len(re.findall(final_re, content))
    return re.sub(final_re, lambda match: '\u2588' * len(match.group()), content), count

def censor_dates(content):
    date_regexes = [
    # Match: Full date with weekday, including timezone
    r'\b(?:Mon|Tue(?:s)?|Wed(?:nes)?|Thu(?:rs)?|Fri|Sat(?:ur)?|Sun),\s+\d{1,2}\s(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\s\d{4}\s\d{2}:\d{2}:\d{2}\s(?:-|\+)\d{4}\s\([A-Z]+\)',
    # Additional patterns for various date formats, including those without explicit day names
    r'\b\d{1,2}[-/]\d{1,2}[-/]\d{2,4}',  
    r'\b\d{4}[-/]\d{1,2}[-/]\d{1,2}',  
    r'\b\d{1,2}(?:st|nd|rd|th)?\s+of\s+(?:January|February|March|April|May|June|July|August|September|October|November|December)',
    r'\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s\d{1,2}(?:st|nd|rd|th)?,\s\d{4}',
    r'\b(?:Mon|Tue(?:s)?|Wed(?:nes)?|Thu(?:rs)?|Fri|Sat(?:ur)?|Sun)?\s?\d{1,2}(?:st|nd|rd|th)?\s+(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)(?:,\s*\d{2,4})?',
    r'\b(?:Mon|Tue|Wed|Thu|Fri|Sat|Sun)\s\d{1,2}(?:st|nd|rd|th)?\s(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\s\d{4}'
]
    combined_regex = '|'.join(date_regexes)
    count = len(re.findall(combined_regex, content))
    return re.sub(combined_regex, lambda match: '\u2588' * len(match.group()), content), count

def censor_names(content):
    count = 0
    doc = nlp(content)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            count += 1
            content = content.replace(ent.text, '\u2588' * len(ent.text))
    emails = censor_emails(content)
    # print(emails)
    for email in emails:
        # doc1 = nlp(email)
        # for ent in doc1.ents:
        #     if ent.label_ == "PERSON":
        content = content.replace(email[0], '\u2588' * len(email[0]))
    return content,count


def censor_emails(content):
    email_regex = r'([a-zA-Z0-9._%+-]+)@([a-zA-Z0-9.-]+\.[a-zA-Z]{2,4})'
    #return re.sub(email_regex, lambda match: '\u2588' * len(match.group(1)) + '@' + match.group(2), content)
    return re.findall(email_regex, content)

def censor_addresses(content):
    addresses = pyap.parse(content, country='US')
    for address in addresses:
        content = content.replace(address.full_address, '\u2588' * len(address.full_address))
    return content, len(addresses)
