# batch_manager.py
import os
import json
import logging
from tqdm import tqdm
from config import CONFIG
from pdf_processor import PDFProcessor

def process_batch(start_idx, batch_size):
    """Process a batch of PDFs"""
    with open(os.path.join(CONFIG['TEMP_FOLDER'], 'pdf_inventory.json'), 'r') as f:
        pdf_files = json.load(f)
    
    batch = pdf_files[start_idx:start_idx + batch_size]
    processor = PDFProcessor()
    
    successful = []
    failed = []
    
    for file_info in batch:
        if processor.process_single_pdf(file_info):
            successful.append(file_info['file_name'])
        else:
            failed.append(file_info['file_name'])
    
    return successful, failed

def run_batch_processing():
    """Main function to manage batch processing"""
    with open(os.path.join(CONFIG['TEMP_FOLDER'], 'pdf_inventory.json'), 'r') as f:
        pdf_files = json.load(f)
    
    total_pdfs = len(pdf_files)
    total_batches = (total_pdfs + CONFIG['BATCH_SIZE'] - 1) // CONFIG['BATCH_SIZE']
    
    successful_pdfs = []
    failed_pdfs = []
    
    with tqdm(total=total_pdfs, desc="Processing PDFs") as pbar:
        for batch_num in range(total_batches):
            start_idx = batch_num * CONFIG['BATCH_SIZE']
            batch_successful, batch_failed = process_batch(start_idx, CONFIG['BATCH_SIZE'])
            
            successful_pdfs.extend(batch_successful)
            failed_pdfs.extend(batch_failed)
            pbar.update(len(batch_successful) + len(batch_failed))
    
    results = {
        'successful': successful_pdfs,
        'failed': failed_pdfs
    }
    
    with open(os.path.join(CONFIG['OUTPUT_FOLDER'], 'processing_results.json'), 'w') as f:
        json.dump(results, f, indent=4)
