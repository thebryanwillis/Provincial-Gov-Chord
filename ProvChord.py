import chord

matrix = [
    [0, 0, 0, 2, 1],
    [0, 0, 0, 2, 6],
    [0, 0, 2, 0, 0],
    [2, 1, 0, 0, 0],
    [2, 6, 0, 0, 0],
]

names = ["Centre-left", "Centre-right", "Nonpartisan", "Minority", "Majority"]

chord.Chord(matrix, names).to_html()