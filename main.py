import streamlit as st
from PyPDF2 import PdfReader
st.markdown("""
<style>
div[data-testid="stExpander"] {
    background-color: white;
    border-radius: 10px;
}

div[data-testid="stExpander"] p {
    color: black !important;
}

.streamlit-expanderHeader {
    color: black !important;
}
</style>
""", unsafe_allow_html=True)
st.title("Pdf Text Extractor")

st.divider()
st.subheader("Upload here")
upload_file = st.file_uploader("Upload your file here", type = ["pdf"])

st.divider()


if upload_file:
    reader = PdfReader(upload_file)

    text = ""

    for page in reader.pages:
        text += page.extract_text()

    number_of_pages = len(reader.pages)
    words = len(text.split())

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Number of pages", number_of_pages)

    with col2:
        st.metric("Number of words", words)

    search_word = st.text_input("Word wise Pages search (Enter a word to search in the PDF)")

    if search_word:
        search_word_lower = search_word.lower()
        found = False
        for i, page in enumerate(reader.pages):
            page_text = page.extract_text()
            if search_word_lower in page_text.lower():
                found = True
                with st.expander(f"Page {i+1}"):
                    st.code(page_text, language=None)
                st.divider()
        if not found:
            st.warning(f"The word '{search_word}' was not found in the PDF.")

    for i, page in enumerate(reader.pages):
        with st.expander(f"Page {i+1}"):
         st.code(page.extract_text(), language=None)
        st.divider()