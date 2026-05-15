with open('Español/D1/D1_imagen3/GoalBus.Driver.html', 'rb') as f:
    content = f.read()
    pos = content.find(b'Alan')
    if pos != -1:
        print(f"Found 'Alan' at position {pos}")
        start = max(0, pos - 50)
        end = min(len(content), pos + 50)
        print(f"Context: {content[start:end]}")
    else:
        print("'Alan' not found in binary search")
