while True:
    try:
        email = input("input your email here: ")
        domain_start = email.index('@') + 1
        domain = email[domain_start:]
        print("The domain name is", domain)
        break
    except ValueError:
        print("Wrong input. Please input an email.")