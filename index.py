import math

# Noktaların tanımlanması
points = [(2, 3), (5, 8), (10, 15), (4, 6), (7, 9)]

# Öklid mesafesi için fonksiyon tanımlama
def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Mesafelerin hesaplanması için
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Minimum mesafenin bulunması için
min_distance = min(distances)

# Sonucu yazdırmak için
print("Minimum mesafe:", min_distance)
