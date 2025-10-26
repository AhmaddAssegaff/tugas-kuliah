print("Program mengihitung huruf vokal.")
print("Dibuat oleh Ahmad")

kalimat = "Pembunuhan rakyat sipil adalah kejahatan perang."
vokal = "aiueoAIUEO"
jumlah_huruf_vokal = 0

for huruf in kalimat:
    if huruf in vokal:
        jumlah_huruf_vokal += 1

print(kalimat, "memiliki total huruf vokal", jumlah_huruf_vokal)
