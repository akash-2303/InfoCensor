# # import re
# # import spacy
# # import pyap
# # from dateparser import parse

# # # Load Spacy NLP model
# # nlp = spacy.load("en_core_web_lg")

# # import re

# # def censor_phone_numbers(content):
# #     """
# #     Censors phone numbers in the given content by replacing them with '#' characters.

# #     Args:
# #         content (str): The content to be censored.

# #     Returns:
# #         str: The censored content with phone numbers replaced by '#' characters.
# #     """
# #     patterns = [
# #         r'\(\d{3}\) \d{3}-\d{4}',  # (555) 123-4567
# #         r'\d{10}',  # 1234567890
# #         r'\+\d{1} \(\d{3}\)-\d{3}-\d{4}',  # +1 (213)-233-1234
# #         r'\+\d{1}\(\d{3}\)-\d{3}-\d{4}'  # +1(213)-233-1234
# #     ]
# #     final_re = re.compile('|'.join(patterns))
# #     return re.sub(final_re, lambda match: '#' * len(match.group()), content)

# # import re

# # def censor_dates(content):
# #     """
# #     Censors dates in the given content by replacing them with '#' characters.

# #     Args:
# #         content (str): The content to be censored.

# #     Returns:
# #         str: The censored content with dates replaced by '#'.

# #     """
# #     date_regexes = [
# #         # Match: Full date with weekday, including timezone
# #         r'\b(?:Mon|Tue(?:s)?|Wed(?:nes)?|Thu(?:rs)?|Fri|Sat(?:ur)?|Sun),\s+\d{1,2}\s(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\s\d{4}\s\d{2}:\d{2}:\d{2}\s(?:-|\+)\d{4}\s\([A-Z]+\)',
# #         # Additional patterns for various date formats, including those without explicit day names
# #         r'\b\d{1,2}[-/]\d{1,2}[-/]\d{2,4}',  
# #         r'\b\d{4}[-/]\d{1,2}[-/]\d{1,2}',  
# #         r'\b\d{1,2}(?:st|nd|rd|th)?\s+of\s+(?:January|February|March|April|May|June|July|August|September|October|November|December)',
# #         r'\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s\d{1,2}(?:st|nd|rd|th)?,\s\d{4}',
# #         r'\b(?:Mon|Tue(?:s)?|Wed(?:nes)?|Thu(?:rs)?|Fri|Sat(?:ur)?|Sun)?\s?\d{1,2}(?:st|nd|rd|th)?\s+(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)(?:,\s*\d{2,4})?',
# #     ]
# #     combined_regex = '|'.join(date_regexes)
# #     return re.sub(combined_regex, lambda match: '#' * len(match.group()), content)

# # def censor_names(content):
# #     """
# #     Censors names in the given content.

# #     Args:
# #         content (str): The content to be censored.

# #     Returns:
# #         str: The censored content.
# #     """
# #     doc = nlp(content)
# #     for ent in doc.ents:
# #         if ent.label_ == "PERSON":
# #             content = content.replace(ent.text, '#' * len(ent.text))
# #     return content

# # def censor_emails(content):
# #     """
# #     Censors email addresses in the given content.

# #     Args:
# #         content (str): The content to be censored.

# #     Returns:
# #         str: The censored content with email addresses replaced by '#' characters.

# #     """
# #     email_regex = r'([a-zA-Z0-9._%+-]+)@([a-zA-Z0-9.-]+\.[a-zA-Z]{2,4})'
# #     return re.sub(email_regex, lambda match: '#' * len(match.group(1)) + '@' + match.group(2), content)

# # def censor_addresses(content):
# #     """
# #     Censors addresses in the given content by replacing them with '#' characters.

# #     Args:
# #         content (str): The content to be censored.

# #     Returns:
# #         str: The censored content with addresses replaced by '#' characters.
# #     """
# #     addresses = pyap.parse(content, country='US')
# #     for address in addresses:
# #         content = content.replace(address.full_address, '#' * len(address.full_address))
# #     return content


# import re
# import spacy
# import pyap
# from dateparser import parse

# # Load Spacy NLP model
# # nlp = spacy.load("en_core_web_lg")
# nlp = spacy.load("en_core_web_trf")

# import re

# def censor_phone_numbers(content):
#     """
#     Censors phone numbers in the given content.

#     Args:
#         content (str): The content to be censored.

