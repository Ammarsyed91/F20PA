# pdf_scanner.py
import os
import json
from pathlib import Path
from config import CONFIG

def scan_pdf_directory(pdf_folder):
    """Scans directory and creates batches of PDF files to process"""
    pdf_files = []
    
    for root, _, files in os.walk(pdf_folder):
        for file in files:
            if file.lower().endswith('.pdf'):
                pdf_files.append({
                    'file_name': file,
                    'root_dir': root,
                    'processed': False
                })
    
    # Save the file list
    Path(CONFIG['TEMP_FOLDER']).mkdir(parents=True, exist_ok=True)
    with open(os.path.join(CONFIG['TEMP_FOLDER'], 'pdf_inventory.json'), 'w') as f:
        json.dump(pdf_files, f)
    
    return len(pdf_files)