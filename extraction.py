import re
import argparse
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# Dictionary of Regular Expressions for each data type
regex_patterns = {
    "emails": r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b',  # Pattern to match email addresses
    "urls": r'https?:\/\/(?:www\.)?[A-Za-z0-9.-]+\.[A-Za-z]{2,}(?:\/[^\s]*)?',  # Pattern to match URLs
    "phone_numbers": r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}',  # Pattern to match phone numbers
    "credit_cards": r'(?:\d{4}[-\s]?){3}\d{4}',  # Pattern to match credit card numbers
    "times_24_hour": r'\b([01]?[0-9]|2[0-3]):[0-5][0-9]\b',  # Pattern to match 24-hour time format
    "times_12_hour": r'\b([1-9]|1[0-2]):[0-5][0-9]\s?[APMapm]{2}\b',  # Pattern to match 12-hour time format
    "html_tags": r'<[^>]+>',  # Pattern to match HTML tags
    "hashtags": r'#\w+',  # Pattern to match hashtags
    "currency_amounts": r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?',  # Pattern to match currency amounts
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
        logging.warning(f"Unknown data type: {data_type}")
        raise ValueError(f"Data type '{data_type}' not recognized.")
    
    logging.info(f"Extracting {data_type} data...")
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
    
    for data_type in regex_patterns:
        extracted_data[data_type] = extract_data(data_type, text)
    
    return extracted_data

def process_large_text(input_file, chunk_size=1024):
    """
    Process a large text file in chunks to avoid memory overload.
    
    Args:
        input_file (str): Path to the large input file.
        chunk_size (int): Size of the chunks to read at a time.

    Yields:
        str: A chunk of text from the file.
    """
    with open(input_file, 'r') as file:
        while chunk := file.read(chunk_size):
            yield chunk

def main():
    """
    Command-Line Interface (CLI) to handle input from the user, either as a text string or from a file.
    """
    parser = argparse.ArgumentParser(description="Extract data using regular expressions.")
    parser.add_argument("input_source", help="Path to input text file or direct text input", type=str)
    parser.add_argument("--from-file", help="Specify if input is a file", action='store_true')
    args = parser.parse_args()

    if args.from_file:
        logging.info(f"Processing large input file: {args.input_source}")
        for text_chunk in process_large_text(args.input_source):
            extracted_results = process_text(text_chunk)
            for data_type, matches in extracted_results.items():
                print(f"{data_type.capitalize()}: {matches}")
    else:
        logging.info("Processing direct text input.")
        extracted_results = process_text(args.input_source)
        for data_type, matches in extracted_results.items():
            print(f"{data_type.capitalize()}: {matches}")

if __name__ == "__main__":
    main()