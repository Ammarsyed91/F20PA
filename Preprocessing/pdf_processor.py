# pdf_processor.py
import os
import re
import json
import logging
import pdfplumber
from nltk.corpus import stopwords
from config import CONFIG  # Import at the top

class PDFProcessor:
    def __init__(self):
        try:
            self.stop_words = set(stopwords.words('english'))
        except LookupError:
            import nltk
            nltk.download('stopwords')
            self.stop_words = set(stopwords.words('english'))
    
    def process_page(self, page):
        """Process a single page"""
        try:
            raw_text = page.extract_text()
            if raw_text:
                cleaned_text = re.sub(r'\s+', ' ', raw_text).strip()
                cleaned_text = ' '.join(
                    word for word in cleaned_text.split() 
                    if word.lower() not in self.stop_words
                )
                return cleaned_text
            return ""
        except Exception as e:
            logging.error(f"Error processing page: {e}")
            return ""

    def process_single_pdf(self, file_info):
        """Process a single PDF file page by page"""
        file_name = file_info['file_name']
        root_dir = file_info['root_dir']
        pdf_path = os.path.join(root_dir, file_name)
        doc_id = os.path.splitext(file_name)[0]
        output_path = os.path.join(CONFIG['OUTPUT_FOLDER'], f"{doc_id}.jsonl")

        try:
            with pdfplumber.open(pdf_path) as pdf:
                with open(output_path, 'w', encoding='utf-8') as out_file:
                    chunk_num = 1
                    current_chunk = ""
                    
                    for page_num, page in enumerate(pdf.pages, 1):
                        page_text = self.process_page(page)
                        if not page_text:
                            continue
                            
                        current_chunk += " " + page_text
                        
                        if len(current_chunk) >= CONFIG['CHUNK_SIZE']:
                            chunks = self.chunk_text(current_chunk, CONFIG['CHUNK_SIZE'], CONFIG['OVERLAP'])
                            for chunk in chunks:
                                record = {
                                    "doc_id": doc_id,
                                    "chunk_num": chunk_num,
                                    "text": chunk
                                }
                                out_file.write(json.dumps(record, ensure_ascii=False) + '\n')
                                chunk_num += 1
                            
                            current_chunk = current_chunk[-CONFIG['OVERLAP']:]
                    
                    if current_chunk:
                        record = {
                            "doc_id": doc_id,
                            "chunk_num": chunk_num,
                            "text": current_chunk.strip()
                        }
                        out_file.write(json.dumps(record, ensure_ascii=False) + '\n')
            
            return True
        except Exception as e:
            logging.error(f"Failed to process {pdf_path}: {e}")
            return False

    def chunk_text(self, text, chunk_size, overlap):
        """Generate chunks of text"""
        chunks = []
        start = 0
        text_length = len(text)

        while start < text_length:
            end = min(start + chunk_size, text_length)
            chunk = text[start:end].strip()
            chunks.append(chunk)
            start += (chunk_size - overlap)
            
            if overlap >= chunk_size:
                break
                
        return chunks