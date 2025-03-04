# 📄 Convert All Individual DOCX's in a Folder to Individual PDF's 🚀  

This project **converts Microsoft Word DOCX files to PDFs** using Python.  
It allows users to **select a folder of DOCX files** and specify a destination folder for the PDFs.  

## 📌 Features  
✅ **Batch converts** all DOCX files in a folder to PDFs  
✅ **User-friendly interface** using Tkinter file selection  
✅ **Simple and fast** with minimal dependencies  

---

## 📥 Installation  

Ensure you have **Python 3.8+** installed.  

### Install dependencies:  
```
pip install docx2pdf
```
---

## 🔑 Usage  

### 1️⃣ Run the script  
```
python docx_to_pdf.py
```
This will:  
- Prompt you to **select a folder containing DOCX files**  
- Ask where you want to **save the converted PDFs**  
- Convert all DOCX files to PDFs  

---

## 📊 Output Files  
The converted PDFs will be saved in the folder you select.  

---

## 🛠 Customization  

### Convert a single file instead of a folder:  
Modify:  
```
convert(word_path, pdf_path)
```
To:  
```
convert("example.docx", "example.pdf")
```
This will convert just one file.

---

## 📜 License  
This project is **MIT Licensed** – feel free to use and modify.  
