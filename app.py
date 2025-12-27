from pathlib import Path

import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Shek_Lun_leung,_Alan_Resume.pdf"
profile_pic_path = current_dir / "assets" / "Profile_Canva_BG.png"
master_project_file = current_dir / "assets" / "Machine_learning_for_optimal_parameter_prediction_in_quantum_key_distribution_updated.pdf"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Shek Lun Leung Alan"
PAGE_ICON = "👋"
NAME = "Shek Leung Lun, Alan"
DESCRIPTION = """
Master of Science in Engineering Physics (Quantum Technology) at Royal Institute of Technology (KTH)

Facilitating quantum technology research and development
"""
EMAIL = "slleung@kth.se"
SOCIAL_MEDIA = {
# "YouTube": "https://youtube.com/c/codingisfun",
    "LinkedIn": "https://www.linkedin.com/in/shek-lun-leung-alan/",
    "GitHub": "https://github.com/alanspace",
# "Twitter": "https://twitter.com",
    "Portfolio": "https://alanspace.github.io/Alan_Portfolio_advanced/"
}

PROJECTS = {
    "🏆 Master Thesis - Communication and Error Correction via Polarisation of Single Photons and Time Ordering": "https://kth.diva-portal.org/smash/record.jsf?pid=diva2%3A1796647&dswid=-1650",
    "🏆 Master Project - Machine Learning for Quantum Key Distribution Network Optimization": "https://github.com/alanspace/digital_resume/blob/master/assets/Machine_learning_for_optimal_parameter_prediction_in_quantum_key_distribution_updated.pdf",
    " Autonomy in AI - Co-authored research on the simulation-reality gap in humanoid robots; proposed accountability frameworks for autonomous agents: ": "https://substack.com/inbox/post/182663178?r=73jdjw&utm_campaign=post&utm_medium=web&showWelcomeOnShare=true&triedRedirect=true"
    # "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
    # "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
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
    st.image(profile_pic, width=400)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📧", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---

st.write('\n')
st.subheader("DreamToDone | Technical Director) (2025-present)")
st.write("""
-        Architecting an AI reasoning ecosystem for creative workflows; selected as a finalist for the KTH Innovation/SSE pitch competition.
     """
)

st.write('\n')
st.subheader("Grant Seeker AI | Technical Lead (Google x Kaggle Hackathon) (2025-present)")
st.write("""
-        Designed a multi-agent ecosystem using Google ADK & Gemini Flash
-        Implemented sequential orchestration (Reasoning -> Search -> Extraction) and parallel web scraping for automated proposal generation
     """
)

st.subheader("Metvibee AB | CTO & Co-Founder (2023-2024)")
st.write("""
- ✨ Prototype development of a smartphone AR app for participatory urban planning
- ✨ Sharing insights on digital place-making by leveraging data and AI
- ✨ Promoting Sustainable Development Goals (SDGs) through technology
- ✨ Collaborating with companies and organizations to develop innovative solutions
"""
)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")

st.write('\n')
st.subheader("Experience & Qualifications")
st.write(
    """
- 🏅 IBM Qiskit Certified Developer
- 🏅 IBM Qiskit Advocate
- 🏅 IBM Qiskit Localization Contributor - Platinum Level Translator
- 🏅 National Section of International Physicists' Tournament
- 💻 QuantumGrad Content Creator
- 💻 Strong hands on experience and knowledge in Python
- 🧠 Good understanding of Quantum AI and their respective applications
- 🤝 Excellent team-player and displaying strong sense of initiative on tasks
"""
)

# Education section header
st.subheader("📚 Education & Expertise in Quantum Technology")

# Courses Taken in Quantum Technology
st.markdown("### 🎓 Courses Taken in Quantum Technology")

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
- **VCQ & TURIS Summer School - September, 2024** 🎓  
  Topics: Quantum Information, General Relativity, Quantum Algorithms, Standard Model, Quantum Gravity 
- **Minato Summer School - June, 2024** 🎓  
  Topics: Cutting-edge Microelectronics, Nanochemistry, Advanced Fabrication Techniques for Quantum Devices
- **7th Superconductivity Summer School - June, 2022** 🎓  
  Topics: Fundamentals of Superconductivity, Applications in Quantum Computing, Materials, Modelling, and Measurements 
""")

# Education section header
st.subheader("🤖 Education & Expertise in Artificial Intelligence")
st.markdown("### 📚 Courses Taken in AI & Society")
st.markdown("""
**📚 Artificial Intelligence in Society**
- Synthesized course theories into an original 15-page framework on the      simulation-reality gap in humanoid LLMs.
- The first Computational Theory of Mind and Brain
- The Mind as Symbol System
- The Turing Test
- John Searle and The Chinese Room
- The Churchland's Connectionist Response to Searle
- The Dreyfus' Phenomenological Critique
- Weizenbaum's Moral Critique
- Four Perspective on Morality
- The Turing Cathedral, Apocalyptic AI and the Pause Letter
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
