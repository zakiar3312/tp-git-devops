def moyenne(liste):
    if not liste:
        raise ValueError("Liste vide")
    return sum(liste) / len(liste)
def mediane(liste):
    s = sorted(liste)
    n = len(s)
    return s[n//2] if n % 2 else (s[n//2-1] + s[n//2]) / 2