#     Returns:
#         tuple: A tuple containing the censored content and the count of phone numbers censored.

#     Example:
#         >>> content = "Please call (555) 123-4567 for assistance."
#         >>> censor_phone_numbers(content)
#         ('Please call ########### for assistance.', 1)
#     """
#     patterns = [
#         r'\(\d{3}\) \d{3}-\d{4}',  # (555) 123-4567
#         r'\d{10}',  # 1234567890
#         r'\+\d{1} \(\d{3}\)-\d{3}-\d{4}',  # +1 (213)-233-1234
#         r'\+\d{1}\(\d{3}\)-\d{3}-\d{4}'  # +1(213)-233-1234
#     ]
#     final_re = re.compile('|'.join(patterns))
#     count = len(re.findall(final_re, content))
#     return re.sub(final_re, lambda match: '#' * len(match.group()), content), count

# import re

# def censor_dates(content):
#     """
#     Censors dates in the given content by replacing them with '#' characters.

#     Args:
#         content (str): The content to be censored.

#     Returns:
#         tuple: A tuple containing the censored content and the count of dates censored.

#     Example:
#         >>> content = "Today is 2022-01-01 and tomorrow is January 2nd, 2022."
#         >>> censor_dates(content)
#         ('Today is ############ and tomorrow is #####################.', 2)
#     """
#     date_regexes = [
#         # Match: Full date with weekday, including timezone
#         r'\b(?:Mon|Tue(?:s)?|Wed(?:nes)?|Thu(?:rs)?|Fri|Sat(?:ur)?|Sun),\s+\d{1,2}\s(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\s\d{4}\s\d{2}:\d{2}:\d{2}\s(?:-|\+)\d{4}\s\([A-Z]+\)',
#         # Additional patterns for various date formats, including those without explicit day names
#         r'\b\d{1,2}[-/]\d{1,2}[-/]\d{2,4}',  
#         r'\b\d{4}[-/]\d{1,2}[-/]\d{1,2}',  
#         r'\b\d{1,2}(?:st|nd|rd|th)?\s+of\s+(?:January|February|March|April|May|June|July|August|September|October|November|December)',
#         r'\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s\d{1,2}(?:st|nd|rd|th)?,\s\d{4}',
#         r'\b(?:Mon|Tue(?:s)?|Wed(?:nes)?|Thu(?:rs)?|Fri|Sat(?:ur)?|Sun)?\s?\d{1,2}(?:st|nd|rd|th)?\s+(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)(?:,\s*\d{2,4})?',
#         r'\b(?:Mon|Tue|Wed|Thu|Fri|Sat|Sun)\s\d{1,2}(?:st|nd|rd|th)?\s(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\s\d{4}'
#     ]
#     combined_regex = '|'.join(date_regexes)
#     count = len(re.findall(combined_regex, content))
#     return re.sub(combined_regex, lambda match: '#' * len(match.group()), content), count

# def censor_names(content):
#     """
#     Censors names in the given content by replacing them with '#' characters.

#     Args:
#         content (str): The content to be censored.

#     Returns:
#         tuple: A tuple containing the censored content (str) and the count of names censored (int).
#     """
#     count = 0
#     doc = nlp(content)
#     for ent in doc.ents:
#         if ent.label_ == "PERSON":
#             count += 1
#             content = content.replace(ent.text, '#' * len(ent.text))
#     emails = censor_emails(content)
#     print(emails)
#     for email in emails:
#         # doc1 = nlp(email)
#         # for ent in doc1.ents:
#         #     if ent.label_ == "PERSON":
#         content = content.replace(email[0], '#' * len(email[0]))
#     return content, count


# def censor_emails(content):
#     """
#     Censors email addresses in the given content.

#     Args:
#         content (str): The content to be censored.

#     Returns:
#         list: A list of email addresses found in the content.

#     """
#     email_regex = r'([a-zA-Z0-9._%+-]+)@([a-zA-Z0-9.-]+\.[a-zA-Z]{2,4})'
#     return re.findall(email_regex, content)

# def censor_addresses(content):
#     """
#     Censors addresses in the given content.

#     Args:
#         content (str): The content to be censored.

#     Returns:
#         tuple: A tuple containing the censored content and the number of addresses censored.
#     """
#     addresses = pyap.parse(content, country='US')
#     for address in addresses:
#         content = content.replace(address.full_address, '#' * len(address.full_address))
#     return content, len(addresses)
