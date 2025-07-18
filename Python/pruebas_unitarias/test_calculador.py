#Las pruebas unitarias son un conjunto de pruebas que se realizan para verificar la calidad de un codigo

#Pytest es una herramienta para realizar pruebas unitarias en python

#nuestros de test deben de ajuro, porque si, siempre comenzar con test_ o terminar con _test
from calculador import sum,rest,multiply,divide
import pytest


@pytest.mark.parametrize("num1,num2,expected_result",
[(1,1,2),   #test case 1
(-2,-3,-5), #test case 2
(3,0,3), #test case 3
(4,4,8), #test case 4
(-15,5,-10), #test case 5
])

#test para las funciones de calculator

def test_sum(num1,num2,expected_result):
  assert sum(num1,num2) == expected_result


@pytest.mark.parametrize("num1,num2,expected_result", [
    (1, 1, 0),
    (-2, -3, 1),
    (3, 0, 3),
    (4, 4, 0),
    (-15, 5, -20),
])

def test_rest(num1,num2,expected_result):
  assert rest(num1,num2) == expected_result

@pytest.mark.parametrize("num1,num2,expected_result", [
    (1, 1, 1),
    (-2, -3, 6),
    (3, 0, 0),
    (4, 4, 16),
    (-15, 5, -75),
])
#pruebas parametrizadas para la multiplicacion
def test_multiply(num1,num2,expected_result):
  assert multiply(num1,num2) == expected_result

@pytest.mark.parametrize("num1,num2,expected_result", [
    (4, 2, 2),
    (9, 3, 3),
    (-15, 5, -3),
])
def test_divide(num1,num2,expected_result):
  with pytest.raises(ValueError):
    assert divide(num1,num2) == expected_result


