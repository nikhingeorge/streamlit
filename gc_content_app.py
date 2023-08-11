import streamlit as st
from pathlib import Path
import pandas as pd
from Bio import SeqIO
from Bio.SeqUtils import gc_fraction

root = Path("datasets")
root.mkdir(exist_ok=True)

def gcDataFrame(path):
    gcContent = [(record.id, gc_fraction(record.seq)) for record in SeqIO.parse(path,"fasta")]
    df = pd.DataFrame(gcContent, columns = ["Seq Id", "GC Fraction"])
    return df

def upload_dataset_using_file():
    uploaded_file = st.file_uploader("Select FASTA File", type="fasta")
    if uploaded_file is not None:
        data = uploaded_file.getvalue()
        path = root.joinpath(uploaded_file.name)
        path.write_bytes(data)
        path = root.joinpath(uploaded_file.name)
        df = gcDataFrame(path)
        st.header("GC Fraction as Table")
        st.dataframe(df, hide_index = True)
        st.bar_chart(df, x= "Seq Id", y = "GC Fraction")

def upload_dataset():
    st.title("GC Viewer")
    st.markdown("GC Viewer is a simple application to explore GC fractions of all sequences in a FASTA file.")
    st.markdown("Select a FASTA file to get started.")
    st.header("Select a FASTA file")
    upload_dataset_using_file()
    
    

upload_dataset()
