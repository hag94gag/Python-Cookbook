email=input("Enter your E-mail: ").lower()
fname=email.split('@')[0].capitalize()
EmailProvider=email.split('@')[1].split('.')[0]
domain=email.split('.')[1]
print(f"Your name is: {fname}")
print(f"Your Email provider is: {EmailProvider}")
print(f"Your Top level domain is: {domain}")