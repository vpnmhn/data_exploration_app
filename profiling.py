import streamlit as st
import pandas as pd
from io import StringIO
import ydata_profiling
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

def read_csv_with_metadata(uploaded_file):
    # Convert the uploaded file to a file-like object
    csv_file = StringIO(uploaded_file.getvalue().decode('utf-8'))

    # Read the file content line by line
    lines = csv_file.readlines()

    # Find the index where the metadata ends
    metadata_end_index = next((i for i, line in enumerate(lines) if not line.strip()), None)

    if metadata_end_index is not None and metadata_end_index < len(lines) - 1:
        # Use metadata_end_index to skip metadata rows
        df = pd.read_csv(StringIO(''.join(lines[metadata_end_index + 1:])), skip_blank_lines=True)
        return df
    else:
        # No metadata found, reset the file pointer and read the entire content
        csv_file.seek(0)
        df = pd.read_csv(csv_file, skip_blank_lines=True)
        return df

def main():
    st.set_page_config(page_title="CSVExplorer",page_icon=":bar_chart:")
    st.title("CSVExplorer:bar_chart:")
    st.header('Explore a dataset')
    st.markdown("This app will help you do data exploration!!")
    st.sidebar.header("User input features")
    file = st.sidebar.file_uploader("Files uploader", type=['csv'])
    if file is not None:
        st.markdown('---')
        df =  read_csv_with_metadata(file)
    
        profile = ProfileReport(df, title="Profiling Report")
        profile_2 = profile.to_html()

        st.title("Detailed report")
        st.write(df)

        st_profile_report(profile)

        # Provide a download link for the report
        st.download_button("Download Report", profile_2, file_name="report.html")

    else:
        st.markdown('---')
        st.write("You did not upload a new file")


if __name__=="__main__":
    main()

