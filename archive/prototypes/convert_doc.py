import os
import shutil
import pypandoc

desktop_dir = r"C:\Users\oladi\Desktop\Thesis\Auto_Doc_GIT_V6\Update the code"
os.makedirs(desktop_dir, exist_ok=True)
os.chdir(desktop_dir)

source_md = "Architecture_Overview_ISO33061.md"
dest_docx = "Architecture_Overview_ISO33061.docx"
dest_pdf = "Architecture_Overview_ISO33061.pdf"

print("Downloading pandoc...")
pypandoc.download_pandoc()

print("Converting to .docx...")
pypandoc.convert_file(source_md, 'docx', outputfile=dest_docx)
print(f"Saved .docx to {dest_docx}")

try:
    print("Converting to .pdf...")
    pypandoc.convert_file(source_md, 'pdf', outputfile=dest_pdf)
    print(f"Saved .pdf to {dest_pdf}")
except Exception as e:
    print(f"Failed to convert to .pdf directly via pandoc: {e}")
    print("Please use Word to save the generated .docx file as .pdf.")
