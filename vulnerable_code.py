# vulnerable_code.py
from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

# VULNERABILITY 1: SQL Injection (SQLi)
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    # TƏHLÜKƏLİ: İstifadəçi məlumatı birbaşa SQL sorğusunun içinə string formatında birləşdirilir (String Concatenation)
    # Hücumçu bura " ' OR '1'='1 " yazaraq parolu bilmədən giriş edə bilər.
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute(query)
    user = cursor.fetchone()
    
    if user:
        return "Giriş uğurludur!"
    return "Yanlış istifadəçi adı və ya parol!"

# VULNERABILITY 2: Reflected Cross-Site Scripting (XSS)
@app.route('/search')
def search():
    query = request.args.get('q', '')
    
    # TƏHLÜKƏLİ: İstifadəçinin axtarış sözü heç bir təmizləmə (Sanitization) olmadan HTML-ə basılır.
    # Hücumçu bura <script>alert(1)</script> yazaraq icazəsiz kod işlədə bilər.
    html_template = f"<h1>Axtarış nəticəsi: {query}</h1>"
    
    return render_template_string(html_template)

if __name__ == '__main__':
    app.run(debug=True)
