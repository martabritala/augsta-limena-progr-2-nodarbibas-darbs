import pytest
from src.trisstura_laukums import trissturi

def h():
    assert trissturis([1,3,5])==1
    
def p():
    assert trissturis([100,3,70])==2

"""
B. Trijstūra laukums
Funkcija akceptē divus argumentus - trisjtūra augstumu un pamatu,
aprēķina trijstūra laukumu un atgriež to. Ja kāds no argumentiem ir mazāks vai vienāds ar 0, atgriež 0.
Formula trijstūra laukuma aprēķināšanai ir augstums*pamats/2

Argumenti:
    h {int vai float} -- trijstūra augstums
    p {int vai float} -- trijstūra pamats
Atgriež:
    int vai float -- rezultāts
def trissturis(p, h):
    laukums = 0
    if p<=0 or h<=0:
        laukums = 0
    else:
        laukums = (p*h)/2
    return laukums

"""