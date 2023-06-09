from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import ElasticVectorSearch, Pinecone, Weaviate, FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback as cb
import pickle
import os
import streamlit as st

st.set_page_config(
    page_title="SQA Manual Chatbot",
    page_icon="./img/favicon.png"
)



os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]


with open('jas_manual_model-linux.pkl', 'rb') as f:
    data = pickle.load(f)

# with open('jas_manual_model.pkl', 'rb') as f:
#     data = pickle.load(f)

chain = load_qa_chain(OpenAI(), chain_type = "stuff")



st.image("./img/jas_logo.png", width=150)
st.markdown("<h1 style='text-align: center;'>JAS Manual Chatbot</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: justify;'>Chatbot ini dibuat untuk membantu anda menemukan jawaban/materi/list dari JAS Manual yang dimiliki oleh tim Safety Quality Assurance (SQA). Anda dapat bertanya menggunakan bahasa Indonesia dan Bahasa Inggris.</p>", unsafe_allow_html=True)





prompt = st.text_area("Input your question below:")
col1, col2, col3 , col4, col5, col6, col7 = st.columns(7)

with col1:
    pass
with col2:
    pass
with col3:
    pass
with col4:
    pass
with col5 :
    pass
with col6 :
    submit_button = st.button("Submit")
with col7 :
    reset_button = st.button("Reset")




if submit_button:
    if prompt == '':
        st.write('There is nothing to be answered...')
    else:
        docs = data.similarity_search(prompt)
        answer = chain.run(input_documents=docs, question=prompt)
        st.write(answer)

if reset_button:
    st.empty()


# st.write(
#     "Has environment variables been set:",
#     os.environ["OPENAI_API_KEY"] == st.secrets["OPENAI_API_KEY"],
# )


