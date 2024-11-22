import streamlit as st
import pandas as pd
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    st.title("insert csv app")

    st.subheader("csv upload")
    uploaded_file = st.file_uploader("csv file", type=["csv"])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("preview:")
        st.dataframe(df)

        save_path = "data/"
        os.makedirs(save_path, exist_ok=True)
        file_path = os.path.join(save_path, uploaded_file.name)

        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success(f"file saved at {file_path}")

        st.write("file:", file_path)
    else:
        st.warning("upload a csv")

if __name__ == "__main__":

    main()

    logger.info("Application Container started.")

