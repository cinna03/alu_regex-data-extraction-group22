import re

# Dictionary of Regular Expressions for each data type
regex_patterns = {
    "emails": r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b',
    "urls": r'https?:\/\/(www\.)?[A-Za-z0-9.-]+\.[A-Za-z]{2,}([\/\w.-]*)*',
    "phone_numbers": r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}',
    "credit_cards": r'(?:\d{4}[-\s]?){3}\d{4}',
    "times_24_hour": r'\b([01]?[0-9]|2[0-3]):[0-5][0-9]\b',
    "times_12_hour": r'\b([1-9]|1[0-2]):[0-5][0-9]\s?[APMapm]{2}\b',
    "html_tags": r'<[^>]+>',
    "hashtags": r'#\w+',
    "currency_amounts": r'\$\d{1,3}(,\d{3})*(\.\d{2})?',
}

def extract_data(data_type, text):
    """
    Extracts specific data types (like emails, URLs, phone numbers) from the text using regex.

    Args:
        data_type (str): The type of data to extract (e.g., 'emails', 'urls').
        text (str): The input text to search through.
    
    Returns:
        list: A list of matched patterns found in the input text.
    """
    pattern = regex_patterns.get(data_type)
    if not pattern:
        raise ValueError(f"Data type '{data_type}' not recognized.")
    
    # Return all matches found
    return re.findall(pattern, text)

def process_text(text):
    """
    Scans the input text and extracts all relevant data types defined in the regex_patterns.

    Args:
        text (str): Input string containing various patterns (emails, URLs, etc.)

    Returns:
        dict: Dictionary containing matched patterns for each data type.
    """
    extracted_data = {}
    
    for data_type, pattern in regex_patterns.items():
        extracted_data[data_type] = extract_data(data_type, text)
    
    return extracted_data

if __name__ == "__main__":
    # Example text for testing
    sample_text = """
    For inquiries, email user@example.com or visit our site at https://www.example.com.
    You can call us at (123) 456-7890 or 123-456-7890. Our team is available at 2:30 PM or 14:30.
    Credit cards: 1234 5678 9012 3456 and 1234-5678-9012-3456. Hashtag: #MyNewProject. Price: $19.99.
    HTML tags like <div class="container"> can be found in the HTML.
    """

    result = process_text(sample_text)
    for data_type, matches in result.items():
        print(f"{data_type.capitalize()}: {matches}")
