# --- PATH SETTINGS ---
# current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
# css_file = current_dir / "styles" / "main.css"
# resume_file = current_dir / "assets" / "Shek_Lun_leung,_Alan_Resume.pdf"
# profile_pic_path = current_dir / "assets" / "Profile_Canva_BG.png"
# master_project_file = current_dir / "assets" / "Machine_learning_for_optimal_parameter_prediction_in_quantum_key_distribution_updated.pdf"

from pathlib import Path
import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
# resume_file = current_dir / "assets" / "shek-lun-leung-resume-anthropic-fellowship.pdf"
profile_pic_path = current_dir / "assets" / "Profile_Canva_BG.png"

# --- RESUME FILE PATHS ---
# Ensure these filenames match what you have in your /assets folder
resume_ai_path = current_dir / "assets" / "shek-lun-leung-resume-anthropic-fellowship.pdf"
resume_quantum_path = current_dir / "assets" / "cv-quantum-engineer-shek-lun-leung.pdf"
resume_cto_path = current_dir / "assets" / "cv-entrepreneur-shek-lun-leung.pdf"

# --- PAGE CONFIG ---
st.set_page_config(page_title="Digital CV | Alan Leung", page_icon="⚛️", layout="wide")

# --- LOAD ASSETS ---
def load_pdf(path):
    with open(path, "rb") as f:
        return f.read()

# Load PDFs (Wrapped in try-except in case files are missing during dev)
try:
    ai_pdf = load_pdf(resume_ai_path)
    q_pdf = load_pdf(resume_quantum_path)
    cto_pdf = load_pdf(resume_cto_path)
except:
    ai_pdf = q_pdf = cto_pdf = b"" # Fallback

profile_pic = Image.open(profile_pic_path)
# --- 1. HEADER SECTION ---
col1, col2 = st.columns([1, 2], gap="medium")
with col1:
    st.image(profile_pic, width=450)

with col2:
    st.title("Shek Leung Lun, Alan")
    st.subheader("Engineering Physics @ KTH | AI Researcher | CTO")
    st.write("📍 Stockholm, Sweden")
    st.write("📧 sheklunleung.qai@proton.me")
    
    # --- 2. THE RESUME DOWNLOAD SECTION (3 COLUMNS) ---
    st.write("### 📄 Download my Resume")
    st.info("Choose the version most relevant to your interests:")
    dl_col1, dl_col2, dl_col3 = st.columns(3)
    with dl_col1:
        st.download_button("🤖 AI Version", data=ai_pdf, file_name="Alan_Leung_AI.pdf", use_container_width=True)
    with dl_col2:
        st.download_button("⚛️ Quantum Tech Version", data=q_pdf, file_name="Alan_Leung_Quantum.pdf", use_container_width=True)
    with dl_col3:
        st.download_button("🚀 Founder/CTO Version", data=cto_pdf, file_name="Alan_Leung_CTO.pdf", use_container_width=True)

# --- SOCIAL LINKS ---
st.write('\n')
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/shek-lun-leung-alan/",
    "GitHub": "https://github.com/alanspace",
    "Portfolio": "https://alanspace.github.io/Alan_Portfolio_advanced/",
    "Substack": "https://simulationgap.substack.com"
}
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

st.write("---")
# # --- GENERAL SETTINGS ---
# PAGE_TITLE = "Digital CV | Shek Lun Leung Alan"
# PAGE_ICON = "⚛️"
# NAME = "Shek Leung Lun, Alan"
# DESCRIPTION = """
# Master of Science Student in Engineering Physics (Quantum Technology) at KTH.
# Specializing in the intersection of High-Performance ML (JAX/PyTorch), 
# Quantum Information, and AI Safety Research.
# """
# EMAIL = "sheklunleung.qai@proton.me"
# SOCIAL_MEDIA = {
#     "LinkedIn": "https://www.linkedin.com/in/shek-lun-leung-alan/",
#     "GitHub": "https://github.com/alanspace",
#     "Portfolio": "https://alanspace.github.io/Alan_Portfolio_advanced/",
#     "Substack": "https://substack.com/@sheklunleung"  # Updated to your research brand
# }

# --- 3. RECENT TECHNICAL LEADERSHIP ---
st.header("🚀 Technical Leadership")
lead_col1, lead_col2, lead_col3 = st.columns(3)

with lead_col1:
    st.subheader("DreamToDone | Technical Director")
    st.write("*Oct 2025 – Present*")
    st.write("- ✨ Architecting an AI reasoning ecosystem for creative workflows.")
    st.write("- ✨ Finalist for the KTH Innovation/SSE pitch competition.")

