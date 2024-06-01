import math

# 2D uzayda noktaları temsil eden 'points' listesini oluşturma
points = [(0, 0), (1, 1), (2, 2), (3, 3), (1, 2), (2, 1)]

# İki nokta arasındaki Öklid mesafesini hesaplayan fonksiyon
def euclideanDistance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# 'points' listesindeki her nokta çifti arasındaki mesafeleri hesaplama
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Minimum mesafeyi bulma
min_distance = min(distances)

# Sonucu yazdırma
print(f'Puanlar arasındaki minimum Öklid mesafesi: {min_distance}')
