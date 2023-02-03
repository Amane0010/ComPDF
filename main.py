import streamlit as st
import PyPDF2
import os

def merge_pdf (pdf_files : list, pdf_name : str) -> str:
    merger = PyPDF2.PdfMerger()
    for pdf in pdf_files:
        merger.append(pdf)

    pdf_path = os.path.abspath(f"{pdf_name}.pdf")
    merger.close()
    return f"{pdf_name}.pdfを生成します", pdf_path

def open_pdf(pdf_path: str, name: str):
    with open(pdf_path, "rb") as pdf_file:
        pdf = pdf_file.read()

    st.download_button(
        label="Download PDF",
        data=pdf,
        file_name=f"{name}.pdf",
        mime='application/octet-stream',
        )


#タイトル
st.title("MyApp")

#結合後のpdfファイルの名前
merged_pdf_name= st.text_input("Name of the merged pdf file","my_material")
st.text("※拡張子は入力不要")

#pdfのアップロード
uploaded_file1 = (st.file_uploader("Choose your .pdf file1", type="pdf"))
uploaded_file2 = (st.file_uploader("Choose your .pdf file2", type="pdf"))
if uploaded_file1 and uploaded_file2 is not None:
    uploaded_files = [uploaded_file1, uploaded_file2]
    mes, pdf_path = merge_pdf(uploaded_files, merged_pdf_name)
    st.text(mes)
    open_pdf(pdf_path,merged_pdf_name)
