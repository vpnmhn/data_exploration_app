import streamlit as st
import pandas as pd
import ydata_profiling
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report



def main():
    st.set_page_config(page_title="CSVExplorer",page_icon=":bar_chart:")
    st.title("CSVExplorer:bar_chart:")
    st.header('Explore a dataset:bar_chart:')
    st.markdown("This app will help you do data exploration")
    st.sidebar.header("User input features")
    file = st.sidebar.file_uploader("Files uploader", type=['csv'])
    if file is not None:
        st.markdown('---')
        df =  pd.read_csv(file)
    
        profile = ProfileReport(df, title="Profiling Report")
        st.title("Detailed report")
        st.write(df)

        st_profile_report(profile)

    else:
        st.markdown('---')
        st.write("You did not upload a new file")


if __name__=="__main__":
    main()

