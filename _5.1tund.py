# #1
# def arithmetic(arv1: float, arv2:float, tehe: str):
#     """
#     Funktsioon töötab nagu lihtme kalkulaator
#     + - liitmine
#     - - lahutamine
#     * - korrutamine
#     / - jagamine
#     kui sisend ei ole järjendis [+,-,/,*], siis tagastab sõne "Tundmatu tehe"
#     :perem float arv1: Sisend ujukomaarv tüübina
#     :perem float arv2: Sisend ujukomaarv tüübina
#     :rtype: varMääramata tüüp (float või srt)
#     """
#     if tehe in["+", "-", "/", "*"]:
#         if arv2==0 and tehe=="/":
#             vastus="DIV/0"
#         else:
#             vastus=eval(str(arv1)+tehe+str(arv2))
#     else:
#         vastus="Tunndmatu tehe"
#     return vastus


# #2
# def is_year_leap(aasta:int)->bool:
#     """Liigaasta leidmine
#     Tagastab True, kui aasta on liigaasta ja False kui aasta on tavaline aasta
#     :param int aasta:Sisend kasutajalt
#     :rtype: bool tõeväärsuses formaadis tulemus
#     """
#     if aasta%4==0:
#         v=True
#     else:
#         v=False
#     return v

# #3
# def square(külg:float)->any:
#     """"Ruudu pindala, ümbermõõdu ja diagonaali leidmine
#     :param float külg: Sisend kasutajalt
#     :rtype: float S,P,d
#     """

#     S=külg**2
#     P=4*külg
#     d=round((2)**(1/2)*külg)
#     return S,P,d

# #4
# def season(param:int)->str:
#     """Kirjeldage funktsioon
#     :param ...:...in range(1,13)
#     :rtype:...Hooajanimetus
#     """
#     if param in [1,2,12]:
#         H="Talv"
#     elif param in [3,4,5]:
#         H="Kevad"
#     elif param in [6,7,8]:
#         H="Suvi"
#     else:
#         H="Sügis"
#     return H

# #5
# def bank(summa:float, aastad:int)->float:
#     """Kirjeldage funktsioon
#     :param ...:...aastad
#     :param ...:...summa
#     :rtype:...Hooajanimetus
#     """
#     for aasta in range(aastad):
#         summa*=1.1
#     return summa

# #6
# from random import*
# def is_prime(a=randint(1,10000))->bool:
#     """Kirjeldage funktsioon
#     :param ...:...in range(1,10000)
#     :rtype:...Hooajanimetus
#     """
#     print(a)
#     v=True 
#     for jagaja in range(2,a):
#         if a%jagaja==0:
#             v=False
#     return v

#7
def is_year_leap(aasta: int) -> bool:
    return (aasta % 4 == 0 and aasta % 100 != 0) or (aasta % 400 == 0)
def date(päev: int, kuu: int, aasta: int) -> bool:
    """Kirjeldage funktsioon
    :param päev: päev (1-31)
    :param kuu: kuu (1-12)
    :param aasta: aasta (>0)
    :rtype: bool
    """
    if päev in range(1,32) and kuu in[1,3,5,7,8,10,12] and aasta>0:
        v=True
    elif päev in range(1,30) and kuu==2 and is_year_leap(aasta):
        v=True
    elif päev in range(1,29) and kuu==2 and is_year_leap(aasta):
        v=True
    if päev in range(1,31) and kuu in[4,6,9,11] and aasta>0:
        v=True
    else:
        v=False
    return v
