password = "p@ssword"
percobaan = 1

while percobaan <= 3: 
    userInput = input("Masukkan Password: ")

    if(userInput == password): 
        print("password benar")
        break
    else:
        percobaan += 1
        print("password yang anda input salah salah")

else: 
    print("akses anda di tolak")