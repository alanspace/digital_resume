from pathlib import Path

import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Shek_Lun_leung,_Alan_Resume.pdf"
profile_pic_path = current_dir / "assets" / "Profile_Canva_BG.png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Shek Lun Leung Alan"
PAGE_ICON = ":wave:"
NAME = "Shek Leung Lun, Alan"
DESCRIPTION = """
Master of Science in Engineering Physics (Quantum Technology) at KTH Royal Institute of Technology

Facilitating quantum technology research and development
"""
EMAIL = "slleung@kth.se"
SOCIAL_MEDIA = {
# "YouTube": "https://youtube.com/c/codingisfun",
    "LinkedIn": "https://www.linkedin.com/in/shek-lun-leung-alan/",
    "GitHub": "https://github.com/alanspace",
# "Twitter": "https://twitter.com",
    "Portfolio": "https://alanspace.github.io/portfolio/"
}
PROJECTS = {
    "🏆 Sales Dashboard - Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320",
    "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
    "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
    "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic_path)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=350)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---

st.write('\n')
st.subheader("Recent Positions - CTO & Co-Founder at Metvibee")
st.write("""
- ✔️ Prototype development of a smartphone AR app for participatory urban planning
- ✔️ Sharing insights on digital place-making by leveraging data and AI
- ✔️ Promoting Sustainable Development Goals (SDGs) through technology
- ✔️ Collaborating with companies and organizations to develop innovative solutions
"""
)


st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ IBM Qiskit Certified Developer
- ✔️ IBM Qiskit Advocate
- ✔️ IBM Qiskit Localization Contributor - Platinum Level Translator
- ✔️ National Section of International Physicists' Tournament
- ✔️ QuantumGrad Content Creator
- ✔️ Strong hands on experience and knowledge in Python
- ✔️ Good understanding of Quantum AI and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)

# Education section header
st.subheader("🚀 Education & Expertise in Quantum Technology")

# Courses Taken in Quantum Technology
st.markdown("### 🌌 Courses Taken in Quantum Technology")

st.markdown("""
**🧑‍🔬 Advanced Quantum Mechanics**  
- Symmetry and Conservation Laws  
- Angular Momentum and Spin  
- Identical Particles  
- Aharonov-Bohm Effect  
- Main Approximation Methods  

**🔧 Quantum Technology**  
- **SNSPD** (Superconducting Nanowire Single-Photon Detector)  
- **SQUID** (Superconducting Quantum Interference Device)  
- Nanowire  
- Quantum Dot  
- Quantum Erasure  

**🧠 Quantum Information & Algorithms**  
- Quantum Algorithms (Shor, Grover, etc.)  
- Quantum Information Processing  
- Quantum Cryptography & Security  
- Quantum Error Correction (Surface Codes)  

**🔬 Quantum Photonics & Entanglement**  
- Entanglement and Quantum Teleportation  
- Single Photon Generation  
- Quantum Repeater & Networking  
- Quantum Key Distribution (QKD)  

**🌐 Fiber-Optical Communication**  
- Light Source (Lasers, LEDs)  
- Optical Fibers & Waveguides  
- Photodetectors (APDs, SNSPDs)  
- Digital Fiber Optic Links for Long-Distance Communication  

**🧪 Quantum Materials**  
- Advanced Characterization Techniques (STM, AFM, XPS)  
- Future Technical Applications (Topological Insulators, Quantum Dots, Superconductors)  

**🧩 Quantum Circuit Design & Quantum Transport**  
- Quantum Transport Theory (Mesoscopic Systems)  
- Lumped-Element Model for Circuit QED  
- Quantum-limited Measurement and Noise Analysis  

**❄️ Superconductivity & Quantum Fluids**  
- Superconductivity Theory & Applications  
- Quantum Fluids (Bose-Einstein Condensates, Superfluids)  
- Topological Quantum Computing
""")

# Summer Schools section header
st.markdown("### 🌟 Summer Schools & Hands-on Experience")

st.markdown("""
- **7th Superconductivity Summer School** 🧲  
  Topics: Fundamentals of Superconductivity, Applications in Quantum Computing, Materials, Modelling, and Measurements  

- **Minato Summer School** 🌏  
  Topics: Cutting-edge Microelectronics, Nanochemistry, Advanced Fabrication Techniques for Quantum Devices  

- **VCQ & TURIS Summer School** 🌠  
  Topics: Quantum Information, General Relativity, Quantum Algorithms, Standard Model, Quantum Gravity  
""")


# - 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL, VBA
# - 📊 Data Visulization: PowerBi, MS Excel, Plotly
# - 📚 Modeling: Logistic regression, linear regression, decition trees
# - 🗄️ Databases: Postgres, MongoDB, MySQL

# # --- SKILLS ---
# st.write('\n')
# st.subheader("Hard Skills")
# st.write(
#     """
# # - 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL, VBA
# # - 📊 Data Visulization: PowerBi, MS Excel, Plotly
# # - 📚 Modeling: Logistic regression, linear regression, decition trees
# # - 🗄️ Databases: Postgres, MongoDB, MySQL
# # """
# # )


# # --- WORK HISTORY ---
# st.write('\n')
# st.subheader("Work History")
# st.write("---")

# # --- JOB 1
# st.write("🚧", "**Senior Data Analyst | Ross Industries**")
# st.write("02/2020 - Present")
# st.write(
#     """
# - ► Used PowerBI and SQL to redeﬁne and track KPIs surrounding marketing initiatives, and supplied recommendations to boost landing page conversion rate by 38%
# - ► Led a team of 4 analysts to brainstorm potential marketing and sales improvements, and implemented A/B tests to generate 15% more client leads
# - ► Redesigned data model through iterations that improved predictions by 12%
# """
# )

# # --- JOB 2
# st.write('\n')
# st.write("🚧", "**Data Analyst | Liberty Mutual Insurance**")
# st.write("01/2018 - 02/2022")
# st.write(
#     """
# - ► Built data models and maps to generate meaningful insights from customer data, boosting successful sales eﬀorts by 12%
# - ► Modeled targets likely to renew, and presented analysis to leadership, which led to a YoY revenue increase of $300K
# - ► Compiled, studied, and inferred large amounts of data, modeling information to drive auto policy pricing
# """
# )

# # --- JOB 3
# st.write('\n')
# st.write("🚧", "**Data Analyst | Chegg**")
# st.write("04/2015 - 01/2018")
# st.write(
#     """
# - ► Devised KPIs using SQL across company website in collaboration with cross-functional teams to achieve a 120% jump in organic traﬃc
# - ► Analyzed, documented, and reported user survey results to improve customer communication processes by 18%
# - ► Collaborated with analyst team to oversee end-to-end process surrounding customers' return data
# """
# )


# # --- Projects & Accomplishments ---
# st.write('\n')
# st.subheader("Projects & Accomplishments")
# st.write("---")
# for project, link in PROJECTS.items():
#     st.write(f"[{project}]({link})")
