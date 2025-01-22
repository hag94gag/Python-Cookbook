def get_people_scores(name="nUl1",**subjs):
    if name!="nUl1":
        print(f"Hello {name}")
    if subjs:
        print ("Your Scores:")
        for sub, score in subjs.items():
            print(f'"{sub} => {score}"')
    else:
        print("You Have No Scores To Show")







get_people_scores("Osama", Math=90, Science=80, Language=70)
get_people_scores(Logic=70, Problems=60)
get_people_scores("Ahmed")