with lead_col2:
    st.subheader("Grant Seeker AI | Technical Lead in Kaggle Hackathon ")
    st.write("*Oct 2025 – Present*")
    st.write("- ✨ Designed a multi-agent ecosystem using Google ADK & Gemini Flash.")
    st.write("- ✨ Implemented sequential orchestration for automated proposal generation.")


with lead_col3:
    st.subheader("Metvibee AB | CTO & Co-Founder")
    st.write("*2023 – 2024*")
    st.write("- ✨ Led technology strategy and AR prototype development for urban planning.")
    st.write("- ✨ Managed full-stack R&D and stakeholder technical demonstrations.")


# st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# # --- LOAD CSS, PDF & PROFIL PIC ---
# with open(css_file) as f:
#     st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
# with open(resume_file, "rb") as pdf_file:
#     PDFbyte = pdf_file.read()
# profile_pic = Image.open(profile_pic_path)


# # --- HERO SECTION ---
# col1, col2 = st.columns(2, gap="small")
# with col1:
#     st.image(profile_pic, width=400)

# with col2:
#     st.title(NAME)
#     st.write(DESCRIPTION)
#     st.download_button(
#         label="📄 Download Resume",
#         data=PDFbyte,
#         file_name=resume_file.name,
#         mime="application/octet-stream",
#     )
#     st.write("📧", EMAIL)


# # --- SOCIAL LINKS ---
# st.write('\n')
# cols = st.columns(len(SOCIAL_MEDIA))
# for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
#     cols[index].write(f"[{platform}]({link})")

# st.write("---")
# # --- EXPERIENCE & QUALIFICATIONS ---
# st.subheader("EXPERIENCE & QUALIFICATIONS ")
# st.markdown("#### DreamToDone | Technical Director (2025–Present)")
# st.write("""
# - ✨ Architecting an AI reasoning ecosystem for creative workflows using Generative AI.
# - ✨ Finalist for the KTH Innovation/SSE pitch competition.
# """)

# st.markdown("#### Grant Seeker AI | Technical Lead in Google x Kaggle Hackathon (2025)")
# st.write("""
# - ✨ Designed a multi-agent ecosystem using Google ADK & Gemini Flash.
# - ✨ Implemented sequential orchestration for automated proposal generation.
# """)

# st.markdown("#### Metvibee AB | CTO & Co-Founder (2023–2024)")
# st.write("""
# - ✨ Led development of a smartphone AR app for participatory urban planning.
# - ✨ Translated complex data models into actionable stakeholder demonstrations.
# """)

st.write("---")

# --- 4. TOP RESEARCH PROJECTS ---
st.header("🔬 Featured Research & Technical Projects")
st.write("Bridging the gap between theoretical physics and empirical AI implementation.")

proj_col1, proj_col2, proj_col3 = st.columns(3)

with proj_col1:
    st.markdown("#### 🛡️ [Autonomy in AI: Exploring Subjectivity](https://tinyurl.com/576zs4vc)")
    st.write("""
    - Investigated the **simulation-reality gap** in LLM-powered humanoid robots.
    - Proposed accountability frameworks for autonomous agents.
    - Originally produced for KTH AI in Society course (2025).
    """)

with proj_col2:
    st.markdown("#### 📈 [ML for QKD Network Optimization](https://github.com/alanspace/QKD_KeyRate_Parameter_Optimization)")
    st.write("""
    - Designed a hybrid **JAX/PyTorch** pipeline for real-time parameter prediction.
    - Achieved a **~270x performance speedup** across 6,000 scenarios.
    - Master's Project at KTH (2024–2025).
    """)

with proj_col3:
    st.markdown("#### 🔬 [Master Thesis: Secure Communication](https://kth.diva-portal.org/smash/record.jsf?pid=diva2%3A1796647&dswid=-1650)")
    st.write("""
    - Analyzed **Beyond Pulse Position Modulation (BPPM)** for energy-efficient security.
    - Proved superior information density via large-scale Python simulations.
    - Published at Ericsson AB / KTH (2023).
    """)


st.write("---")

# --- 5. ACADEMIC FOUNDATION: DEEP TECH & QUANTUM ---
st.header("🎓 Specialized Academic Foundation")
st.write("A comprehensive background in Quantum Engineering, Mathematical Physics, and AI Safety.")

# --- TABS FOR PRIMARY DOMAINS ---
tab_quantum, tab_ai, tab_math, tab_sustain = st.tabs([
    "⚛️ Quantum Technology", 
    "🤖 AI Safety", 
    "📐 Math & Methodology", 
    "🌱 Sustainability Science"
])

