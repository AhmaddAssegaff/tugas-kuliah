password = "p@ssword"

for index in range(3): 
    userInput = input("Masukkan Password: ")

    if(userInput == password): 
        print("password benar")
        break
    else:
        print("password yang anda input salah salah")

else: 
    print("akses anda di tolak")