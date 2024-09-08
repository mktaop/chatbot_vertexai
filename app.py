
import streamlit as st
import streamlit.components.v1 as components

st.subheader("Chatbot using Vertex AI Agent Builder.")

html_code="""

<!DOCTYPE html>
<html>
<head>
  <title>Your Custom Chatbot</title>
  <style>
    body {
      background-color: lightblue;
    }
  </style>
</head>
<body>
  <h1>Your Custom Chatbot</h1>
  <p>This is a test only. Please add additional information you wish to include.</p>
</body>
</html>

....INSERT THE HTML FROM AGENT BUILDER HERE.....
    
"""

components.html(html_code, height=650,  scrolling=True)
