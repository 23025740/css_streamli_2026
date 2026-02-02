import streamlit as st
import pandas as pd

# --------------------------------------------------
# Page Config
# --------------------------------------------------
st.set_page_config(
    page_title="Research Portfolio | Mobile Payments & Financial Inclusion",
    page_icon="🇿🇦",
    layout="wide"
)

# --------------------------------------------------
# Initialization
# --------------------------------------------------
# Ensures data persists during the session
for key in ["education", "experience", "projects", "publications"]:
    if key not in st.session_state:
        st.session_state[key] = []

# --------------------------------------------------
# Sidebar Navigation
# --------------------------------------------------
st.sidebar.title("📌 Portfolio Navigation")
st.sidebar.markdown("---")
menu = st.sidebar.radio(
    "Go to:",
    [
        "Researcher Profile",
        "Education",
        "Experience",
        "Research Interests",
        "Research Projects",
        "Publications",
        "SA STEM Data Explorer",
        "Contact"
    ]
)

# --------------------------------------------------
# 1. Researcher Profile
# --------------------------------------------------
if menu == "Researcher Profile":
    st.title("👤 Researcher Profile")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        name = st.text_input("Name", "Dr. Kevin Lee")
        field = st.text_input("Field", "FinTech & Digital Economics")
        inst = st.text_input("Institution", "University of South Africa (UNISA)")
        st.image("https://via.placeholder.com/150", caption="Profile Picture Placeholder")

    with col2:
        st.subheader("Professional Bio")
        bio_text = (
            "Researcher specializing in the digital economy with a primary focus on "
            "South Africa. I investigate how mobile payment systems—ranging from "
            "banking apps to emerging Fintech—act as catalysts for financial inclusion "
            "among unbanked and underbanked populations."
        )
        bio = st.text_area("Edit Bio", bio_text, height=150)
        st.info(f"**Current Focus:** {bio}")

# --------------------------------------------------
# 2. Education
# --------------------------------------------------
elif menu == "Education":
    st.title("🎓 Education")
    
    with st.expander("Add Academic History"):
        c1, c2 = st.columns(2)
        degree = c1.text_input("Degree (e.g., PhD in Economics)")
        school = c2.text_input("University")
        year = st.text_input("Year of Graduation")
        
        if st.button("Add Education"):
            st.session_state.education.append({"deg": degree, "sch": school, "yr": year})
            st.success("Record added!")

    for edu in st.session_state.education:
        st.write(f"**{edu['deg']}** | {edu['sch']} ({edu['yr']})")

# --------------------------------------------------
# 3. Experience
# --------------------------------------------------
elif menu == "Experience":
    st.title("💼 Professional Experience")
    
    with st.expander("Add Work/Research Experience"):
        role = st.text_input("Role")
        org = st.text_input("Organization")
        desc = st.text_area("Key Responsibilities")
        
        if st.button("Add Experience"):
            st.session_state.experience.append({"role": role, "org": org, "desc": desc})
            st.success("Experience logged!")

    for exp in st.session_state.experience:
        st.markdown(f"**{exp['role']}** at *{exp['org']}*")
        st.caption(exp['desc'])

# --------------------------------------------------
# 4. Research Interests
# --------------------------------------------------
elif menu == "Research Interests":
    st.title("🔬 Research Interests & Vision")

    interests = {
        "📱 Mobile Payment Adoption": [
            "User acceptance of PayShap and digital wallets",
            "Trust factors in digital transactions",
            "Impact of high data costs on adoption"
        ],
        "🏦 Financial Inclusion": [
            "Mapping the 'Last Mile' in rural SA provinces",
            "MSME formalization through digital footprints",
            "Digital literacy in the informal economy"
        ],
        "⚖️ Regulatory Policy": [
            "SARB Vision 2025 impact",
            "Fintech licensing and consumer protection",
            "Cybersecurity for first-time digital users"
        ]
    }

    for area, items in interests.items():
        with st.expander(area):
            for item in items:
                st.write(f"• {item}")

# --------------------------------------------------
# 5. Research Projects
# --------------------------------------------------
elif menu == "Research Projects":
    st.title("🧠 Active Projects")

    # Seeded project for the user
    st.markdown("### 🏆 Flagship Project")
    st.info("""
    **Title:** Assessing Mobile Payment Impact on Financial Inclusion in SA  
    **Objective:** Evaluating how mobile-first banking reduces the gap in rural financial access.  
    **Status:** Field Data Collection phase.
    """)

    with st.expander("Add New Project"):
        p_title = st.text_input("Project Title")
        p_desc = st.text_area("Summary")
        if st.button("Save Project"):
            st.session_state.projects.append({"title": p_title, "desc": p_desc})

    for p in st.session_state.projects:
        st.markdown(f"#### {p['title']}")
        st.write(p['desc'])

# --------------------------------------------------
# 6. STEM Data Explorer
# --------------------------------------------------
elif menu == "SA STEM Data Explorer":
    st.title("📊 Financial Inclusion Data Explorer")
    st.markdown("Visualizing trends in the South African payment landscape.")

    # Mock data reflecting the SA context
    sa_fin_data = pd.DataFrame({
        "Province": ["Gauteng", "Western Cape", "KZN", "Limpopo", "Eastern Cape"],
        "Smartphone Penetration (%)": [94, 91, 85, 78, 72],
        "Mobile App Usage (%)": [82, 78, 65, 42, 38],
        "Cash Reliance (%)": [15, 18, 40, 65, 70]
    })

    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.write("### Provincial Metrics")
        st.dataframe(sa_fin_data)
        
    with col2:
        st.write("### Digital vs. Cash Reliance")
        st.bar_chart(sa_fin_data.set_index("Province")[["Mobile App Usage (%)", "Cash Reliance (%)"]])

    st.warning("Note: This data represents the 'Digital Divide' between urban hubs and rural provinces.")

# --------------------------------------------------
# 7. Contact
# --------------------------------------------------
elif menu == "Contact":
    st.title("📬 Connect with Me")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("📧 **Email:** kevin.lee@university.ac.za")
        st.write("🔗 **LinkedIn:** [linkedin.com/in/kevinlee-sa](#)")
        st.write("🐙 **GitHub:** [github.com/kevinlee-research](#)")
    
    with col2:
        st.write("### Send a Research Inquiry")
        with st.form("contact_form"):
            user_email = st.text_input("Your Email")
            msg = st.text_area("Message")
            if st.form_submit_button("Submit"):
                st.success(f"Thank you! Your message has been simulated as sent.")

# --------------------------------------------------
# Clean up Publications (Placeholder Logic)
# --------------------------------------------------
elif menu == "Publications":
    st.title("📚 Publications")
    st.write("No publications listed yet. Add one below:")
    
    with st.expander("Add Publication"):
        pub_title = st.text_input("Title")
        pub_yr = st.number_input("Year", 2020, 2026, 2026)
        if st.button("Save Publication"):
            st.session_state.publications.append({"title": pub_title, "yr": pub_yr})
    
    if st.session_state.publications:
        st.table(pd.DataFrame(st.session_state.publications))