with tab_quantum:
    st.subheader("High-Level Quantum Expertise Matrix")
    
    # ROW 1: Theory and Algorithms
    q_col1, q_col2, q_col3 = st.columns(3)
    with q_col1:
        st.markdown("""
        **🧠 Quantum Information (SH2381)**
        - Quantum Algorithms (Shor, Grover, etc.)
        - Quantum Information Processing
        - Quantum Cryptography & Security
        - Quantum Error Correction (Surface Codes)
        """)
    with q_col2:
        st.markdown("""
        **🔬 Quantum Photonics (SK2900)**
        - Entanglement and Quantum Teleportation
        - Single Photon Generation
        - Quantum Repeater & Networking
        - Quantum Key Distribution (QKD)
        """)
    with q_col3:
        st.markdown("""
        **🧑‍🔬 Advanced Quantum Mechanics (SI2380)**
        - Symmetry and Conservation Laws
        - Angular Momentum and Spin
        - Identical Particles
        - Aharonov-Bohm Effect
        - Main Approximation Methods
        """)

    # ROW 2: Hardware and Systems
    q_col4, q_col5, q_col6 = st.columns(3)
    with q_col4:
        st.markdown("""
        **🔧 Quantum Technology (SK2903)**
        - SNSPD (Superconducting Nanowire)
        - SQUID (Interference Devices)
        - Nanowire & Quantum Dots
        - Quantum Erasure
        """)
    with q_col5:
        st.markdown("""
        **❄️ Superconductivity & other Quantum Fluids (SK2905)**
        - Superconductivity Theory & Apps
        - BEC (Bose-Einstein Condensates)
        - Superfluids
        - Topological Quantum Computing
        """)
    with q_col6:
        st.markdown("""
        **🧩 Quantum Circuits (SK2906)**
        - Transport Theory (Mesoscopic Systems)
        - Lumped-Element Model for Circuit QED
        - Quantum-limited Measurement
        - Noise Analysis
        """)

    # ROW 3: Communication and Materials
    q_col7, q_col8, q_col9 = st.columns(3)
    with q_col7:
        st.markdown("""
        **🌐 Fiber-Optical Communication (SK2811)**
        - Light Sources (Lasers, LEDs)
        - Optical Fibers & Waveguides
        - Photodetectors (APDs, SNSPDs)
        - Digital Fiber Optic Links for Long-Distance Communication  
        """)
    with q_col8:
        st.markdown("""
        **🧪 Quantum Materials (SK2904)**
        - Advanced Characterization Techniques (STM, AFM, XPS)
        - Topological Insulators
        - Superconductors
        - Quantum Dots
        """)
    with q_col9:
        st.markdown("""
        **🔎 Methodology of Science (AK2030)**
        - Hypothesis Testing & Statistical Reasoning
        - Models, Definitions & Experiments
        - Research Ethics & Risk Assessment
        """)

    # ROW 4: Communication and Materials
    q_col10, q_col11, q_col12 = st.columns(3)
    with q_col10:
        st.markdown("""
        **🌐 research Methodology (SH2007)**
        - Light Sources (Lasers, LEDs)
        - Optical Fibers & Waveguides
        - Photodetectors (APDs, SNSPDs)
        - Digital Fiber Optic Links for Long-Distance Communication  
        """)
    with q_col11:
        st.markdown("""
        **🧪 Optics and Laser Physics (FK7046)**
        - Advanced Characterization Techniques (STM, AFM, XPS)
        - Topological Insulators
        - Superconductors
        - Quantum Dots
        """)
    with q_col12:
        st.markdown("""
        **🔎 Atomic and Molecular Physics (FK5023)**
        - Hypothesis Testing & Statistical Reasoning
        - Models, Definitions & Experiments
        - Research Ethics & Risk Assessment
        """)

    st.markdown("### 🌟 Advanced Technical Training & Summer Schools")
    ss_col1, ss_col2, ss_col3 = st.columns(3)
    with ss_col1:
        st.markdown("""
        **VCQ & TURIS (2024)**  
        *Vienna, Austria*  
         Topics: Quantum Information, General Relativity, Quantum Algorithms, Standard Model, Quantum Gravity
        """)
    with ss_col2:
        st.markdown("""
        **Minato Summer School (2024)**  
        *Toulouse, France*  
        Topics: Cutting-edge Microelectronics, Nanochemistry, Advanced Fabrication Techniques for Quantum Devices.
        """)
    with ss_col3:
        st.markdown("""
        **7th Superconductivity (2022)**  
        *Oxford, UK*  
        Topics: Fundamentals of Superconductivity, Applications in Quantum Computing, Materials, Modelling, and Measurements 
""")

