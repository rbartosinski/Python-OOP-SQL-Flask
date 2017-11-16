def check_palindrome(wyraz):
    nowy = wyraz.replace(" ", "")
    nowy = nowy.upper()
    palindrom = nowy[::-1]
    if nowy == palindrom:
        return True
    else:
        return False

# return nowy == palindrom[::-1] - to wystarczy i tak przy porównaniu zwróci True lub False

print(check_palindrome("Kobyła ma Mały bok"))
print(check_palindrome(input("Sprawdź czy podane zdanie jest palindormem: ")))