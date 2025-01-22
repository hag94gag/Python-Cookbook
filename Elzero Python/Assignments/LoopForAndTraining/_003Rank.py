


my_ranks = {
  'Math': 'A',
  "Science": 'B',
  'Drawing': 'A',
  'Sports': 'C'
}

points={"A":100,"B":80,"C":40}

total=0

for subj, rank in my_ranks.items():
    print(f"My rank in {subj} is {rank} Which Equal {points[rank]} Points")
    total+=points[rank]
print(f"The total points are {total}")