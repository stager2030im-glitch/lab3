temperaturas = [18, 25, 31, 12, 28, 35, 20]

fria = 0
templados = 0 
caluroso = 0

for temp in temperaturas:
    if temp < 15:
        clasificacion = "fria"
        fria += 1
    elif temp <= 25:
        clasificacion = "templados"
        templados += 1
    elif temp > 25:
        clasificacion = "caluroso"
        caluroso += 1    

    print(f"{temp}°C -> {clasificacion}")

print("\nResumen de dias:")
print(f"frios: {fria}")
print(f"templados: {templados}")
print(f"caluroso: {caluroso}")