import random
def ball ():
    ballcontent=\
                    [
                        [  
                            "Yes",
                            "Definitely",
                            "Without a doubt",
                            "You may rely on it"
                        ]
                        ,
                        [   
                            "No",
                            "My sources say no",
                            "Outlook not so good",
                            "Very doubtful"
                        ]
                        ,
                        [   
                            "Ask again later",
                            "Cannot predict now",
                            "Reply hazy, try again",
                        ]
                        ,
                        [   
                            "Concentrate and ask again",
                            "Yes, but not likely"
                        ]
                        
                    ]
    print(random.choice(random.choice(ballcontent)))

Ques=input("Enter a Question: ")
ball()