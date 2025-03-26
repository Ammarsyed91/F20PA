# PDF Processing Pipeline
This project provides a pipeline for processing PDF files. The pipeline scans a designated folder for PDFs, extracts and cleans text from each file, and splits the text into manageable chunks for further processing. It utilizes libraries such as [pdfplumber](https://github.com/jsvine/pdfplumber) for PDF extraction and [nltk](https://www.nltk.org/) for text processing.


## Prerequisites

  

-  **Python Version:** This project requires Python 3.8 or higher.

-  **Virtual Environment:** It is strongly recommended to use a virtual environment to manage dependencies and avoid conflicts.

  

## Setup Instructions
1.  **Clone the Repository**
Using SSH:

```bash
git clone git@github.com:Ammarsyed91/F20PA.git
cd F20PA
```
**Or, using HTTPS:**
```bash
git  clone  https://github.com/Ammarsyed91/F20PA.git
cd  F20PA
```
## Create and Activate a Virtual Environment
**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```
**On macOS/Linux:**
```
python -m venv venv
venv\Scripts\activate
```
## Install Dependencies
Ensure you have the requirements.txt file in the repository. Then run:
```
pip install -r requirements.txt
```
## Configure File Paths
Open the config.py file and adjust the following paths to match your system:
PDF_FOLDER: The absolute path where your PDF files are stored.
**OUTPUT_FOLDER**: The absolute path where processed files will be saved.
**TEMP_FOLDER**: A temporary folder inside the output folder for intermediate files.
Modify any other configuration settings as needed.

## Project Structure

- **config.py** — Configuration (paths, batch size, chunk size, workers)  
- **pdf_scanner.py** — Scans PDF directory and builds `pdf_inventory.json`  
- **pdf_processor.py** — Extracts, cleans, and chunks text from PDFs  
- **batch_manager.py** — Processes PDFs in batches; logs successes/failures  
- **main.py** — Entry point — sets up logging, scans PDFs, then runs processing  
- **requirements.txt** — Lists Python dependencies  

## Running the Script
Once you have configured your paths and installed the dependencies, run the pipeline with:

    python main.py
This command will 

 - Set up logging (with output to both the console and a rotating log file).
 - Scan the designated folder for PDFs.
 - Process the PDFs in batches, generating output files in the specified output folder
