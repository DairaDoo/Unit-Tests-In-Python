import pytest
from geometry import calcular_area_rectangulo

def test_calcular_que_base_y_altura_sean_numeros():
    with pytest.raises(TypeError, match="Base y altura deben ser números"):
        calcular_area_rectangulo("a", "n")

def test_probar_resultado_exitoso():
    resultado = calcular_area_rectangulo(base=5, altura=4)
    assert resultado == 20

def test_calcular_error_de_valores_negativos():
    with pytest.raises(ValueError, match="Base y altura no pueden ser negativos"):
        calcular_area_rectangulo(base=-5, altura=4)
