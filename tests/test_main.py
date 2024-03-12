import pytest
from assignment1.main import censor_phone_numbers, censor_dates, censor_names, censor_addresses

def test_censor_phone_numbers():
    text = "My phone number is (123) 456-7890. Call me at 1234567890 or +1 (213)-233-1234 or +1(213)-233-1234"
    expected_text = "My phone number is ##############. Call me at ########## or ################# or ################"
    censored_text, count = censor_phone_numbers(text)
    assert censored_text == expected_text
    assert count == 4  

def test_censor_dates():
    text = "I was born on 01/01/2000 or 2000-01-01 or January 1st, 2000"
    expected_text = "I was born on ########## or ########## or #################"
    censored_text, count = censor_dates(text)
    assert censored_text == expected_text
    assert count == 3  

def test_censor_names():
    text = "My name is John Doe and I live in New York."
    expected_text = "My name is ######## and I live in New York."
    censored_text, count = censor_names(text)
    assert censored_text == expected_text
    assert count == 1  

def test_censor_addresses():
    text = "My address is 350 Fifth Avenue, New York, NY 10118"
    expected_text = "My address is ####################################"
    censored_text, count = censor_addresses(text)
    assert censored_text == expected_text
    assert count == 1
