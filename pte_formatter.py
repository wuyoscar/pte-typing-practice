import os
import re
import argparse
import urllib.parse
import webbrowser
from autocorrect import Speller

class OConverter:
    def __init__(self, spell_check = True, skip_header = False ):
        # added spell check
        # added skip header 
        self.source_directory = 'raw_txt'
        self.destination_directory = 'fast_txt'
        self.spell = spell_check
        self.skip_header = skip_header

    
    def format_text(self, text):
        if self.skip_header:
            text = re.sub(r'-\s?.*?(?:\n|$)', '', text, flags=re.MULTILINE)
        
        # Extract English words and punctuation
        items = re.findall(r'\b[a-zA-Z]+(?:-[a-zA-Z]+)*\'?[a-zA-Z]*\b|[.,!?;]', text)
        
        if self.spell:
            # Combine the items into a single string
            combined_text = ' '.join(items)

            # Spell correct the combined text
            blob =  Speller()
            corrected_text = blob(combined_text)

            # Split the corrected text to get the items and format them
            items = corrected_text.split()        


        # Join the items with '|'
        formatted_text = '|'.join(items)
        return formatted_text
    
    def convert_file(self, filename):
        input_filepath = os.path.join(self.source_directory, filename)
        
        assert os.path.exists(input_filepath), f"Error: {input_filepath} does not exist!"
        
        with open(input_filepath, 'r', encoding='utf-8') as file:
            content = file.read()
        assert type(content) == str, f"Error: {content[:10]} does not exist!"
        
        # Format the content
        result = self.format_text(content)
        
        # Create output filepath
        output_filename = f"{os.path.splitext(filename)[0]}_fast.txt"
        output_filepath = os.path.join(self.destination_directory, output_filename)
        
        # Write the result to the output file
        with open(output_filepath, 'w') as file:
            file.write(self.format_lines(result))
        return result 
    
    def process_directory(self):
        # Check and create destination directory if it doesn't exist
        if not os.path.exists(self.destination_directory):
            os.makedirs(self.destination_directory)
        
        # Loop through each file in the source directory
        for filename in os.listdir(self.source_directory):
            if filename.endswith(".txt"):
                self.convert_file(filename)
                
    def generate_link(self, formatted_text, duration_inSec: int=540, shuffle=0) -> str:
        base_url = "https://10fastfingers.com/widget/typingtest"
        params = {
            "dur": duration_inSec,
            "rand": shuffle,
            "words": formatted_text
        }
        url = f"{base_url}?{urllib.parse.urlencode(params)}"
        return url
    
    def format_lines(self, text, max_line_length=87):
        words = text.split('|')
        lines = []
        current_line = []

        current_length = 0
        for word in words:
            if current_length + len(word) + 1 > max_line_length:  # +1 for the '|'
                lines.append('|'.join(current_line))
                current_length = 0
                current_line = []

            current_line.append(word)
            current_length += len(word) + 1  # +1 for the '|'

        # Append any remaining words to the lines
        if current_line:
            lines.append('|'.join(current_line))

        return '\n'.join(lines)
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert English text with punctuation in files to specified format.')
    
    # Exclusive group ensures that only one of the arguments can be specified
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--file', type=str, help='Specific file to convert from raw_txt directory.')
    group.add_argument('--directory', action='store_true', help='Process entire raw_txt directory.')
    group.add_argument('--open', type=str, help='Generate a 10fastfingers link using the formatted text from the specified file.')
        
    args = parser.parse_args()
    
    converter = OConverter()
    
    if args.file:
        converter.convert_file(args.file)
    elif args.directory:
        converter.process_directory()
    elif args.open:
        formatted_text = converter.convert_file(args.open)
        link = converter.generate_link(formatted_text)
        webbrowser.open(link)