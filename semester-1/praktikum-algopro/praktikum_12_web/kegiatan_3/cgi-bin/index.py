#!/usr/bin/env python3
import cgi

print("Content-Type: text/html\n")

form = cgi.FieldStorage()
L = form.getfirst("L", "")

hasil = ""
if L.isdigit():
    L_int = int(L)
    hasil = f"<p>Luas Persegi: {L_int * L_int}</p>"

print(f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>CGI Persegi</title>
    <link rel="stylesheet" href="/static/style.css">
</head>
<body>
    <h1>Nama Bangun Datar: Persegi</h1>
    <p>Dimensi: 2D</p>
    <p>Rumus Luas: L × L</p>

    <form method="post" action="/cgi-bin/index.py">
        <label>Masukkan L:</label>
        <input type="number" name="L" required>
        <button type="submit">Hitung</button>
    </form>

    {hasil}
</body>
</html>""")
