def show_skills (name,*skills):
    if not skills:
        print(f"Hey {name} you don't have any skills yet")
    else:
        print(f"Hey {name}")
        for skill in skills:
            print(skill)
            
show_skills("Osama", "HTML", "CSS", "JS", "Python")
show_skills("Ahmed")