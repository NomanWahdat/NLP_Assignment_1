# NLP_Assignment_1
Assignment 1: 
Introduction
The Advanced Regex Tool is a user-friendly application that helps you work with text using regular expressions (regex). It lets you extract and fix different types of information from your input. Here’s a quick look at what each part of the tool does:
Functionality Overview
1. Extract Domain
•	What it Does: This function finds the domain name from a URL.
•	Input: A URL (like https://www.example.com).
•	Output: The domain name (like example) or a message saying "No domain found."
2. Extract Dates
•	What it Does: It pulls out dates from a piece of text.
•	Input: Text that contains dates (like "I was born on 12/25/2000").
•	Output: A list of formatted dates (like ["2000-12-25"]) or "No dates found."
3. Extract Prices
•	What it Does: This function finds prices in different currencies.
•	Input: Text with prices (like "The book costs $12.99").
•	Output: A list of prices (like [('$', '12.99')]) or "No prices found."
4. Extract Hyperlinks
•	What it Does: It extracts links from HTML code.
•	Input: A string of HTML (like <a href="http://example.com">Link</a>).
•	Output: A list of URLs (like ["http://example.com"]) or "No hyperlinks found."
5. Correct Spelling
•	What it Does: It fixes common spelling mistakes in a text.
•	Input: Text with mistakes (like "I recived the letter").
•	Output: The corrected text (like "I received the letter").
6. Extract Addresses
•	What it Does: This function finds addresses in a text.
•	Input: Text that contains addresses (like "123 Main St").
•	Output: A list of addresses (like ["123 Main St"]) or "No addresses found."
7. Extract Hex Color Codes
•	What it Does: It pulls out hex color codes from CSS code.
•	Input: A string of CSS (like color: #FFFFFF;).
•	Output: A list of hex color codes (like ["FFFFFF"]) or "No hex color codes found."
