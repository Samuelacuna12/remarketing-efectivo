"""Pruebas del contrafactual, costes y límites de entrada; stdlib únicamente."""
import math
import unittest
from calculadora_remarketing import DEMO, Grupo, calcular


class CalculadoraTest(unittest.TestCase):
    def test_ejemplo_normaliza_grupos_desiguales_y_resta_coste_una_vez(self):
        r = calcular(Grupo(**DEMO["tratamiento"]), Grupo(**DEMO["control"]), 2500)
        self.assertAlmostEqual(r["ingresos_incrementales_estimados"], 8000)
        self.assertAlmostEqual(r["compradores_incrementales_estimados"], 80)
        self.assertAlmostEqual(r["contribucion_incremental_antes_campana"], 3200)
        self.assertAlmostEqual(r["beneficio_incremental_estimado"], 700)
        self.assertAlmostEqual(r["beneficio_incremental_por_cliente_tratamiento"], .175)

    def test_misma_economia_por_cliente_no_significa_efecto_de_campana(self):
        t = Grupo(200, 20, 24, 2000, 1000, 200)
        c = Grupo(100, 10, 12, 1000, 500, 100)
        r = calcular(t, c, 90)
        self.assertEqual(r["ingresos_incrementales_estimados"], 0)
        self.assertEqual(r["beneficio_incremental_estimado"], -90)

    def test_mas_ingresos_puede_destruir_margen(self):
        t = Grupo(100, 20, 20, 1800, 1200, 500)
        c = Grupo(100, 10, 10, 1000, 400, 100)
        r = calcular(t, c, 100)
        self.assertEqual(r["ingresos_incrementales_estimados"], 800)
        self.assertEqual(r["beneficio_incremental_estimado"], -500)

    def test_control_sin_compras_y_coste_cero_no_inventa_ratios(self):
        r = calcular(Grupo(20, 1, 1, 100, 30, 10), Grupo(20, 0, 0, 0, 0, 0), 0)
        self.assertIsNone(r["lift_relativo_compra"])
        self.assertIsNone(r["ingreso_incremental_sobre_coste_campana"])
        lo, hi = r["intervalo_95_diferencia_tasa_compra"]
        self.assertLess(lo, .05)
        self.assertGreater(hi, .05)
        self.assertLess(lo, 0)  # una compra no demuestra un incremento.

    def test_intervalo_con_cero_eventos_tiene_incertidumbre(self):
        r = calcular(Grupo(10, 0, 0, 0, 0, 0), Grupo(10, 0, 0, 0, 0, 0), 0)
        lo, hi = r["intervalo_95_diferencia_tasa_compra"]
        self.assertLess(lo, 0)
        self.assertGreater(hi, 0)

    def test_datos_invalidos_son_rechazados(self):
        casos = [(0, 0, 0, 0, 0, 0), (10, 11, 11, 0, 0, 0),
                 (10, 1, 0, 0, 0, 0), (10, 0, 1, 0, 0, 0),
                 (True, 0, 0, 0, 0, 0), (10, 1.5, 2, 100, 30, 10),
                 (10, 1, 1, math.inf, 0, 0), (10, 1, 1, math.nan, 0, 0),
                 (10, 1, 1, -10, 0, 0)]
        for caso in casos:
            with self.subTest(caso=caso), self.assertRaises(ValueError):
                Grupo(*caso)
        for coste in [-1, math.inf, math.nan, True, "100"]:
            with self.subTest(coste=coste), self.assertRaises(ValueError):
                calcular(Grupo(10, 1, 1, 100, 30, 10), Grupo(10, 1, 1, 100, 30, 10), coste)


if __name__ == "__main__":
    unittest.main()
