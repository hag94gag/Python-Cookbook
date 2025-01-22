
students = \
                {
                        "Ahmed": 
                                {
                                    "Math": "A",
                                    "Science": "D",
                                    "Draw": "B",
                                    "Sports": "C",
                                    "Thinking": "A"
                                },
                                
                        "Sayed": 
                                {
                                    "Math": "B",
                                    "Science": "B",
                                    "Draw": "B",
                                    "Sports": "D",
                                    "Thinking": "A"
                                },
                                
                        "Mahmoud": 
                                {
                                    "Math": "D",
                                    "Science": "A",
                                    "Draw": "A",
                                    "Sports": "B",
                                    "Thinking": "B"
                                }
                }
            

points={"A":100,"B":80,"C":40,"D":20}
total=0

for student, subjs in students.items():
    
    print(f"-- Student Name => {student}")
    print("*"*200)
    for subj in subjs:
        print(f"- {subj} => {points[students[student][subj]]} Points")
    print("\n\n")


# students = \
#     {
#             "Ahmed": 
#                 {
#                     "Math": "A",
#                     "Science": "D",
#                     "Draw": "B",
#                     "Sports": "C",
#                     "Thinking": "A"
#                 },
#             "Sayed": 
#                 {
#                     "Math": "B",
#                     "Science": "B",
#                     "Draw": "B",
#                     "Sports": "D",
#                     "Thinking": "A"
#                 },
#             "Mahmoud": 
#                 {
#                     "Math": "D",
#                     "Science": "A",
#                     "Draw": "A",
#                     "Sports": "B",
#                     "Thinking": "B"
#                 }
#     }
    
# points={"A":100,"B":80,"C":40,"D":20}
# total=0

# for student in students:
    
#     print(f"-- Student Name => {student}")
#     print("*"*200)
#     for subj in students[student]:
#         for deg in students[student][subj]:
#            print(f"- {subj} => {points[deg]} Points")
    
#     print("\n\n")




