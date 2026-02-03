import streamlit as st
import pandas as pd

# --------------------------------------------------
# Page Config
# --------------------------------------------------
st.set_page_config(
    page_title="Research Portfolio | Mobile Payments SA",
    page_icon="🇿🇦",
    layout="wide"
)

# --------------------------------------------------
# Initialization (Persistence Logic)
# --------------------------------------------------
if "education" not in st.session_state:
    st.session_state.education = []
if "experience" not in st.session_state:
    st.session_state.experience = []
if "projects" not in st.session_state:
    st.session_state.projects = []

# --------------------------------------------------
# Sidebar Navigation
# --------------------------------------------------
st.sidebar.title("📌 Portfolio Navigation")
menu = st.sidebar.radio(
    "Go to:",
    ["Profile", "Education", "Experience", "Research Interests", "STEM Explorer", "Contact"]
)

# --------------------------------------------------
# 1. Profile Section
# --------------------------------------------------
if menu == "Profile":
    st.title("👤 Researcher Profile")
    st.info("**Research Topic:** The Adoption and Impact of Mobile Payment Systems on Financial Inclusion in South Africa.")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.text_input("Name", "Ritshidze Tshivhase")
        st.text_input("Field", "Data Science & AI")
    with col2:
        st.text_area("Bio", "Specializing in how digital wallets bridge the gap for the unbanked in SA.")

# --------------------------------------------------
# 2. Education 
# --------------------------------------------------
elif menu == "Education":
    st.title("🎓 Education")
    
    # Input Form
    with st.expander("➕ Add New Education"):
        with st.form("edu_form", clear_on_submit=True):
            deg = st.text_input("Degree")
            sch = st.text_input("University")
            yr = st.text_input("Year")
            if st.form_submit_button("Add Record"):
                if deg and sch:
                    st.session_state.education.append({"deg": deg, "sch": sch, "yr": yr})
                    st.success(f"Added {deg}")
                else:
                    st.error("Please fill in Degree and School.")

    # Display List
    st.markdown("### Academic History")
    if st.session_state.education:
        for edu in st.session_state.education:
            st.markdown(f"**{edu['deg']}**")
            st.write(f"{edu['sch']} — {edu['yr']}")
            st.divider()
    else:
        st.write("No education records added yet.")

# --------------------------------------------------
# 3. Experience 
# --------------------------------------------------
elif menu == "Experience":
    st.title("💼 Experience")
    
    # Input Form
    with st.expander("➕ Add New Experience"):
        with st.form("exp_form", clear_on_submit=True):
            role = st.text_input("Role")
            org = st.text_input("Organization")
            dur = st.text_input("Duration")
            if st.form_submit_button("Add Experience"):
                if role and org:
                    st.session_state.experience.append({"role": role, "org": org, "dur": dur})
                    st.success(f"Added {role}")
                else:
                    st.error("Please fill in Role and Organization.")

    # Display List
    st.markdown("### Professional Timeline")
    if st.session_state.experience:
        for exp in st.session_state.experience:
            st.markdown(f"**{exp['role']}**")
            st.write(f"*{exp['org']}* | {exp['dur']}")
            st.divider()
    else:
        st.write("No experience records added yet.")

# --------------------------------------------------
# 4. STEM Explorer (Topic-Specific Data)
# --------------------------------------------------
elif menu == "STEM Explorer":
    st.title("📊 Financial Inclusion Data Explorer")
    
    # Sample data related to your topic
    data = {
        "Method": ["Banking App", "Mobile Wallet", "USSD Payments", "Cash"],
        "Adoption Rate (%)": [45, 30, 15, 60],
        "Trust Score (1-10)": [8, 6, 7, 10]
    }
    df = pd.DataFrame(data)
    
    st.write("### Payment Method Preferences in SA Townships")
    st.bar_chart(df.set_index("Method")["Adoption Rate (%)"])
    st.table(df)

# --------------------------------------------------
# 5. Research Interests
# --------------------------------------------------
elif menu == "Research Interests":
    st.title("🔬 Research Interests")
    st.markdown("""
    * **Fintech Acceptance:** Factors influencing the transition from cash to digital.
    * **Last-Mile Delivery:** How mobile payments reach rural communities in SA.
    * **Policy Impact:** Evaluation of SARB's Vision 2025 on financial inclusion.
    """)

# --------------------------------------------------
# 6. Contact
# --------------------------------------------------
elif menu == "Contact":
    st.title("📬 Contact")
    st.write("📧 Email: tshivhaserichie@gmail.com")




