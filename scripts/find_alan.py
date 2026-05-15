with open('Español/D1/D1_imagen3/GoalBus.Driver.html', 'r', encoding='utf-8', errors='ignore') as f:
    for i, line in enumerate(f, 1):
        if 'Alan' in line:
            print(f"Line {i}: {line.strip()}")
