"""
Funkcija akceptē divus argumentus - skaiļus a un b,
aprēķina to dalījumu un atgriež to. Ja skaiļus dalīt nedrīkst,
atgriež 0.

Argumenti:
    a {int vai float} -- pirmais skaitlis
    b {int vai float} -- otrais skaitlis
Atgriež:
    int vai float -- rezultāts

"""
def dali(sk1, sk2):
    #sk1 = float(input("Ievadiet pirmo skaitli: "))
    #sk2 = float(input("Ievadiet otro skaitli: "))
    dali = sk1 / sk2
    print("Dalījums ir:", dali)

    return dali