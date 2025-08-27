from dotenv import load_dotenv
load_dotenv()  # load all the environment variables

import streamlit as st
import os
import sqlite3
import google.generativeai as genai

# Configure our API Key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Function to load Google Gemini model and provide SQL Query as response
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")  # ✅ correct model
    response = model.generate_content([prompt[0], question])
    return response.text

# Function to retrieve query from the SQL database
def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

# Define Your Prompt
prompt = [
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS,
    SECTION and MARKS.

    Example 1: How many entries of records are present?
    SQL: SELECT COUNT(*) FROM STUDENT;

    Example 2: Tell me all the students studying in Data Science class?
    SQL: SELECT * FROM STUDENT WHERE CLASS="Data Science";

    Important:
    - Do NOT include ``` or the word "sql" in the output.
    - Do NOT include any comma after the generated answer.
    """
]

# Streamlit App
st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("Gemini App To Retrieve SQL Data")

question = st.text_input("Input: ", key="input")

submit = st.button("Ask the question")

# If submit is clicked
if submit:
    response = get_gemini_response(question, prompt)
    st.subheader("Generated SQL Query")
    st.code(response, language="sql")

    try:
        data = read_sql_query(response, "student.db")
        st.subheader("The Response is")
        for row in data:
            st.write(row)
    except Exception as e:
        st.error(f"Error: {e}")