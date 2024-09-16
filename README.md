API that aggregates data from all over the web and displays relevant information based on the user request

A. How to run the APP:
The app can be run from the command line, either with a direct text input or a file input.

option 1: python extraction.py "Contact: user@example.com, URL: https://example.com, Phone: (123) 456-7890"

option 2: python extraction.py path/to/large_text_file.txt --from-file

B. Output format:

Emails: ['user@example.com']
URLs: ['https://example.com']
Phone Numbers: ['(123) 456-7890']
Credit Cards: []
Times 24-hour: []
Times 12-hour: []
HTML Tags: []
Hashtags: []
Currency Amounts: []

C. Unit testing:
To ensure the correctness of the extraction logic, unit tests are included. You can run the tests using unittest as follows:

python -m unittest test_extraction.py
