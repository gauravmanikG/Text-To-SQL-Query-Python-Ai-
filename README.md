# 📝 Text-To-SQL using Streamlit + Gemini API

A simple yet powerful AI-powered SQL Query Generator.  
Just write your question in plain English (or even casual WhatsApp-style language), and the app will generate the correct SQL query and execute it on the database.

---

## 🚀 Tech Stack
- **Python 3**
- **Streamlit** → for interactive UI  
- **Google Gemini API** → AI-powered query generation  
- **SQLite** → local DB for demo, can be extended  
- **dotenv** → for API key management  

---

## ✨ Features
- 🗣 **English to SQL** → Write simple English, and get instant SQL queries & results.  
- 💬 **WhatsApp-style input** → Even informal text like *"show me all sci stud"* works!  
- 🤖 **AI Learning Mode** → If you’re learning SQL, you can ask:
  - "Write a query using HAVING clause"  
  - "Give me an example with SELECT"  
- 🎨 **Custom Settings** → Change theme and layout from the Streamlit settings sidebar.  
- ☁️ **Easy Deployment** → Deploy directly with one click from Streamlit’s top-right menu.  

---

## ⚡ Installation

Clone the repo:
```bash
git clone https://github.com/YOUR_USERNAME/Text-To-SQL.git
cd Text-To-SQL
Create a virtual environment & install dependencies:

python -m venv venv
# On Mac/Linux
source venv/bin/activate
# On Windows
venv\Scripts\activate

pip install -r python/requirements.txt
Add your Gemini API key in .env file:


GEMINI_API_KEY=your_api_key_here
Run the app:


streamlit run python/app.py
🛠 Project Structure
🔥 Note: All main project files are inside the python/ folder.



Text-To-SQL/
│── assets/               # Screenshots & assets
│── python/               # Main project source code
│   ├── app.py            # Main Streamlit app
│   ├── sql.py            # DB helper functions
│   ├── student.db        # Sample SQLite DB
│   └── requirements.txt  # Python dependencies
│── package.json          # (Optional frontend config)
│── .env                  # API key (ignored in git)
│── .gitignore
🌍 Deployment
One-click deploy on Streamlit Cloud

Or host on Render / Railway / HuggingFace Spaces

🤝 Contributing
Contributions are welcome! Fork the repo, open a PR, and let’s make this tool even better 🚀

📜 License
This project is licensed under the MIT License.

yaml

---

This way, anyone who visits your repo immediately sees:
- That the **important files live under `python/`**.  
- How to **install and run** correctly.  

---
