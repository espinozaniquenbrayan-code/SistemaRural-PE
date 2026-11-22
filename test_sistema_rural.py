import builtins
import importlib
import sys

import pytest


@pytest.fixture
def sr(monkeypatch):
    """Importa sistema_rural con listas vacías (el menú se cierra con la opción 0)."""
    monkeypatch.setattr(builtins, "input", lambda _="": "0")
    sys.modules.pop("sistema_rural", None)
    modulo = importlib.import_module("sistema_rural")
    return modulo


def escribir(monkeypatch, *respuestas):
    datos = iter(respuestas)
    monkeypatch.setattr(builtins, "input", lambda _="": next(datos))


def test_cp01_dni_de_8_digitos_aceptado(sr, monkeypatch):
    escribir(monkeypatch, "Ana Prueba", "12345678")
    sr.registrar_paciente()
    assert ["Ana Prueba", "12345678"] in sr.pacientes


def test_cp02_dni_con_letras_rechazado(sr, monkeypatch):
    escribir(monkeypatch, "Ana Prueba", "12345ABC")
    sr.registrar_paciente()
    assert ["Ana Prueba", "12345ABC"] not in sr.pacientes


def test_cp03_fecha_valida_aceptada(sr, monkeypatch):
    sr.pacientes.append(["Ana Prueba", "12345678"])
    escribir(monkeypatch, "12345678", "25/11/2026", "09:00")
    sr.registrar_cita()
    assert ["12345678", "25/11/2026", "09:00"] in sr.citas


def test_cp04_stock_de_3_genera_alerta(sr, monkeypatch, capsys):
    escribir(monkeypatch, "Paracetamol", "3")
    sr.controlar_medicamentos()
    assert "ALERTA" in capsys.readouterr().out


def test_cp05_stock_de_10_no_genera_alerta(sr, monkeypatch, capsys):
    escribir(monkeypatch, "Amoxicilina", "10")
    sr.controlar_medicamentos()
    assert "ALERTA" not in capsys.readouterr().out
