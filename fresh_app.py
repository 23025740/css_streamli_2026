# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 11:44:43 2026

@author: 23025740
"""

import streamlit as st
import pandas as pd

# --------------------------------------------------
# Page Config
# --------------------------------------------------
st.set_page_config(
    page_title="Research & Data Science Portfolio",
    layout="wide"
)

# --------------------------------------------------
# Sidebar Navigation
# --------------------------------------------------
st.sidebar.title("📌 Navigation")

menu = st.sidebar.radio(
    "Go to:",
    [
        "Researcher Profile",
        "Education",
        "Experience",
        "Research Interests",
        "Projects",
        "Publications",
        "STEM Data Explorer",
        "Contact"
    ],
    key="main_navigation"  
)

# --------------------------------------------------
# Initialize Session State
# --------------------------------------------------
for key in ["education", "experience", "projects", "publications"]:
    if key not in st.session_state:
        st.session_state[key] = []

# --------------------------------------------------
# Researcher Profile
# --------------------------------------------------
if menu == "Researcher Profile":
    st.title("👤 Researcher Profile")

    name = st.text_input("Name", "Dr. Kevin Lee")
    field = st.text_input("Field", "Data Science & Artificial Intelligence")
    institution = st.text_input("Institution", "Tech Innovation University")
    bio = st.text_area(
        "Short Bio",
        "Researcher and data professional with interests in data analysis, "
        "data engineering, and quantitative modeling."
    )

    col1, col2 = st.columns(2)
    with col1:
        st.write(f"**Name:** {name}")
        st.write(f"**Field:** {field}")
        st.write(f"**Institution:** {institution}")
    with col2:
        st.info(bio)

# --------------------------------------------------
# Education
# --------------------------------------------------
elif menu == "Education":
    st.title("🎓 Education")

    with st.expander("Add Education"):
        degree = st.text_input("Degree")
        school = st.text_input("School / University")
        year = st.text_input("Year")
        focus = st.text_area("Specialization / Focus")

        if st.button("Add Education"):
            st.session_state.education.append({
                "Degree": degree,
                "School": school,
                "Year": year,
                "Focus": focus
            })
            st.success("Education added")

    for edu in st.session_state.education:
        st.markdown(f"""
        **{edu['Degree']}**  
        *{edu['School']}* ({edu['Year']})  
        {edu['Focus']}
        """)

# --------------------------------------------------
# Experience
# --------------------------------------------------
elif menu == "Experience":
    st.title("💼 Experience")

    with st.expander("Add Experience"):
        role = st.text_input("Role / Position")
        org = st.text_input("Organization")
        duration = st.text_input("Duration")
        description = st.text_area("Description")

        if st.button("Add Experience"):
            st.session_state.experience.append({
                "Role": role,
                "Organization": org,
                "Duration": duration,
                "Description": description
            })
            st.success("Experience added")

    for exp in st.session_state.experience:
        st.markdown(f"""
        **{exp['Role']}** — {exp['Organization']}  
        *{exp['Duration']}*  
        {exp['Description']}
        """)

# --------------------------------------------------
# Research Interests
# --------------------------------------------------
elif menu == "Research Interests":
    st.title("🔬 Research Interests & Career Ventures")

    areas = {
        "📊 Data Analysis": [
            "Exploratory Data Analysis (EDA)",
            "Statistical insights",
            "Visualization and reporting"
        ],
        "🤖 Data Science": [
            "Machine learning",
            "Predictive modeling",
            "Feature engineering"
        ],
        "🏗️ Data Engineering": [
            "ETL pipelines",
            "Databases and data warehousing",
            "Big data systems"
        ],
        "📈 Quantitative Analysis": [
            "Statistical modeling",
            "Time-series analysis",
            "Risk and performance modeling"
        ]
    }

    for area, items in areas.items():
        with st.expander(area):
            for item in items:
                st.write(f"• {item}")

    vision = st.text_area(
        "Career Vision",
        "I aim to work at the intersection of data analysis, data engineering, "
        "and quantitative modeling to build scalable, data-driven systems "
        "for research, finance, and technology."
    )
    st.info(vision)

# --------------------------------------------------
# Projects
# --------------------------------------------------
elif menu == "Projects":
    st.title("🧠 Projects")

    with st.expander("Add Project"):
        title = st.text_input("Project Title")
        tech = st.text_input("Technologies Used")
        desc = st.text_area("Project Description")
        link = st.text_input("Project Link")

        if st.button("Add Project"):
            st.session_state.projects.append({
                "Title": title,
                "Tech": tech,
                "Description": desc,
                "Link": link
            })
            st.success("Project added")

    for proj in st.session_state.projects:
        st.markdown(f"""
        ### {proj['Title']}
        **Tech:** {proj['Tech']}  
        {proj['Description']}  
        🔗 {proj['Link']}
        """)

# --------------------------------------------------
# Publications
# --------------------------------------------------
elif menu == "Publications":
    st.title("📚 Publications")

    with st.expander("Add Publication"):
        title = st.text_input("Title")
        authors = st.text_input("Authors")
        venue = st.text_input("Journal / Conference")
        year = st.number_input("Year", 2000, 2100, 2024)

        if st.button("Add Publication"):
            st.session_state.publications.append({
                "Title": title,
                "Authors": authors,
                "Venue": venue,
                "Year": year
            })
            st.success("Publication added")

    if st.session_state.publications:
        df = pd.DataFrame(st.session_state.publications)
        st.dataframe(df)

# --------------------------------------------------
# STEM Data Explorer
# --------------------------------------------------
elif menu == "STEM Data Explorer":
    st.title("📊 STEM Data Explorer")

    ai_data = pd.DataFrame({
        "Algorithm": ["Neural Net", "Decision Tree", "SVM", "Random Forest", "Transformer"],
        "Accuracy (%)": [92, 85, 88, 90, 95]
    })

    st.metric("Best Accuracy", f"{ai_data['Accuracy (%)'].max()}%")
    st.bar_chart(ai_data.set_index("Algorithm"))

# --------------------------------------------------
# Contact
# --------------------------------------------------
elif menu == "Contact":
    st.title("📬 Contact")
    st.write("📧 Email: kevin.lee@example.com")
    st.write("🔗 LinkedIn / GitHub available upon request")
import streamlit as st
import pandas as pd

# --------------------------------------------------
# Page Config
# --------------------------------------------------
st.set_page_config(
    page_title="Research & Data Science Portfolio",
    layout="wide"
)

# --------------------------------------------------
# Sidebar Navigation
# --------------------------------------------------
st.sidebar.title("📌 Navigation")

menu = st.sidebar.radio(
    "Go to:",
    [
        "Researcher Profile",
        "Education",
        "Experience",
        "Research Interests",
        "Projects",
        "Publications",
        "STEM Data Explorer",
        "Contact"
    ]
)

# --------------------------------------------------
# Initialize Session State
# --------------------------------------------------
for key in ["education", "experience", "projects", "publications"]:
    if key not in st.session_state:
        st.session_state[key] = []

# --------------------------------------------------
# Researcher Profile
# --------------------------------------------------
if menu == "Researcher Profile":
    st.title("👤 Researcher Profile")

    name = st.text_input("Name", "Dr. Kevin Lee")
    field = st.text_input("Field", "Data Science & Artificial Intelligence")
    institution = st.text_input("Institution", "Tech Innovation University")
    bio = st.text_area(
        "Short Bio",
        "Researcher and data professional with interests in data analysis, "
        "data engineering, and quantitative modeling."
    )

    col1, col2 = st.columns(2)
    with col1:
        st.write(f"**Name:** {name}")
        st.write(f"**Field:** {field}")
        st.write(f"**Institution:** {institution}")
    with col2:
        st.info(bio)

# --------------------------------------------------
# Education
# --------------------------------------------------
elif menu == "Education":
    st.title("🎓 Education")

    with st.expander("Add Education"):
        degree = st.text_input("Degree")
        school = st.text_input("School / University")
        year = st.text_input("Year")
        focus = st.text_area("Specialization / Focus")

        if st.button("Add Education"):
            st.session_state.education.append({
                "Degree": degree,
                "School": school,
                "Year": year,
                "Focus": focus
            })
            st.success("Education added")

    for edu in st.session_state.education:
        st.markdown(f"""
        **{edu['Degree']}**  
        *{edu['School']}* ({edu['Year']})  
        {edu['Focus']}
        """)

# --------------------------------------------------
# Experience
# --------------------------------------------------
elif menu == "Experience":
    st.title("💼 Experience")

    with st.expander("Add Experience"):
        role = st.text_input("Role / Position")
        org = st.text_input("Organization")
        duration = st.text_input("Duration")
        description = st.text_area("Description")

        if st.button("Add Experience"):
            st.session_state.experience.append({
                "Role": role,
                "Organization": org,
                "Duration": duration,
                "Description": description
            })
            st.success("Experience added")

    for exp in st.session_state.experience:
        st.markdown(f"""
        **{exp['Role']}** — {exp['Organization']}  
        *{exp['Duration']}*  
        {exp['Description']}
        """)

# --------------------------------------------------
# Research Interests
# --------------------------------------------------
elif menu == "Research Interests":
    st.title("🔬 Research Interests & Career Ventures")

    areas = {
        "📊 Data Analysis": [
            "Exploratory Data Analysis (EDA)",
            "Statistical insights",
            "Visualization and reporting"
        ],
        "🤖 Data Science": [
            "Machine learning",
            "Predictive modeling",
            "Feature engineering"
        ],
        "🏗️ Data Engineering": [
            "ETL pipelines",
            "Databases and data warehousing",
            "Big data systems"
        ],
        "📈 Quantitative Analysis": [
            "Statistical modeling",
            "Time-series analysis",
            "Risk and performance modeling"
        ]
    }

    for area, items in areas.items():
        with st.expander(area):
            for item in items:
                st.write(f"• {item}")

    vision = st.text_area(
        "Career Vision",
        "I aim to work at the intersection of data analysis, data engineering, "
        "and quantitative modeling to build scalable, data-driven systems "
        "for research, finance, and technology."
    )
    st.info(vision)

# --------------------------------------------------
# Projects
# --------------------------------------------------
elif menu == "Projects":
    st.title("🧠 Projects")

    with st.expander("Add Project"):
        title = st.text_input("Project Title")
        tech = st.text_input("Technologies Used")
        desc = st.text_area("Project Description")
        link = st.text_input("Project Link")

        if st.button("Add Project"):
            st.session_state.projects.append({
                "Title": title,
                "Tech": tech,
                "Description": desc,
                "Link": link
            })
            st.success("Project added")

    for proj in st.session_state.projects:
        st.markdown(f"""
        ### {proj['Title']}
        **Tech:** {proj['Tech']}  
        {proj['Description']}  
        🔗 {proj['Link']}
        """)

# --------------------------------------------------
# Publications
# --------------------------------------------------
elif menu == "Publications":
    st.title("📚 Publications")

    with st.expander("Add Publication"):
        title = st.text_input("Title")
        authors = st.text_input("Authors")
        venue = st.text_input("Journal / Conference")
        year = st.number_input("Year", 2000, 2100, 2024)

        if st.button("Add Publication"):
            st.session_state.publications.append({
                "Title": title,
                "Authors": authors,
                "Venue": venue,
                "Year": year
            })
            st.success("Publication added")

    if st.session_state.publications:
        df = pd.DataFrame(st.session_state.publications)
        st.dataframe(df)

# --------------------------------------------------
# STEM Data Explorer
# --------------------------------------------------
elif menu == "STEM Data Explorer":
    st.title("📊 STEM Data Explorer")

    ai_data = pd.DataFrame({
        "Algorithm": ["Neural Net", "Decision Tree", "SVM", "Random Forest", "Transformer"],
        "Accuracy (%)": [92, 85, 88, 90, 95]
    })

    st.metric("Best Accuracy", f"{ai_data['Accuracy (%)'].max()}%")
    st.bar_chart(ai_data.set_index("Algorithm"))

# --------------------------------------------------
# Contact
# --------------------------------------------------
elif menu == "Contact":
    st.title("📬 Contact")
    st.write("📧 Email: kevin.lee@example.com")

    st.write("🔗 LinkedIn / GitHub available upon request")
