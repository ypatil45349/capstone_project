from langchain_text_splitters import RecursiveCharacterTextSplitter
from pypdf import PdfReader


def read_pdf(file_path):

    reader = PdfReader(file_path)

    text = ""

    for page in reader.pages:
        text += page.extract_text()

    return text


def chunk_text(text):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_text(text)

    return chunks

def process_document(file_path):

    # Step 1: Read PDF
    text = read_pdf(file_path)

    # Step 2: Chunk the text
    chunks = chunk_text(text)

    return chunks