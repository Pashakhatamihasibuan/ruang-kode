for t in [1900, 2000, 2024, 2025]:
    kabisat = (t % 4 == 0 and t % 100 != 0) or t % 400 == 0
    print(t, "kabisat?", kabisat)
