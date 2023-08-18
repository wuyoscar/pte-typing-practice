import os
import re
import argparse
import urllib.parse
import webbrowser
class Converter:
    
    def __init__(self):
        self.source_directory = 'raw_txt'
        self.destination_directory = 'fast_txt'
    
    @staticmethod
    def format_text(text):
        # Extract English words and punctuation
        items = re.findall(r'\b[a-zA-Z]+(?:-[a-zA-Z]+)*\'?[a-zA-Z]*\b|[.,!?;]', text)
        
        # Remove duplicates but maintain order
        ordered_unique_items = []
        for item in items:
            if item not in ordered_unique_items:
                ordered_unique_items.append(item)
        
        # Join the items with '|'
        formatted_text = '|'.join(items)
        return formatted_text
    
    def convert_file(self, filename):
        input_filepath = os.path.join(self.source_directory, filename)
        
        with open(input_filepath, 'r') as file:
            content = file.read()
        
        # Format the content
        result = self.format_text(content)
        
        # Create output filepath
        output_filename = f"{os.path.splitext(filename)[0]}_fast.txt"
        output_filepath = os.path.join(self.destination_directory, output_filename)
        
        # Write the result to the output file
        with open(output_filepath, 'w') as file:
            file.write(result)
        return result 
    def process_directory(self):
        # Check and create destination directory if it doesn't exist
        if not os.path.exists(self.destination_directory):
            os.makedirs(self.destination_directory)
        
        # Loop through each file in the source directory
        for filename in os.listdir(self.source_directory):
            if filename.endswith(".txt"):
                self.convert_file(filename)
                
    def generate_link(self, formatted_text, duration=300, shuffle=0):
        base_url = "https://10fastfingers.com/widget/typingtest"
        params = {
            "dur": duration,
            "rand": shuffle,
            "words": formatted_text
        }
        url = f"{base_url}?{urllib.parse.urlencode(params)}"
        return url
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert English text with punctuation in files to specified format.')
    
    # Exclusive group ensures that only one of the arguments can be specified
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--file', type=str, help='Specific file to convert from raw_txt directory.')
    group.add_argument('--directory', action='store_true', help='Process entire raw_txt directory.')
    group.add_argument('--open', type=str, help='Generate a 10fastfingers link using the formatted text from the specified file.')
        
    args = parser.parse_args()
    
    converter = Converter()
    
    if args.file:
        converter.convert_file(args.file)
    elif args.directory:
        converter.process_directory()
    elif args.open:
        formatted_text = converter.convert_file(args.open)
        link = converter.generate_link(formatted_text)
        webbrowser.open(link)