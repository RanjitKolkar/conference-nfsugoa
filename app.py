import streamlit as st

st.set_page_config(
    page_title="Conference on Telecom-enabled Frauds Mapping and Mitigation",
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
        <h2>One Day Conference on</h2>
        <h1>Telecom-enabled Frauds Mapping and Mitigation</h1>
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

# ================= CONFERENCE THEMES =================
st.subheader("🎯 Conference Themes")

st.markdown("""
### **Theme 1: Telecom-enabled Frauds – Current Challenges and Way Forward**

Includes, but is not limited to, the following areas:

1. Phishing, Vishing, and Caller ID Spoofing in telecommunications  
2. SIM and eSIM vulnerabilities  
3. Fraudulent OTT-linked communication and impersonation through spoofed caller IDs  
4. Emerging trends such as SIM Box fraud, IRSF (International Revenue Share Fraud), Wangiri scams, etc.  
5. Role of Generative AI in telecom frauds, including robocalls and AI-driven phishing  
6. Mule account misuse and financial layering techniques  
7. SIM swapping and identity takeover  
8. OTP interception and authentication bypass mechanisms  
9. Digital arrest scams, investment fraud, and advanced social engineering techniques  
10. Cyber-enabled and cyber-dependent telecom frauds  
11. Cross-border spoofing and organised telecom fraud operations  

### **Theme 2: Regulatory and Techno-legal Safeguards to Combat Telecom-enabled Frauds**

1. Regulatory and legal frameworks for safeguarding against telecom-enabled frauds  
2. Legal remedies, enforcement challenges, and prosecutorial mechanisms  
3. Global regulatory initiatives and international cooperation frameworks  
4. Accountability of telecom service providers, OTT platforms, and social media intermediaries  
5. Victim-centric regulatory and policy approaches to telecom-enabled fraud prevention  
""")
# ================= CALL FOR PAPERS =================
st.markdown("## 📄 Call for Papers")

st.markdown("""
<div style="
background-color:#f4f8ff;
padding:20px;
border-radius:12px;
border-left:6px solid #003366;
">

The conference provides an excellent platform for researchers, academicians, 
policy professionals, and practitioners to present original and unpublished research through:

<ul>
<li>🎤 <b>Oral Presentations</b></li>
<li>🖼 <b>Poster Presentations</b></li>
</ul>

Selected high-quality papers will be considered for publication in:
<ul>
<li><i>NFSU Journal of Cyber Security and Digital Forensics</i></li>
<li><i>NFSU Journal of Forensic Science</i></li>
</ul>

</div>
""", unsafe_allow_html=True)



# ================= TIMELINE =================
st.markdown("## 📅 Conference Timeline")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div style="background:#e8f0ff;padding:15px;border-radius:10px;text-align:center;">
    <b>📌 Submission Deadline</b><br>
    28 February 2026
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="background:#e8f0ff;padding:15px;border-radius:10px;text-align:center;">
    <b>📢 Acceptance Notification</b><br>
    1 March 2026
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style="background:#003366;color:white;padding:15px;border-radius:10px;text-align:center;">
    <b>🎓 Conference Date</b><br>
    7 March 2026
    </div>
    """, unsafe_allow_html=True)



# ================= SUBMISSION =================
st.markdown("## 📎 Submission Portal")

st.markdown("""
<div style="text-align:center; margin-top:10px;">
<a href="https://docs.google.com/forms/d/e/1FAIpQLSe0TRBmJHpeojZS7yQF9aZMZsMxMNVeJgIMMpj9hHDoHCssfg/viewform" target="_blank">
<button style="
background-color:#003366;
color:white;
padding:14px 30px;
border:none;
border-radius:10px;
font-size:18px;
cursor:pointer;
">
🚀 Submit Your Paper
</button>
</a>
</div>
""", unsafe_allow_html=True)

st.info("📌 All submissions must adhere to the prescribed conference format guidelines.")
# ================= PAPER SUBMISSION FORMAT =================
st.subheader("📝 Paper Submission Format")

st.write("""
All papers must be prepared strictly in **IEEE Conference Format**.

Authors are required to:
- Use the official IEEE conference template (MS Word or LaTeX)
- Follow double-column format
- Maintain proper referencing style as per IEEE guidelines
- Limit the paper length to 6–8 pages (including references)
- Ensure originality and avoid plagiarism and AI generated content. 

Submissions not adhering to IEEE format may be returned for revision.
""")

st.markdown("""
🔗 **Download Official IEEE Conference Templates:**

[Click Here to Download IEEE Templates](https://www.ieee.org/conferences/publishing/templates.html)
""")

st.info("📌 Authors are advised to carefully follow IEEE formatting guidelines before submission.")

# ================= TARGET PARTICIPANTS =================
st.subheader("👥 Who Should Attend?")

st.markdown("""
- Researchers & Research Scholars  
- Academicians 
- Law Enforcement Officials  
- Telecom & Cyber Security Professionals  
- Legal Experts and Policy Makers 
""")



# ============ ORGANIZING COMMITTEE ============
st.subheader("👥 Organizing Committee")
st.markdown("""
<div class="highlight-box">
<b>Chief Patron:</b> Dr. J. M. Vyas, Hon'ble Vice-Chancellor, NFSU <br>
<b>Chair:</b> Prof. (Dr.) Naveen Kumar Chaudhary, Director, NFSU Goa  <br>
<b>Co-Chair:</b> Dr. Lokesh Chouhan, Dean Academics, NFSU Goa  <br>
<b>Convener:</b> Dr. Sandeep Munjal, Assistant Professor, NFSU Gandhinagar<br>
<b>Coordinator:</b> Dr. Panem Charanarur, Assistant Professor, NFSU Goa<br>
<b>Coordinator:</b> Dr. Ranjit Kolkar, Assistant Professor, NFSU Goa<br>
<b>Coordinator:</b> Mr. Harsh Panchal, Lecturer, NFSU Goa<br>

""", unsafe_allow_html=True)

# ================= FOOTER =================
st.markdown("---")
st.markdown("""
<div class="footer">
📍 Organized by <b>National Forensic Sciences University (NFSU), Goa Campus</b><br>
Curti, Ponda, Goa<br><br>
Contact: sandeep.munjal@nfsu.ac.in, 8587089702  |  ranjit.kolkar@nfsu.ac.in, +91 8618879217
</div>
""", unsafe_allow_html=True)
