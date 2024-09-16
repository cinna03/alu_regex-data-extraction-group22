import pytest
from extraction import extract_data

# Sample text to test against
sample_text = """
    Contact user@example.com and admin@site.co.uk.
    URL: https://www.example.com, call (123) 456-7890 or 123.456.7890.
    Use credit card 1234 5678 9012 3456 or 1234-5678-9012-3456.
    Event at 2:30 PM or 14:30. HTML tags: <p>, <div>. Hashtags: #AIrocks.
    Prices: $1,234.56.
"""

def test_email_extraction():
    assert extract_data("emails", sample_text) == [
        "user@example.com", "admin@site.co.uk"
    ]

def test_url_extraction():
    assert extract_data("urls", sample_text) == [
        "https://www.example.com"
    ]

def test_phone_number_extraction():
    assert extract_data("phone_numbers", sample_text) == [
        "(123) 456-7890", "123.456.7890"
    ]

def test_credit_card_extraction():
    assert extract_data("credit_cards", sample_text) == [
        "1234 5678 9012 3456", "1234-5678-9012-3456"
    ]

def test_currency_extraction():
    assert extract_data("currency_amounts", sample_text) == [
        "$1,234.56"
    ]

# Add more tests for other data types (hashtags, HTML tags, times, etc.)

if __name__ == "__main__":
    pytest.main()
