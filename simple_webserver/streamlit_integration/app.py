import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
# from langchain.vectorstores import FAISS
# from langchain.llms import OpenAI
# from langchain.chains.question_answering import load_qa_chain
# from langchain.callbacks import get_openai_callback

with st.sidebar:
    st.title('💬 NexDoc App')
    st.markdown('''
    ## About
    This is an LLM-powered chatbot built using:
    - [Streamlit](https://streamlit.io/)
    - [LangChain](https://python.langchain.com/)
    - [Google Vertex AI PaLM](https://platform.openai.com/docs/models)
 
    ''')
  
   

def main():
	st.header("Chat with Your PDF 💬")

	pdf = st.file_uploader("Upload your PDF", type='pdf')

	if pdf is not None:
		pdf_reader = PdfReader(pdf)

		text = ""
		for page in pdf_reader.pages:
			text += page.extract_text()

		text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
            )
		chunks = text_splitter.split_text(text=text)

		st.write(chunks)

	count = 1
	query = st.text_input("Ask questions about your PDF file:", key = count)
	while query:
		st.write("Return Response from LLM Model")
		count = count + 1
		query = st.text_input(label='Hey there', key=count, label_visibility='collapsed')
		#st.write("Return Response from LLM Model")
		




if __name__ == '__main__':
	main()