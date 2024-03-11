# cis6930sp24-assignment1
# Contents

# Overview
In this assignment, we censor sensitive information like names, dates, phone numbers and address from the user inputted plaintext file. I am replacing the information with '#' key. THe program must be run using the command
# pipenv run python censoror.py --input '*.txt' \
#                    --names --dates --phones --address\
#                    --output 'files/' \
#                    --stats stderr
where --input parameter takes a glob(files that can be accepted) with more than one input being accepted and the --output ,specifying the directory to store all the censored files, will be written to text files(irrespective of input type) with the name being original filename.censored . Incase the input file cannot be processed or censored we display an error message for the same. 

# main.py
I used main.py to list out the functions for each of the flags. 
Note: I have made email as a seperate flag owing to cinvenience as it was a simple regex to hide username apart from the domain name. 

main.py contains the following functions:
censor_phone_numbers
def censor_phone_numbers(content):
    """
    Censors phone numbers in the given content by replacing them with '#' characters. This was done using regular expressions and can identify phone numbers in various formats like 
    (555) 123-4567
    1234567890
    +1 (213)-233-1234
    +1(213)-233-1234

    Args:
        content (str): The content to be censored.

    Returns:
        str: The censored content with phone numbers replaced by '#' characters.
    """

censor_dates
def censor_dates(content):
    """
    Censors dates in the given content by replacing them with '#' characters. Once again used regular expressions to detect a wide range of date formats like
    Mon, 12 January 2021 14:30:00 +0200 (EST)
    12/31/2020
    2020-12-31
    January 1st, 2020
    March 3rd
    Friday 5th March

    Args:
        content (str): The content to be censored.

    Returns:
        str: The censored content with dates replaced by '#'.

    """

censor_names
def censor_names(content):
    """
    Censors names in the given content. Acheived this by using spaCy's NER model en_core_web_lg to detect names. Can detect names with various combinatiosn and even middle names, and names with prefixes like
    John Doe
    Trent-Alexander Arnold
    Dr. Sarah Connor
    George R. R. Martin

    Args:
        content (str): The content to be censored.

    Returns:
        str: The censored content.
    """

censor_emails
ef censor_emails(content):
    """
    Censors email addresses in the given content. Using regular expressions, specifically targetting the username part to censor. 

    Args:
        content (str): The content to be censored.

    Returns:
        str: The censored content with email addresses replaced by '#' characters.

    """

censor_addresses
def censor_addresses(content):
    """
    Censors addresses in the given content by replacing them with '#' characters. For detecting addresses, I used a library called PyAP to parse and extract street addresses from the given text. It can handle addresses of various formats like
    123 Main St, Anytown, CA 90210
    456 Elm Avenue, Smalltown, TX 75001
    789 Pine Blvd Apt 101, Largetown, FL 33101

    Args:
        content (str): The content to be censored.

    Returns:
        str: The censored content with addresses replaced by '#' characters.
    """

# censoror.py
This is the python script that carries out the actual censoring work. It leverages the flags detected by the functions in main.py and parses the command line arguments to see which fields the users wants to censor, the location of the input files, and the destination for the censored output, as well as where to output statistics regarding the censorship process.

Following are the functions in censoror.py
process_text
def process_text(text, options):
    """
    Process the given text based on the specified flags the users mention.

    Args:
        text (str): The input text to be processed.
        options (dict): A dictionary containing the processing options .

    Returns:
        str: The processed text.

    """

process_files
def process_files(input_pattern, output_dir, options, stats_flag):
    """
    Process files matching the given input pattern, censoring the content and saving the censored files to the output directory.

    Args:
        input_pattern (str): The pattern to match the input files.
        output_dir (str): The directory to save the censored files.
        options (dict): A dictionary of options for processing the text.
        stats_flag (str): The flag indicating where to output the statistics.

    Returns:
        None

    Raises:
        None
    """

main
def main():
    """
    Censor sensitive information from text files.

    This function takes command line arguments to specify the input files, output directory,
    where to write stats, and which types of information to censor. It then calls the
    `process_files` function to perform the censorship.

    Command line arguments:
    --input: Glob pattern for input files (required)
    --output: Output directory (required)
    --stats: Where to write stats, choices are 'stdout' or 'stderr' (required)
    --names: Censor names (optional)
    --dates: Censor dates (optional)
    --phones: Censor phone numbers (optional)
    --address: Censor addresses (optional)
    """

Note: The documentation links for all libraries and models I used are mentioned in collaborators file.

# test_main.py
This script is a suite of unit tests designed to validate the effectiveness of the censor functionalities implemented in main.py . This is done using pytest library. It contains testing functions for all of the flags implemented in main function

test_censor_phone_numbers
def test_censor_phone_numbers():
    """
    Test case for the censor_phone_numbers function.

    This test case checks if the censor_phone_numbers function correctly censors phone numbers in a given text.

    The text contains multiple phone numbers in different formats, including with and without parentheses, dashes, and country codes.

    The expected output is a string where all phone numbers are replaced with a series of '#' characters.

    Example:
    Input:
    text = "My phone number is (123) 456-7890. Call me at 1234567890 or +1 (213)-233-1234 or +1(213)-233-1234"
    expected = "My phone number is ##############. Call me at ########## or ################# or ################"

    """

test_censor_dates
def test_censor_dates():
    """
    Test case for the censor_dates function.

    This test case checks if the censor_dates function correctly censors dates in a given text.

    The text contains multiple date formats, such as "01/01/2000", "2000-01-01", and "January 1st, 2000".
    The expected output is a text with the dates censored, represented by a series of '#' characters.

    Example:
    Input:
    text = "I was born on 01/01/2000 or 2000-01-01 or January 1st, 2000"
    expected = "I was born on ########## or ########## or #################"

    Output:
    assert censor_dates(text) == expected

    """

test_censor_names:
def test_censor_names():
    """
    Test case for the censor_names function.

    This test case checks if the censor_names function correctly censors names in a given text.

    The text contains a name "John Doe" which should be censored to "########".

    The expected output is "My name is ######## and I live in New York".

    """

test_censor_emails
def test_censor_emails():
    """
    Test case for the censor_emails function.

    This test case checks if the censor_emails function correctly censors email addresses in a given text.

    The text contains an email address "jane@example.com". The expected output is the same text with the email address censored, i.e., "#####################".

    The assert statement checks if the actual output from the censor_emails function matches the expected output.

test_censor_address
def test_censor_addresses():
    """
    Test case for the censor_addresses function.

    This test case checks if the censor_addresses function correctly censors the addresses in the given text.

    The text contains an address in the format "350 Fifth Avenue, New York, NY 10118".
    The expected result is the same text with the address censored, represented by a series of '#' characters.

    """

# stats

# Bugs and Assumptions