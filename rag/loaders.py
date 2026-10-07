from pathlib import Path

print(Path(__file__))

p = Path(__file__).resolve()

print(p.parents[0])

print(p.parents[1])

print(p.parents[2])