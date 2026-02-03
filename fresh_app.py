import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Tshivhase Ritshidze | Portfolio", layout="wide")

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("📌 Navigation")
menu = st.sidebar.radio(
    "Go to:",
    ["Profile", "Education & Experience", "Project Portfolio", "STEM Data Explorer: Research Hub", "Contact"],
)

# --- SECTION: PROFILE ---
if menu == "Profile":
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://via.placeholder.com/300", caption="Tshivhase Ritshidze")
    with col2:
        st.title("Tshivhase Ritshidze")
        st.subheader("BSc Computer Science & Mathematics | University of Venda")
        st.write("""
        I am a data-driven researcher and developer focusing on the intersection of **FinTech and Social Impact**. 
        My current research investigates how mobile payment rails—specifically real-time systems like PayShap—are 
        transforming financial inclusion for the unbanked and informal sectors in South Africa.
        """)
        st.markdown("### Technical Stack")
        st.code("Languages: Python (Data Science), Java, C++, SQL\nTools: Streamlit, Plotly, Git, Linux", language='python')

# --- SECTION: EDUCATION & EXPERIENCE ---
elif menu == "Education & Experience":
    st.header("Academic & Professional Journey")
    
    with st.expander("💼 Internship: InterBoot", expanded=True):
        st.write("#### **Software Engineering Intern**")
        st.write("*InterBoot | 2025 - Present*")
        st.write("""
        - Developing scalable web applications and integrating secure payment APIs.
        - Applying mathematical modeling to optimize system performance and data flow.
        - Collaborating in an Agile environment to deliver user-centric software solutions.
        """)

    with st.expander("🎓 Education: University of Venda", expanded=True):
        st.write("#### **BSc in Computer Science and Mathematics**")
        st.write("*2023 - 2026 (Expected)*")
        st.write("""
        - **Core CS:** Data Structures, Algorithms, Database Systems, Software Engineering.
        - **Core Maths:** Calculus, Linear Algebra, Discrete Mathematics, Numerical Analysis.
        """)

# --- SECTION: PROJECT PORTFOLIO ---
elif menu == "Project Portfolio":
    st.header("Selected Projects")
    p1, p2 = st.columns(2)
    with p1:
        st.info("### Mobile Payment Impact Model")
        st.write("A Python-based simulation analyzing how transaction fee reductions correlate with informal trader adoption.")
    with p2:
        st.success("### Algorithm Visualizer")
        st.write("A tool built for peers at UniVen to visualize complex sorting algorithms in real-time.")

# --- SECTION: STEM DATA EXPLORER (RESEARCH HUB) ---
elif menu == "STEM Data Explorer: Research Hub":
    st.title("📊 Research Dashboard")
    st.header("The Adoption & Impact of Mobile Payment Systems on Financial Inclusion")
    
    st.markdown("""
    This dashboard serves as a visualization tool for my undergraduate research. 
    It tracks the shift from cash-heavy informal economies to digital 'alias-based' payment systems in South Africa.
    """)

    # --- RESEARCH DATASET ---
    # Representative data based on SARB Vision 2025 and 2024/2025 bank reports
    data = {
        "Year": [2021, 2022, 2023, 2024, 2025],
        "Unbanked Population (%)": [19, 18.2, 16.5, 15.0, 13.1],
        "PayShap Volume (Millions)": [0, 0, 0.4, 74.2, 461.0], # Surge in 2024/25
        "Digital Wallet Usage (%)": [38, 42, 46, 70, 78]
    }
    df = pd.DataFrame(data)

    # --- METRICS ---
    m1, m2, m3 = st.columns(3)
    m1.metric("Current Unbanked Rate", "13.1%", "-1.9% YoY")
    m2.metric("PayShap Transactions (Total)", "461M", "+522% Growth")
    m3.metric("Avg. Transaction Size", "R498", "Entry-level Targeted")

    # --- INTERACTIVE VISUALIZATION ---
    st.divider()
    st.subheader("Visualizing the Digital Leap")
    
    chart_choice = st.selectbox("Select View:", ["Financial Inclusion vs. Wallet Growth", "PayShap Adoption Curve"])
    
    if chart_choice == "Financial Inclusion vs. Wallet Growth":
        fig = px.line(df, x="Year", y=["Unbanked Population (%)", "Digital Wallet Usage (%)"],
                      title="Inverse Correlation: Digital Access vs. Financial Exclusion",
                      markers=True, color_discrete_sequence=["#EF553B", "#636EFA"])
        st.plotly_chart(fig, use_container_width=True)
    else:
        fig = px.bar(df, x="Year", y="PayShap Volume (Millions)", 
                     title="PayShap Transaction Growth (Post-Launch 2023)",
                     color="PayShap Volume (Millions)", color_continuous_scale="Viridis")
        st.plotly_chart(fig, use_container_width=True)

    # --- RESEARCH ANALYSIS TABLE ---
    st.subheader("Comparative Impact of Payment Rails")
    impact_data = pd.DataFrame({
        "System": ["PayShap", "FNB eWallet", "Capitec Pay", "MTN MoMo", "1Voucher"],
        "Accessibility": ["High (Alias-based)", "Moderate", "High (App-based)", "High (USSD/Agent)", "Very High (Cash-to-Digital)"],
        "Inclusion Target": ["SMEs/Individuals", "Remittance", "Retail Consumers", "Unbanked Rural", "Informal Traders"],
        "Cost to User": ["Low (R0 < R100)", "Fixed Fee", "Low/Variable", "Tiered", "Commission-based"]
    })
    st.table(impact_data)
    
    st.info("**Research Insight:** My analysis shows that systems using 'ShapIDs' (cellphone numbers) significantly lower the psychological and technical barrier for unbanked individuals compared to traditional IBAN/Account formats.")

# --- SECTION: CONTACT ---
elif menu == "Contact":
    st.header("📬 Contact & Collaboration")
    st.write("I am currently open to internship opportunities and research collaborations in the FinTech space.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("📧 **Email:** [tshivhaseritshidze03@gmail.com](mailto:tshivhaseritshidze03@gmail.com)")
        st.write("📍 **Location:** Thohoyandou, Limpopo")
    with col2:
        st.write("🔗 **LinkedIn:** [linkedin.com/in/yourprofile]")
        st.write("💻 **GitHub:** [github.com/yourusername]")
