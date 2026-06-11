# secure_code.py
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

# FIXED 1: Parameterized Query against SQL Injection
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    # TƏHLÜKƏSİZ: '?' işarələrindən istifadə edərək məlumatlar SQL sorğusundan tam təcrid olunur (Parameterized Query)
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    cursor.execute(query, (username, password))
    user = cursor.fetchone()
    
    if user:
        return "Giriş uğurludur!"
    return "Yanlış istifadəçi adı və ya parol!"

# FIXED 2: HTML Escaping against Cross-Site Scripting (XSS)
@app.route('/search')
def search():
    query = request.args.get('q', '')
    
    # TƏHLÜKƏSİZ: render_template funksiyası daxil olan xüsusi simvolları (&, <, >) avtomatik zərərsizləşdirir (HTML Entity Escaping)
    # Artıq <script> yazılsa belə, o kod kimi yox, sadəcə adi yazı kimi ekranda görünəcək.
    return render_template('search_results.html', query=query)

if __name__ == '__main__':
    app.run(debug=False) # Təhlükəsizlik üçün debug rejimini bağlayırıq
