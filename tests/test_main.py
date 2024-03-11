import pytest
from assignment1.main import censor_phone_numbers, censor_dates, censor_names, censor_emails, censor_addresses

def test_censor_phone_numbers():
    text = "My phone number is (123) 456-7890. Call me at 1234567890 or +1 (213)-233-1234 or +1(213)-233-1234"
    expected = "My phone number is ##############. Call me at ########## or ################# or ################"
    assert censor_phone_numbers(text) == expected

def test_censor_dates():
    text = "I was born on 01/01/2000 or 2000-01-01 or January 1st, 2000"
    expected = "I was born on ########## or ########## or #################"
    assert censor_dates(text) == expected

def test_censor_names():
    text = "My name is John Doe and I live in New York"
    expected = "My name is ######## and I live in New York"
    assert censor_names(text) == expected

# def test_censor_emails():
#     text = "My email is jane@example.com"
#     expected = "My email is #####################."
#     assert censor_emails(text) == expected

def test_censor_addresses():
    text = "My address is 350 Fifth Avenue, New York, NY 10118"
    expected = "My address is ####################################"
    assert censor_addresses(text) == expected