import re
import streamlit as st

def check_password_strength(password):
    strength = 0
    remarks = []
    
    if len(password) >= 8:
        strength += 1
    else:
        remarks.append("🔴 Password should be at least 8 characters long.")
    
    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        remarks.append("🟠 Include at least one uppercase letter.")
    
    if re.search(r'[a-z]', password):
        strength += 1
    else:
        remarks.append("🟠 Include at least one lowercase letter.")
    
    if re.search(r'\d', password):
        strength += 1
    else:
        remarks.append("🟡 Include at least one number.")
    
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    else:
        remarks.append("🟡 Include at least one special character (!@#$%^&* etc.).")
    
    return strength, remarks

def main():
    st.set_page_config(page_title="Fortify Password Analyzer", page_icon="🔒", layout="centered")
    
    st.markdown("""
        <h1 style='text-align: center; color: #4CAF50;'>🔐 Fortify Password Analyzer</h1>
        <p style='text-align: center; font-size: 18px;'>Check your password strength and get personalized security suggestions.</p>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    password = st.text_input("Enter your password:", type="password", help="Make sure your password is strong for better security.")
    
    if st.button("🔍 Analyze Password", use_container_width=True):
        if password:
            strength, remarks = check_password_strength(password)
            
            st.divider()
            
            if strength == 5:
                st.success("✅ Strong Password: Your password is highly secure!")
            elif strength >= 3:
                st.warning("⚠️ Moderate Password: You can improve security with a few tweaks.")
            else:
                st.error("❌ Weak Password: Your password needs significant improvement.")
            
            st.subheader("🔧 Suggestions to Improve:")
            for remark in remarks:
                st.write(f"- {remark}")
        else:
            st.error("❗ Please enter a password to analyze.")

if __name__ == "__main__":
    main()

