
# Retrieval-Augmented Generation (RAG) Pipeline for Dissertation

This repository contains two Jupyter notebooks that work together to build and use a Retrieval-Augmented Generation (RAG) system using your dissertation dataset. The system processes your JSONL files, builds a FAISS index for fast similarity search, and then uses a gated Llama model to generate responses based on retrieved context.

## Notebooks Overview

### 1. index_creation.ipynb

- **Purpose**:  
  Reads JSONL files from your dataset, processes the text, generates embeddings using SentenceTransformer, builds a FAISS index, and saves the index along with metadata files.
  
- **Usage**:  
  Run this notebook **locally on your PC**.  
  The notebook will process JSONL files from the directory `/Users/ammar/Desktop/Dissertation/Dataset` (or a specified folder), and save the following output files:
  - `my_index.idx` – the FAISS index file.
  - `all_texts.pkl` – list of processed text chunks.
  - `doc_ids.pkl` – list of document IDs.
  - `chunk_nums.pkl` – list of chunk numbers.

### 2. rag_pipeline-2.ipynb

- **Purpose**:  
  Loads the pre-built FAISS index and metadata files created by `index_creation.ipynb`, retrieves relevant context based on a user query, and uses a Llama-based text generation model to produce an answer.
  
- **Usage**:  
  It is recommended to run this notebook in **Google Colab** (or another cloud environment) for ease of resource management.  
  Before running, ensure that the FAISS index and metadata files from `index_creation.ipynb` are accessible (for example, via Google Drive).

## Prerequisites & Requirements

- **Python Version**: 3.6 or higher.
- **Libraries**:
  - For `index_creation.ipynb`:  
    `faiss-cpu`, `sentence-transformers`, `tqdm`, `numpy`, and standard Python libraries (`glob`, `json`, `os`, `pickle`, `logging`).
  - For `rag_pipeline-2.ipynb`:  
    `llama-cpp-python`, `langchain`, `sentence-transformers`, `openai==0.28.0`, `transformers`, `torch`, `accelerate`, `faiss-cpu`, `ipywidgets`, and `gradio`.
- **Data**:  
  - JSONL files must be stored in `/Users/ammar/Desktop/Dissertation/Dataset` for index creation.
- **Llama Model Access**:
  - The Llama model used in this project is gated. Users must request access, generate an access token with their account, and configure their environment with this token before running the Llama model.

## Setup and Execution

### Step 1: Create the FAISS Index Locally

1. **Clone the Repository**:
   ```bash
   git clone git@github.com:Ammarsyed91/F20PA.git
   cd F20PA
   ```
   **Open  `index_creation.ipynb`**:


**Configure the JSONL Directory**:

-   For my case I had configured it to use `/Users/ammar/Desktop/Dissertation/Dataset`, you may have to modify the path to fit your case  Modify the path in the notebook if needed.

**Run the Notebook**:

-   Execute the notebook cells sequentially.
-   The notebook will process the dataset, create the FAISS index, and save the files:
    -   `my_index.idx`
    -   `all_texts.pkl`
    -   `doc_ids.pkl`
    -   `chunk_nums.pkl`


### Step 2: Run the RAG Pipeline on Google Colab

**Important: I have used Google Colab for this script due to which these instructions are fit for Google Colab only. If you prefer using other environment, the steps may vary.** 

1.  **Open  `rag_pipeline-2.ipynb`  in Google Colab**:
    -   Upload or mount your project repository or the relevant files in Colab.
2.  **Ensure Data Accessibility**:
    -   Make sure that the FAISS index and metadata files generated in Step 1 are available in your  environment and the correct path is configured.
        
3.  **Install Required Libraries in Colab**:
    
    -   The notebook includes an installation cell for the required packages:      
        `!pip install llama-cpp-python langchain sentence-transformers openai==0.28.0 transformers torch "accelerate>=0.26.0" faiss-cpu ipywidgets gradio` 
        
4.  **Log in and Mount Google Drive**:
    
    -   Follow instructions in the notebook to log in to Hugging Face (if necessary) and mount your Google Drive to access the FAISS index files.
        
5.  **Run the Notebook**:
    
    -   Execute the notebook cells to load the FAISS index and metadata, set up the query processing, and generate responses using the Llama model.
        

## Additional Notes

-   **Gated Llama Model**:  
    The Llama model requires special access.
    -   Visit the HuggingFace website.
    -   Request for the Model access or join the waitlist as required.
    -   Once approved, generate your access token.
    -   Ensure the token is correctly configured in your environment when running  `rag_pipeline-2.ipynb`.
        
