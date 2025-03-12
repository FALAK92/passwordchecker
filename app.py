import streamlit as st
import re

st.set_page_config(page_title="Password Strength Checker" , page_icon="🔒")
st.title("🔑 Password Strength Checker")
st.markdown(''''
## Welcome To Ultimate Passwrod Checker 👋 
Use this tool to check your passwrod strength and this tool get suggestion on how to make password more strong 
            we will helpful to you 😊  ''')

password = st.text_input("Enetr Your Password" , type="password")

suggestion = []

counter = 0

if password:
    if len(password) >= 8:
        counter += 1
    else:
        suggestion.append("👎Password should be at least 8 characters long")

    if re.search(r'[A-Z]', password) and re.search(r'[a-z]' , password):
        counter += 1
    else:
        suggestion.append("👎Password should have at least one uppercase and one lowercase letter")
    
    if re.search(r'[\d]', password):
        counter += 1
    else:
        suggestion.append("👎Password should have at least one digit")

    if re.search(r'[@#$%&*]', password):
        counter += 1
    else:
        suggestion.append("👎Password should have at least one special character(@#$%&*)")

    if counter == 4:
        suggestion.append(" 👍Password is strong")
    elif counter == 3:
        suggestion.append("🆗Password is better")
    else:
        suggestion.append("🚫Password is weak")

    if suggestion:
        st.markdown(" ## Improvement")
        for allrules in suggestion:
            st.markdown(f"## {allrules}") 

else:
        st.info( "🙏Please enter your password to check its strength" )
