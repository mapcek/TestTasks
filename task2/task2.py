with open(input("Путь к файлу с координатами и радиусом окружности: "), "r") as f:
    circle = f.read().split("\n")

coords = list(map(float, circle[0].split()))
radius = float(circle[1])

with open(input("Путь к файлу с координатами точек: "), "r") as f:
    points = f.read().split("\n")

points = [list(map(float, point.split())) for point in points]


def point_position(point, coords, radius):
    x, y = point
    cx, cy = coords
    distance = ((x - cx) ** 2 + (y - cy) ** 2) ** 0.5
    if distance < radius:
        return "1 - точка внутри"
    elif distance == radius:
        return "0 - точка лежит на окружности"
    else:
        return "2 - точка снаружи"


for point in points:
    print(point_position(point, coords, radius))
