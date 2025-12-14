#!/usr/bin/env python3
import os
import sys
from urllib.parse import parse_qs

print("Content-Type: text/html\n")

data = ""
if os.environ.get("REQUEST_METHOD") == "POST":
    length = int(os.environ.get("CONTENT_LENGTH", 0))
    data = sys.stdin.read(length)
else:
    data = os.environ.get("QUERY_STRING", "")

params = parse_qs(data)
L = params.get("L", [""])[0]

hasil = ""
if L.isdigit():
    L = int(L)
    hasil = f"<p>Luas Persegi: {L * L}</p>"

print(f"""
<!DOCTYPE html>
<html>
<body>
    <form method="post">
        <input type="number" name="L" required>
        <button>Hitung</button>
    </form>
    {hasil}
</body>
</html>
""")