with tab_ai:
    ai_col1, ai_col2 = st.columns(2)
    with ai_col1:
        st.markdown("""
        **🤖 Artificial Intelligence in Society**
        - The first Computational Theory of Mind and Brain
        - The Mind as Symbol System
        - The Turing Test
        - John Searle and The Chinese Room
        - The Churchlands' Connectionist Response to Searle
        - The Dreyfus' Phenomenological Critique
        - Weizenbaum's Moral Critique
        - Four Perspective on Morality
        - The Turing Cathedral, Apocalyptic AI and the Pause Letter
        - **Original Research:** 15-page report on the Simulation-Reality gap in Humanoid robots.
        """)
    with ai_col2:    
        st.markdown("""
        **🔎 Methodology of Science (AK2030)**
        - Hypothesis Testing & Statistical Reasoning
        - Models, Definitions & Experiments
        - Research Ethics & Risk Assessment
        """)

with tab_math:
    ma_col1, ma_col2 = st.columns(2)
    with ma_col1:
        st.markdown("""
            **Mathematical Methods in Physics (Advanced Graduate Level) (FK7048)**
            - **Differential Equations:** Method of Frobenius, Nonlinear ODEs, Sturm-Liouville Theorem.
            - **Complex Analysis:** Contour Integrals, Cauchy’s Theorem, Residue Theory, singularities.
            - **Special Functions:** Bessel, Neumann, Legendre, Gamma/Beta functions, Orthogonal Polynomials.
            - **Integral Transforms:** Fourier and Laplace Transforms, Convolution Theory, Green's Functions.
    """)
    with ma_col2:
        st.markdown("""
        **💻 Programming Techniques II (DA4007)**
        - **C++ Development:** OOP (Classes/Inheritance), Constructor/Destructor logic, Smart Pointers.
        - **Unix/Linux Environment:** Shell scripting, Terminal piping & redirection, LSW.
        - **Software Engineering:** Makefiles, Git version control, Debugging & Error handling.
        """)

with tab_sustain:
    st.markdown("""
    **🌱 Introduction to Sustainability Science (BL7041)**
    - Systems Thinking & Anthropocene Dynamics
    - Changemaking Options and Objectives
    - Reconnecting human systems with planetary boundaries
    """)

# PROJECTS = {
#     "🛡️ Autonomy in AI - Exploring the simulation-reality gap in humanoid robots and human accountability.": "https://tinyurl.com/576zs4vc",
#     "📈 ML for QKD Optimization - 270x speedup in quantum network parameter prediction using JAX & PyTorch.": "https://github.com/alanspace/QKD_KeyRate_Parameter_Optimization",
#     "🔬 Master Thesis - Secure Communication & Error Correction via Single Photon Polarisation.": "https://kth.diva-portal.org/smash/record.jsf?pid=diva2%3A1796647&dswid=-1650",
# }

# --- HIGHLIGHTED PROJECTS ---
# st.subheader("Selected Research & Technical Projects")
# for project, link in PROJECTS.items():
#     st.write(f"[{project}]({link})")

st.write('\n')

# --- CORE SKILLS ---
# st.subheader("Technical Qualifications")
# st.write(
#     """
# - 🏅 IBM Qiskit Certified Developer
# - 🏅 IBM Qiskit Advocate
# - 🏅 IBM Qiskit Localization Contributor - Platinum Level Translator
# - 🏅 National Section of International Physicists' Tournament
# - 💻 QuantumGrad Content Creator
# - 💻 Strong hands on experience and knowledge in Python
# - 🧠 Good understanding of Quantum AI and their respective applications
# - 🤝 Excellent team-player and displaying strong sense of initiative on tasks
# """
# )

# --- 6. ACHIEVEMENTS & COMMUNITY ---
st.write("---")
st.header("🏅 Achievements & Community Leadership")

ach_col1, ach_col2 = st.columns(2)

with ach_col1:
    st.markdown("""
    - **🏅 IBM Qiskit Advocate & Certified Developer**
    - **🤝 QAMP 2025 Mentee** (Quantum Certification Tutorial Development)
    - **🏆 Winner:** IBM Qiskit Global Hackathon (2020)
    """)

with ach_col2:
    st.markdown("""
    - **🌍 National Winner:** International Physicists' Tournament (2022)
    - **🎙️ Qiskit Hackathon Taiwan (2021):** Technical Mentor
    - **✍️ Content Creator:** QuantumGrad (Deep Tech Education)
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
