import shelve

F = shelve.open("ahmad")
print(F["data"])
F.close()
