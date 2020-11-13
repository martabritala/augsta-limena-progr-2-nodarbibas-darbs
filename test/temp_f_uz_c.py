import pytest
from src.temperatura_FuzC import FtoC

def test_temperatura_viszemaka():
    assert FtoC(500)==-273.15
    
def test_temperatura_norm():
    assert FtoC(32)==0

"""
D. Temperatūras pārveidošana F->C

Funkcija akceptē vienu argumentu - temperatūru Fārenheita grādos,
un atgriež temperatūru Celsija grādos. Zemākā temperatūra
Celsija grādos var būt −273.15, tādēļ, ja aprēķinātā temperatūra ir zemāka, atgriež −273.15.

Argumenti:
    t {int vai float} -- temperatūra Fārenheita grādos
Atgriež:
    int vai float -- temperatūra Celsija grādos
"""
