from PyPDF2 import PdfMerger

merger = PdfMerger()

# Get number of PDFs
n = int(input("How many pdfs do you want to merge?\n"))

# Collect PDF filenames
pdfs = []
for i in range(n):
    pdf_name = input(f"Enter the name of pdf {i+1}: ")
    pdfs.append(pdf_name)

# Append each PDF to the merger
for pdf in pdfs:
    merger.append(pdf)

# Write the merged PDF
merger.write("merged.pdf")
merger.close()

print("PDFs merged successfully!")