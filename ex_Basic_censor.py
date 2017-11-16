def censor(lancuch):
    wszystkie = lancuch.split()
    niedozwolone = ["Java", "C#", "Ruby", "PHP"]
    dozwolone =[]
    for i in wszystkie:
        if i in niedozwolone:
            dozwolone.append("****")
        else:
            dozwolone.append(i)
    return " ".join(dozwolone)

c = censor("Java is the best, but PHP is the bestest!")  # ;-)
print (c)
