# config.py
import os
import multiprocessing

# Define absolute paths
PDF_FOLDER = "/Users/ammar/Desktop/Dissertation/FullProcessTrial/PDFs/"
OUTPUT_FOLDER = "/Users/ammar/Desktop/Dissertation/FullProcessTrial/OutputPDF/"
TEMP_FOLDER = os.path.join(OUTPUT_FOLDER, "temp")

CONFIG = {
    'PDF_FOLDER': PDF_FOLDER,                  # Absolute path to read PDFs
    'OUTPUT_FOLDER': OUTPUT_FOLDER,            # Absolute path to write processed files
    'TEMP_FOLDER': TEMP_FOLDER,                # Temp folder inside OUTPUT_FOLDER
    'BATCH_SIZE': 100,
    'CHUNK_SIZE': 2000,
    'OVERLAP': 200,
    'MAX_WORKERS': max(1, multiprocessing.cpu_count() - 1),
    'RETRIES': 1
}
