# Dissertation RAG System

This repository implements a Retrieval-Augmented Generation (RAG) pipeline for a dissertation dataset. It is organized into two main parts:

- **Preprocessing**: Processes your dataset and builds a FAISS index along with the required metadata.
- **Model Implementation**: Uses the pre-built FAISS index to retrieve relevant context and generate responses using a gated Llama model.

> **Note:**  
> It is assumed that you already have the dataset downloaded. Throughout the files, you will need to update file paths according to your local setup.

## Repository Structure

- **Preprocessing**  
  Contains the notebook `index_creation.ipynb` which:
  - Reads JSONL files.
  - Processes the text and extracts metadata.
  - Generates embeddings and builds a FAISS index.
  - Saves the FAISS index and metadata files.

- **Model Implementation**  
  Contains the notebook `rag_pipeline-2.ipynb` which:
  - Loads the pre-built FAISS index and metadata files.
  - Retrieves relevant texts based on user queries.
  - Uses a gated Llama model to generate answers.
  - **Important**: The Llama model is gated; you must request access, generate an access token with your account, and configure your environment accordingly.

## Setup and Execution

1. **Download Dataset**:  
   Ensure that your dataset is downloaded and available.

2. **Run Preprocessing**:  
   - Navigate to the **Preprocessing** directory.
   - Open and run `index_creation.ipynb` on your local machine.
   - Update file paths as needed.
   - This will create the necessary FAISS index and metadata files.

3. **Run Model Implementation**:  
   - Once the FAISS index and metadata files are created, navigate to the **Model Implementation** directory.
   - Open and run `rag_pipeline-2.ipynb` (preferred to run on Google Colab).
   - Update file paths as needed to ensure the notebook can access the FAISS index and metadata.
   - Follow the instructions in the notebook to log in, mount any required storage, and configure your Llama model access token.

## Additional Information

For more details about the configuration and usage of each script, please refer to the README files located in their respective directories.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- **FAISS** for efficient similarity search.
- **Hugging Face Transformers** for state-of-the-art language models.
- **SentenceTransformers** for embedding generation.
- The research community for providing these tools and models.
