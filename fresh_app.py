import streamlit as st
import pandas as pd

# --------------------------------------------------
# Page Config
# --------------------------------------------------
st.set_page_config(
    page_title="Research & Data Science Portfolio",
    page_icon="🔬",
    layout="wide"
)

# --------------------------------------------------
# Custom Styling
# --------------------------------------------------
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #007bff;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# --------------------------------------------------
# Initialize Session State (Crucial for persistence)
# --------------------------------------------------
if "education" not in st.session_state:
    st.session_state.education = []
if "experience" not in st.session_state:
    st.session_state.experience = []
if "projects" not in st.session_state:
    st.session_state.projects = []
if "publications" not in st.session_state:
    st.session_state.publications = []

# --------------------------------------------------
# Sidebar Navigation
# --------------------------------------------------
st.sidebar.title("📌 Navigation")
menu = st.sidebar.radio(
    "Go to:",
    ["Profile", "Education", "Experience", "Research Interests", "Projects", "Publications", "STEM Explorer", "Contact"]
)

# --------------------------------------------------
# 1. Profile Section
# --------------------------------------------------
if menu == "Profile":
    st.title("👤 Researcher Profile")
    col1, col2 = st.columns([1, 2])
    
    with col1:
        name = st.text_input("Name", "Dr. Kevin Lee")
        field = st.text_input("Field", "Data Science & AI")
        inst = st.text_input("Institution", "Tech Innovation University")
    
    with col2:
        bio = st.text_area("Short Bio", "Researcher focused on scalable data-driven systems.")
        st.info(f"**Current Status:** {field} at {inst}")

# --------------------------------------------------
# 2. Education & Experience (Combined Logic)
# --------------------------------------------------
elif menu in ["Education", "Experience"]:
    st.title(f" {menu}")
    
    # Selection logic based on menu
    mode = "education" if menu == "Education" else "experience"
    
    with st.expander(f"➕ Add New {menu}"):
        if mode == "education":
            c1, c2 = st.columns(2)
            deg = c1.text_input("Degree")
            sch = c2.text_input("School")
            yr = st.text_input("Year")
            if st.button("Save Education"):
                st.session_state.education.append({"Degree": deg, "School": sch, "Year": yr})
        else:
            role = st.text_input("Role")
            org = st.text_input("Organization")
            dur = st.text_input("Duration")
            if st.button("Save Experience"):
                st.session_state.experience.append({"Role": role, "Org": org, "Dur": dur})

    # Display items
    items = st.session_state.education if mode == "education" else st.session_state.experience
    for item in items:
        st.write(f"---")
        st.write(item)

# --------------------------------------------------
# 3. Publications (With Dataframe View)
# --------------------------------------------------
elif menu == "Publications":
    st.title("📚 Publications")
    
    with st.expander("Add Publication"):
        title = st.text_input("Title")
        yr = st.number_input("Year", 2000, 2026, 2024)
        if st.button("Add"):
            st.session_state.publications.append({"Title": title, "Year": yr})
            
    if st.session_state.publications:
        pub_df = pd.DataFrame(st.session_state.publications)
        st.table(pub_df) # Table looks cleaner for academic lists

# --------------------------------------------------
# 4. STEM Explorer (The "Data Science" Part)
# --------------------------------------------------
elif menu == "STEM Explorer":
    st.title("📊 STEM Data Explorer")
    
    uploaded_file = st.file_uploader("Upload your research CSV", type="csv")
    
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.write("### Data Preview")
        st.dataframe(df.head())
        
        st.write("### Quick Visualization")
        columns = df.columns.tolist()
        x_axis = st.selectbox("Select X axis", columns)
        y_axis = st.selectbox("Select Y axis", columns)
        st.line_chart(df.set_index(x_axis)[y_axis])
    else:
        st.info("Upload a CSV to analyze your own data, or view the sample below:")
        sample_data = pd.DataFrame({"Trial": [1,2,3,4], "Result": [10, 25, 14, 30]})
        st.bar_chart(sample_data.set_index("Trial"))

# --------------------------------------------------
# 5. Contact
# --------------------------------------------------
elif menu == "Contact":
    st.title("📬 Contact")
    with st.form("contact_form"):
        email = st.text_input("Your Email")
        msg = st.text_area("Message")
        submit = st.form_submit_button("Send")
        if submit:
            st.success("Message 'sent' (this is a simulation)!")
