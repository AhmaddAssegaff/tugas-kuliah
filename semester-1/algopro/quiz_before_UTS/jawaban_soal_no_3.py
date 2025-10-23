Z = 'L200250034'
m = Z[9:6:-1]
n = int(m[0])
p = int(m) + 19
q = 15 - n
r = p // 10
s = 2 * m
t = p % q
u = t ** 2
v = p - t
w = n < 6
print(m, n, p, q, r, s, t, u, v, w)
