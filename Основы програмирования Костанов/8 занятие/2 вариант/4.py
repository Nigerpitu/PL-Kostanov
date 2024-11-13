def s_angle(a,b):
    s = a*b
    return s

ans = []

for i in range(3):
    a = int(input())
    b = int(input())
    ans.append(s_angle(a, b))

print("Площади трёх треугольников",ans)
