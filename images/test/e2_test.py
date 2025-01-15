


import pytest
import sys
from pathlib import Path

# Agregar el directorio src al path
src_path = str(Path(__file__).parent.parent.parent / 'src')
sys.path.append(src_path)

from main_e2 import agregar_producto, calcular_total, buscar_producto, aplicar_descuento, mostrar_inventario, inventario

# Fixture para limpiar el inventario antes de cada test
@pytest.fixture(autouse=True)
def limpiar_inventario():
    inventario.clear()
    yield

def test_agregar_producto():
    agregar_producto("Laptop", 1000, 5)
    assert len(inventario) == 1
    assert inventario[0]["nombre"] == "Laptop"
    assert inventario[0]["precio"] == 1000
    assert inventario[0]["cantidad"] == 5  # Verifica que se guarde la cantidad

def test_no_permite_duplicados():
    agregar_producto("Mouse", 50, 10)
    agregar_producto("Mouse", 60, 5)
    assert len(inventario) == 1
    assert inventario[0]["precio"] == 50  # Mantiene el primer precio

def test_calcular_total():
    agregar_producto("Laptop", 1000, 1)
    agregar_producto("Mouse", 50, 2)
    total = calcular_total()
    assert total == 1050

def test_buscar_producto_existente():
    agregar_producto("Teclado", 100, 3)
    producto = buscar_producto("Teclado")
    assert producto is not None
    assert producto["nombre"] == "Teclado"

def test_buscar_producto_inexistente():
    producto = buscar_producto("NoExiste")
    assert producto is None

def test_aplicar_descuento_existente():
    agregar_producto("Monitor", 800, 2)
    aplicar_descuento("Monitor", 0.1)  # 10% descuento
    producto = buscar_producto("Monitor")
    assert producto["precio"] == 720  # 800 - (800 * 0.1)

def test_aplicar_descuento_inexistente():
    with pytest.raises(Exception):  # Debería manejar el caso de producto no encontrado
        aplicar_descuento("NoExiste", 0.1)

def test_precio_no_puede_ser_cero():
    with pytest.raises(ValueError):
        agregar_producto("Mouse", 0, 1)

def test_mostrar_inventario(capsys):
    agregar_producto("Laptop", 1000, 1)
    mostrar_inventario()
    captured = capsys.readouterr()
    assert "Laptop" in captured.out
    assert "1000" in captured.out

def test_cantidad_debe_ser_positiva():
    with pytest.raises(ValueError):
        agregar_producto("Laptop", 1000, -1)

def test_calcular_total_inventario_vacio():
    total = calcular_total()
    assert total == 0

def test_aplicar_descuento_porcentaje_valido():
    with pytest.raises(ValueError):
        agregar_producto("Monitor", 800, 2)
        aplicar_descuento("Monitor", 1.5)  # Más del 100% de descuento

def test_tipo_datos_correctos():
    with pytest.raises(TypeError):
        agregar_producto(123, "1000", "5")  # Tipos incorrectos

def test_manejo_productos_multiples():
    productos = [
        ("Laptop", 1000, 5),
        ("Mouse", 50, 10),
        ("Teclado", 100, 3)
    ]
    for nombre, precio, cantidad in productos:
        agregar_producto(nombre, precio, cantidad)
    
    assert len(inventario) == 3
    total = calcular_total()
    assert total == 1150