import streamlit as st  # pip install streamlit
import pandas as pd  # pip install pandas

from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode, ColumnsAutoSizeMode

# Config 
st.set_page_config(
    page_title='AG Excel',
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={}
)

st.title('AG-Grid For Excel 📊')
uploaded_file = st.file_uploader('Choose a XLSX file', type='xlsx')

if uploaded_file:
    st.toast(':green[Success]', icon='✅')
    
    with st.expander(f"**📉 :blue[Data Table - {uploaded_file.name[:-5]}]**",expanded= True):
        # Read Fils
        df = pd.read_excel(uploaded_file, engine='openpyxl')
        
        # AG-Grid
        gb = GridOptionsBuilder.from_dataframe(df)
        gb.configure_pagination(paginationAutoPageSize=True)
        gb.configure_side_bar(columns_panel=True)
        gridOptions = gb.build()
        
        # Select Fit
        fit = st.selectbox("Select Fit", ["FIT CONTENTS", "FIT ALL COLUMNS TO VIEW"])
        if fit == "FIT CONTENTS":
            data_table = AgGrid(df,
                gridOptions = gridOptions,
                update_mode = GridUpdateMode.FILTERING_CHANGED,
                columns_auto_size_mode = ColumnsAutoSizeMode.FIT_CONTENTS,
                enable_enterprise_modules = True,
                allow_unsafe_jscode = True,
                theme="streamlit"
            )
        else:
            data_table = AgGrid(df,
                gridOptions = gridOptions,
                update_mode = GridUpdateMode.FILTERING_CHANGED,
                columns_auto_size_mode = ColumnsAutoSizeMode.FIT_ALL_COLUMNS_TO_VIEW,
                enable_enterprise_modules = True,
                allow_unsafe_jscode = True,
                theme="streamlit"
            )
