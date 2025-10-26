from PyPDF2 import PdfReader
 
with open("Loops.pdf", 'rb') as file: #rb beacause its non txt file 
    reader = PdfReader(file)
    text = ""
 
    for reader in reader.pages:
        text += reader.extract_text()
 
 
    with open("pdf_data.txt", "a") as file:
        file.write(text)

    