#!/usr/bin/env python3

import cgi

print("Content-Type: text/html\n")

print("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>CGI Test</title>
</head>
<body>
    <h1>DATA DIRI</h1>
    <p>nama : Ahmad</p>
    <p>Alamat: di jalan</p>
    <p>tempat, tanggal-lahir: Surakarta, 12-06-2006</p>
    <p>tempat wisata fav: di hatimu</p>
    <p>motto: hiduplah</p>
</body>
</html>""")
