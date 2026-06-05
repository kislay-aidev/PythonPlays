from scipy.spatial.distance import cosine as cos
p1 = (1, 0)
p2 = (10, 2)

bus = cos(p1, p2)
print (bus)