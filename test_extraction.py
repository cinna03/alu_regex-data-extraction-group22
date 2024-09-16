import unittest
from extraction import extract_data, process_text

class TestRegexExtraction(unittest.TestCase):

    def test_extract_emails(self):
        text = "Contact us at user@example.com or firstname.lastname@company.co.uk."
        expected_emails = ['user@example.com', 'firstname.lastname@company.co.uk']
        self.assertEqual(extract_data("emails", text), expected_emails)

    def test_extract_urls(self):
        text = "Visit https://www.example.com or http://subdomain.example.org/page."
        expected_urls = ['https://www.example.com', 'http://subdomain.example.org/page']
        self.assertEqual(extract_data("urls", text), expected_urls)

    def test_extract_phone_numbers(self):
        text = "Call me at (123) 456-7890 or 123-456-7890."
        expected_phone_numbers = ['(123) 456-7890', '123-456-7890']
        self.assertEqual(extract_data("phone_numbers", text), expected_phone_numbers)

    def test_extract_credit_cards(self):
        text = "Credit card: 1234 5678 9012 3456 or 1234-5678-9012-3456."
        expected_credit_cards = ['1234 5678 9012 3456', '1234-5678-9012-3456']
        self.assertEqual(extract_data("credit_cards", text), expected_credit_cards)

    def test_extract_times(self):
        text = "The meeting is at 14:30 or 2:30 PM."
        expected_times_24_hour = ['14:30']
        expected_times_12_hour = ['2:30 PM']
        self.assertEqual(extract_data("times_24_hour", text), expected_times_24_hour)
        self.assertEqual(extract_data("times_12_hour", text), expected_times_12_hour)

    def test_extract_html_tags(self):
        text = '<p>This is a paragraph.</p> <div class="example"></div>'
        expected_tags = ['<p>', '</p>', '<div class="example">', '</div>']
        self.assertEqual(extract_data("html_tags", text), expected_tags)

    def test_extract_hashtags(self):
        text = "Use #example and #ThisIsAHashtag in your posts."
        expected_hashtags = ['#example', '#ThisIsAHashtag']
        self.assertEqual(extract_data("hashtags", text), expected_hashtags)

    def test_extract_currency_amounts(self):
        text = "The cost is $19.99 or $1,234.56."
        expected_amounts = ['$19.99', '$1,234.56']
        self.assertEqual(extract_data("currency_amounts", text), expected_amounts)

    def test_process_text(self):
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
        self.assertEqual(process_text(text), expected_output)

if __name__ == '__main__':
    unittest.main()

