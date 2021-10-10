# TURDEAN PAULA-FLORINA PROBLEMELE 3 SI 4 + (LA ALEGERE) PROBLEMA 5 si PROBLEMA 1
from typing import Union


def is_prime(x):
    """
    Determina daca un n umar este prim sau nu.
    :param x: Numarul verificat.
    :return: Returneaza True daca numarul este prim si False in caz contrar
    """
    if x < 2:
        return False
    for i in range(2, x//2):
        if x % i == 0:
            return False
    return True


def test_is_prime():
    assert is_prime(0) is False
    assert is_prime(2) is True


def get_goldbach(n) -> Union[(int, int)]:
    """
    Descompune un numar in suma de doi termeni primi.
    :param n: Numarul descompus.
    :return: Returneaza cei doi temeni (numere intregi).
    """
    if int(n) < 3:
        if int(n) % 2 != 0:
            print("Numarul nu este valabil")
            breakpoint()
    else:
        for i in range(2, int(n)//2):
            if is_prime(i) is True and is_prime(int(n)-i) is True:
                return i, int(n)-i


def test_get_goldbach():
    assert get_goldbach(36) == (5, 31)


def is_palindrome(n) -> bool:
    pal = 0
    copie = int(n)
    while copie > 0:
        digit = copie % 10
        pal = pal * 10 + digit
        copie = copie//10
    if int(n) == pal:
        return True
    else:
        return False


def test_is_palindrome():
    assert is_palindrome(5665) is True
    assert is_palindrome(1234) is False


def get_largest_prime_below(n):
    copie = int(n)
    for i in range(copie, 2, -1):
        if is_prime(i) is True:
            return i


def test_get_largest_prime_below():
    assert get_largest_prime_below(18) == 17
    assert get_largest_prime_below(3) == 2


def get_newton_sqrt(n, steps) -> float:
    copie = float(n)
    for i in range(steps):
        n = 0.5 * (n + copie/n)
    return n


def test_get_newton_sqrt():
    assert get_newton_sqrt(9, 2) == 3.4


shouldRun = True
while shouldRun:
    print("1)Determină numerele prime p1 si p2 astfel încât n = p1 + p2. Pentru ce fel de n există soluție?")
    print("2)Determina radicalul unui număr dat folosind metoda lui Newton.")
    print("3)Găsește ultimul număr prim mai mic decât un număr dat.")
    print("4)Determină dacă un număr dat este palindrom.")
    print("x)Iesire")
    optiune = input("Alegeti o optiune: ")
    if optiune == "1":
        nr = input("Dati un numar: ")
        print(get_goldbach(nr), " Exista solutii doar pentru numerele >3 si pare")
    elif optiune == "2":
        nr = float(input("Dati un  numar: "))
        st = int(input("Dati un numar de pasi: "))
        print(get_newton_sqrt(nr, st))
    elif optiune == "3":
        nr = input("Dati un numar: ")
        print(get_largest_prime_below(nr))
    elif optiune == "4":
        nr = input("Dati un numar: ")
        print(is_palindrome(nr))
    elif optiune == "x":
        print("Ati iesit din program")
        shouldRun = False
    else:
        print("!!! Optiune gresita !!!")
