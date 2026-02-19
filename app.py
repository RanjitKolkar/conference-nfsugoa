import streamlit as st

st.set_page_config(
    page_title="Conference on Mapping and Mitigating Telecom-enabled Frauds",
    page_icon="📡",
    layout="wide",
)

# --- Clean Theme ---
st.markdown("""
<style>
html, body, .stApp {
    background-color: #ffffff;
    color: #000000;
}
h1, h2, h3 {
    color: #003366;
}
.stButton button {
    background-color: #003366;
    color: white;
    border-radius: 8px;
    padding: 10px 24px;
    font-size: 16px;
}
.footer {
    text-align: center;
    margin-top: 30px;
    padding: 15px;
    color: #003366;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

# ================= HEADER =================
col1, col2 = st.columns([1, 4])

with col1:
    st.image("nfsu emblem logo.png", use_container_width=True)

with col2:
    st.markdown("""
    <div style="text-align:center">
        <h3>National Forensic Sciences University, Goa Campus</h3>
        <h2>One Day Conference</h2>
        <h1>Conference on Mapping and Mitigating Telecom-enabled Frauds</h1>
        <p><b> 7 March 2026 | 📍 NFSU Goa Campus, Curti, Ponda | 💻 Hybrid Mode</b></p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ================= ABOUT =================
st.subheader("📌 About the Conference")

st.write("""
In recent years, **telecom-enabled fraud** has seen a sharp rise globally. 
These crimes frequently originate far beyond the jurisdiction of their victims, 
creating significant geographical barriers that complicate investigations and hinder timely justice.

As cyber-enabled and transnational offences, telecom frauds demand:
- Thorough understanding of modus operandi  
- Enhanced international cooperation  
- Strong techno-legal frameworks  
- Well-coordinated institutional mechanisms  

To address these emerging challenges, NFSU Goa is organising this one-day conference 
to examine the evolving threat landscape of telecom-enabled frauds, 
its cross-border implications, and the critical regulatory and techno-legal measures required.
""")

# ================= SUB-THEMES =================
st.subheader("🎯 Conference Sub-Themes")

st.markdown("""
**1️⃣ Telecom Based Cyber Frauds – Current Challenges and Way Forward**

**2️⃣ Regulatory and Techno-legal Challenges in Telecom-enabled Cyber Frauds**
""")

# ================= CALL FOR PAPERS =================
st.subheader("📄 Call for Papers")

st.write("""
The conference provides an excellent platform for researchers, academicians, 
policy professionals, and practitioners to present their research through:

- 🎤 Oral Presentations  
- 🖼 Poster Presentations  

Selected papers will be published in:
- *NFSU Journal of Cyber Security and Digital Forensics*
- *NFSU Journal of Forensic Science*
""")

# ================= TIMELINE =================
st.subheader(" Conference Timeline")

st.markdown("""
| Event | Date |
|-------|------|
| Paper Submission Deadline | 28 February 2026 |
| Acceptance Notification | 1 March 2026 |
| Conference Date | 7 March 2026 |
""")

# ================= SUBMISSION =================
st.subheader("📎 Submission Details")

st.info("Paper Submission Link: To be provided soon.")

st.markdown("""
<a href="#" target="_blank">
<button>
📌 Submit Paper
</button>
</a>
""", unsafe_allow_html=True)

# ================= TARGET PARTICIPANTS =================
st.subheader("👥 Who Should Attend?")

st.markdown("""
- Researchers & Research Scholars  
- Faculty Members  
- Law Enforcement Officials  
- Policy Makers  
- Telecom & Cyber Security Professionals  
- Legal Experts  
""")

# ================= FOOTER =================
st.markdown("---")
st.markdown("""
<div class="footer">
📍 Organized by <b>National Forensic Sciences University (NFSU), Goa Campus</b><br>
Curti, Ponda, Goa<br><br>
📧 Contact: ranjit.kolkar@nfsu.ac.in
</div>
""", unsafe_allow_html=True)
