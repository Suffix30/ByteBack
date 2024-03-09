# backpack_analysis_script.py

import os

def analyze_file(file_path):
    try:
        # Open the file and read its contents
        with open(file_path, 'rb') as file:
            contents = file.read().decode('utf-8', errors='replace')  # Try decoding with UTF-8
            
        # Get file size in bytes
        file_size = os.path.getsize(file_path)
        
        # Count the number of lines in the file
        num_lines = contents.count('\n') + 1
        
        # Count the number of words in the file
        words = contents.split()
        num_words = len(words)
        
        # Calculate average word length
        total_word_length = sum(len(word) for word in words)
        average_word_length = total_word_length / num_words if num_words > 0 else 0
        
        # Check if the file contains specific keywords related to malware
        keywords = ['virus', 'malware', 'trojan', 'ransomware']
        found_keywords = [keyword for keyword in keywords if keyword in contents.lower()]
        
        # Determine file type based on extension
        file_type = os.path.splitext(file_path)[1].lower()
        
        # Analyze file type
        if file_type == '.exe':
            file_analysis = "Executable file (.exe)"
            # Add more analysis specific to executable files if needed
        elif file_type == '.txt':
            file_analysis = "Text file (.txt)"
            # Add more analysis specific to text files if needed
        else:
            file_analysis = "Unknown file type"
        
        # Construct analysis results
        analysis_results = f"Analysis results for {file_path}:\n" \
                           f"File size: {file_size} bytes\n" \
                           f"Number of lines: {num_lines}\n" \
                           f"Number of words: {num_words}\n" \
                           f"Average word length: {average_word_length:.2f} characters\n" \
                           f"Keywords found: {', '.join(found_keywords)}\n" \
                           f"File type: {file_analysis}"
        
        return analysis_results
    
    except FileNotFoundError:
        return f"Error: File {file_path} not found."
    except Exception as e:
        return f"Error analyzing file: {e}"
