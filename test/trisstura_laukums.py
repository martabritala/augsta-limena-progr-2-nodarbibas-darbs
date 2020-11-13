import pytest
from src.trisstura_laukums import trissturi

def test_vesel_pozitivi():
    assert trissturi(2, 3) == 2

def test_poz_dala():
    assert trissturi(2,4.2) == 4.2

def test_abi_dalas():
    assert trissturi(3.2,4.4)==7.04

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