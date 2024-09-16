import re

# Define the regular expressions for each data type
regex_patterns = {
    'email': r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
    'url': r'https?:\/\/[^\s/$.?#].[^\s]*',
    'phone': r'(\(\d{3}\)\s?|\d{3}[.-]?)\d{3}[.-]?\d{4}',
    'credit_card': r'\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}',
    'time': r'(1[0-2]|0?[1-9]):[0-5][0-9]\s?(AM|PM)?|([01]?[0-9]|2[0-3]):[0-5][0-9]',
    'html_tag': r'<[^>]+>',
    'hashtag': r'#[A-Za-z0-9_]+',
    'currency': r'\$\d{1,3}(,\d{3})*(\.\d{2})?'
}

