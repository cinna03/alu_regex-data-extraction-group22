import unittest
from extraction import extract_data, process_text

class TestRegexExtraction(unittest.TestCase):
    """
    Test class for regular expression extraction functions.
    """

    def test_extract_emails(self):
        """
        Test extracting email addresses from a text.
        """
        # Input text containing email addresses
        text = "Contact us at user@example.com or firstname.lastname@company.co.uk."
        # Expected email addresses
        expected_emails = ['user@example.com', 'firstname.lastname@company.co.uk']
        # Assert that the extracted emails  the expected ones
        self.assertEqual(extract_data("emails", text), expected_emails)

    def test_extract_urls(self):
        """
        Test extracting URLs from a text.
        """
        # Input text containing URLs
        text = "Visit https://www.example.com or http://subdomain.example.org/page."
        # Expected URLs
        expected_urls = ['https://www.example.com', 'http://subdomain.example.org/page']
        # Assert that the extracted URLs match the expected ones
        self.assertEqual(extract_data("urls", text), expected_urls)

    def test_extract_phone_numbers(self):
        """
        Test extracting phone numbers from a text.
        """
        # Input text containing phone numbers
        text = "Call me at (123) 456-7890 or 123-456-7890."
        # Expected phone numbers
        expected_phone_numbers = ['(123) 456-7890', '123-456-7890']
        # Assert that the extracted phone numbers match the expected ones
        self.assertEqual(extract_data("phone_numbers", text), expected_phone_numbers)

    def test_extract_credit_cards(self):
        """
        Test extracting credit card numbers from a text.
        """
        # Input text containing credit card numbers
        text = "Credit card: 1234 5678 9012 3456 or 1234-5678-9012-3456."
        # Expected credit card numbers
        expected_credit_cards = ['1234 5678 9012 3456', '1234-5678-9012-3456']
        # Assert that the extracted credit card numbers match the expected ones
        self.assertEqual(extract_data("credit_cards", text), expected_credit_cards)

    def test_extract_times(self):
        """
        Test extracting times from a text.
        """
        # Input text containing times
        text = "The meeting is at 14:30 or 2:30 PM."
        # Expected times in 24-hour format
        expected_times_24_hour = ['14:30']
        # Expected times in 12-hour format
        expected_times_12_hour = ['2:30 PM']
        # Assert that the extracted times match the expected ones
        self.assertEqual(extract_data("times_24_hour", text), expected_times_24_hour)
        self.assertEqual(extract_data("times_12_hour", text), expected_times_12_hour)

    def test_extract_html_tags(self):
        """
        Test extracting HTML tags from a text.
        """
        # Input text containing HTML tags
        text = '<p>This is a paragraph.</p> <div class="example"></div>'
        # Expected HTML tags
        expected_tags = ['<p>', '</p>', '<div class="example">', '</div>']
        # Assert that the extracted HTML tags match the expected ones
        self.assertEqual(extract_data("html_tags", text), expected_tags)

    def test_extract_hashtags(self):
        """
        Test extracting hashtags from a text.
        """
        # Input text containing hashtags
        text = "Use #example and #ThisIsAHashtag in your posts."
        # Expected hashtags
        expected_hashtags = ['#example', '#ThisIsAHashtag']
        # Assert that the extracted hashtags match the expected ones
        self.assertEqual(extract_data("hashtags", text), expected_hashtags)

    def test_extract_currency_amounts(self):
        """
        Test extracting currency amounts from a text.
        """
        # Input text containing currency amounts
        text = "The cost is $19.99 or $1,234.56."
        # Expected currency amounts
        expected_amounts = ['$19.99', '$1,234.56']
        # Assert that the extracted currency amounts match the expected ones
        self.assertEqual(extract_data("currency_amounts", text), expected_amounts)

    def test_process_text(self):
        """
        Test processing a text and extracting all relevant data types.
        """
        # Input text containing various data types
        text = """
            Contact: user@example.com
            URL: https://www.example.com
            Phone: (123) 456-7890
            Credit Card: 1234 5678 9012 3456
            Time: 14:30
            Hashtag: #example
            Price: $19.99
            <div class="test">HTML content</div>
        """
        # Expected output with all extracted data types
        expected_output = {
            "emails": ['user@example.com'],
            "urls": ['https://www.example.com'],
            "phone_numbers": ['(123) 456-7890'],
            "credit_cards": ['1234 5678 9012 3456'],
            "times_24_hour": ['14:30'],
            "times_12_hour": [],
            "html_tags": ['<div class="test">', '</div>'],
            "hashtags": ['#example'],
            "currency_amounts": ['$19.99'],
        }
        # Assert that the processed text matches the expected output
        self.assertEqual(process_text(text), expected_output)

if __name__ == '__main__':
    unittest.main()