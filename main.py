"""
Ce programme permet d'encoder une chaîne de caractères par une liste de tuples.

fonctions secondaires :
    - artcode_i(s) : encodent la chaîne de caractères passée en paramètre 
        à l'aide d'un algorithme itératif
    - artcode_r(s) : encodent la chaîne de caractères passée en paramètre 
        à l'aide d'un algorithme récursif

fonction principale ;
    - main() : test d'appel
"""
#### Imports et définition des variables globales

#### Fonctions secondaires

def artcode_i(s):
    """
    retourne la liste de tuples encodant une chaîne de caractères 
    passée en argument selon un algorithme itératif

    Args:
        s (str) : la chaîne de caractères à encoder

    Returns:
        list : la liste des tuples (caractère, nombre d'occurences)
    """
    # votre code ici
    c = [s[0]]
    o = [1]
    # continuité
    k = 1
    while k < len(s):
        if s[k] == s[k-1]:
            o[-1] += 1
        else :
            c = c + [s[k]]
            o = o + [1]
        k += 1
    return list(zip(c,o))


def artcode_r(s):
    """
    retourne la liste de tuples encodant une chaîne de caractères 
    passée en argument selon un algorithme récursif

    Args:
        s (str) : la chaîne de caractères à encoder

    Returns:
        list : la liste des tuples (caractère, nombre d'occurences)
"""
    code = []
    # cas de base
    if s == "":
        return code
    # calculer le nombre d'occurences du premier caractère de la chaîne
    c = [s[0]]
    o = [1]
    if s.startswith('\n'):
        c = ['\n']
    else :
        k = 1
        while k<len(s) and s[k]==s[k-1]:
            o[0] += 1
            k += 1
    code = list(zip(c,o))
    return code + artcode_r(s.replace(s[0],'',o[0]))

def main():
    """
    Permet de faire des tests d'appel
    """
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
