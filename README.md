# cis6930sp24-assignment1
# Contents
Overview
main.py
censoror.py
test_main.py
stats
Assumptions and bugs
How to run

# Overview
In this assignment, we censor sensitive information like names, dates, phone numbers and address from the user inputted plaintext file. I am replacing the information with '\u2588' key. THe program must be run using the command
` pipenv run python censoror.py --input '*.txt' \
                    --names --dates --phones --address\
                    --output 'files/' \
                    --stats stderr`
where --input parameter takes a glob(files that can be accepted) with more than one input being accepted and the --output ,specifying the directory to store all the censored files, will be written to text files(irrespective of input type) with the name being original filename.censored . Incase the input file cannot be processed or censored we display an error message for the same. 

# main.py
I used main.py to list out the functions for each of the flags. 
Note: I have made email as a seperate flag owing to cinvenience as it was a simple regex to hide username apart from the domain name. 

main.py contains the following functions:
censor_phone_numbers
def censor_phone_numbers(content):
    """
    Censors phone numbers in the given content by replacing them with '\u2588' characters. This was done using regular expressions and can identify phone numbers in various formats like 
    (555) 123-4567
    1234567890
    +1 (213)-233-1234
    +1(213)-233-1234

    Args:
        content (str): The content to be censored.

    Returns:
        tuple: A tuple containing the censored content and the count of phone numbers censored.
    """

censor_dates
def censor_dates(content):
    """
    Censors dates in the given content by replacing them with '\u2588' characters. Once again used regular expressions to detect a wide range of date formats like
    Mon, 12 January 2021 14:30:00 +0200 (EST)
    12/31/2020
    2020-12-31
    January 1st, 2020
    March 3rd
    Friday 5th March

    Args:
        content (str): The content to be censored.

    Returns:
        tuple: A tuple containing the censored content and the count of dates censored.

    """

censor_names
def censor_names(content):
    """
    Censors names in the given content. Acheived this by using spaCy's NER model en_core_web_trf to detect names. Can detect names with various combinations and even middle names, and names with prefixes like
    John Doe
    Trent-Alexander Arnold
    Dr. Sarah Connor
    George R. R. Martin

    Args:
        content (str): The content to be censored.

    Returns:
        tuple: A tuple containing the censored content (str) and the count of names censored (int).
    """

censor_emails
ef censor_emails(content):
    """
    Censors email addresses in the given content. Using regular expressions, specifically targetting the username part to censor. 

    Args:
        content (str): The content to be censored.

    Returns:
        list: A list of email addresses found in the content. Is not an individual flag but is used by name function. 

    """

censor_addresses
def censor_addresses(content):
    """
    Censors addresses in the given content by replacing them with '\u2588' characters. For detecting addresses, I used a library called PyAP to parse and extract street addresses from the given text. It can handle addresses of various formats like
    123 Main St, Anytown, CA 90210
    456 Elm Avenue, Smalltown, TX 75001
    789 Pine Blvd Apt 101, Largetown, FL 33101
    Also there were a few addresses that pyap failed to recognize so I also used spaCy as a double check to make sure no addresses get missed. 

    Args:
        content (str): The content to be censored.

    Returns:
        tuple: A tuple containing the censored content and the number of addresses censored.
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
    This test case checks if the censor_phone_numbers function correctly censors phone numbers in a given text.

    It compares the censored text and the count of censored phone numbers with the expected values.
    The text contains multiple phone numbers in different formats, including with and without parentheses, dashes, and country codes.

    The expected output is a string where all phone numbers are replaced with a series of '\u2588' characters and it checks if the count matches. .

    Example:
    Input:
    text = "My phone number is (123) 456-7890. Call me at 1234567890 or +1 (213)-233-1234 or +1(213)-233-1234"
    expected = "My phone number is ##############. Call me at ########## or ################# or ################"

    """

test_censor_dates
def test_censor_dates():
    """
    This test case checks if the censor_dates function correctly censors dates in a given text.
    It verifies that the censored text matches the expected text and that the count of censored dates is correct.
    The text contains multiple date formats, such as "01/01/2000", "2000-01-01", and "January 1st, 2000".
    The expected output is a text with the dates censored, represented by a series of '\u2588' characters.

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
    This test case checks if the censor_names function correctly censors names in a given text.
    The expected behavior is that the censor_names function should replace any occurrence of a name in the text with a series of '\u2588' characters of the same length as the name.
    The text contains a name "John Doe" which should be censored to "########".

    The expected output is "My name is ######## and I live in New York".

    """
    assert censor_dates(text) == expected

test_censor_address
def test_censor_addresses():
    """
    This test case checks if the censor_addresses function correctly censors the addresses in the given text.
    It verifies that the censored text matches the expected text and that the count of censored addresses is correct. 
    The expected result is the same text with the address censored, represented by a series of '\u2588' characters.

    assert censor_dates(text) == expected
    """

# stats
To display the statistics regarding how many details have been censored, I initialized count and kept incremented it as we keep detecting new entries of the fields the user enters. I took a random file from the dataset, 11.txt, to check the code in local environment and got the output in the following format

`11.txt: Names censored: 40, Dates censored: 4, Phones censored: 1, Addresses censored: 0
Files processed: 1
Characters censored: 396
Errors: 0`


# Assumptions and Bugs
I did make some assumptions whilst writing the code. First major assumption is, addresses are only US addresses. pyap library and the spaCy transformer model only have US addresses so anything else might fail. Also I assumed all email usernames are sensitive and did not check if the username contains a name or if it was abstract. Also we are assuming there wont be any foreign names that dont follow the same scripting style. 

As for bugs, phone numbers that are not of the three mostly used US format will not be detected. Numbers that might have dots instead of space for instance, will not get flagged and censored. Numbers without area codes will also fail to get censored. Similarly not all date formats are recognized. Dates that mention a rangle like 2002 - 2004 and formats like 3rd of March are not getting detected by the regex. Also in some cases, abbreviations like tue, might fail to get recognized. In the sample output, the month and year were succesfully detected and censored but 'Tuesday' was not censored. As for names, parts of names like oe, Doe are sometimes failing. Also foreign names wont get recognized. 

# How to Run
To run pytest, simply use
`pytest`

And to execute the program, use
`pipenv run python censoror.py --input '*.txt' \
                    --names --dates --phones --address\
                    --output 'files/' \
                    --stats stderr`
where files is the name of the directory you want your output to get stored in. 