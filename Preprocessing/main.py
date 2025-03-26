#main.py
# main.py
import os
import logging
import sys
from logging.handlers import RotatingFileHandler
from config import CONFIG
from pdf_scanner import scan_pdf_directory
from batch_manager import run_batch_processing

def setup_logging():
    logging.basicConfig(
        level=logging.WARNING,
        format='%(asctime)s %(levelname)s:%(message)s',
        handlers=[
            logging.StreamHandler(sys.stdout),
            RotatingFileHandler("processing.log", maxBytes=10**7, backupCount=5)
        ]
    )

if __name__ == "__main__":
    setup_logging()
    logging.warning("Starting PDF processing pipeline")
    
    # Create necessary directories
    os.makedirs(CONFIG['OUTPUT_FOLDER'], exist_ok=True)
    os.makedirs(CONFIG['TEMP_FOLDER'], exist_ok=True)
    
    # Scan PDFs and create inventory
    total_pdfs = scan_pdf_directory(CONFIG['PDF_FOLDER'])
    logging.warning(f"Found {total_pdfs} PDFs to process")
    
    # Run batch processing
    run_batch_processing()
    
    logging.warning("Processing complete!")