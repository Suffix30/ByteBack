# backpack_analysis.py

import os
from backpack_analysis_script import analyze_file

def analyze_file_wrapper(file_path):
    try:
        # Check if the file exists
        if not os.path.exists(file_path):
            return f"Error: File {file_path} not found."
        
        # Analyze the file using the analysis script
        analysis_results = analyze_file(file_path)
        
        return analysis_results
    
    except Exception as e:
        return f"Error analyzing file: {e}"
