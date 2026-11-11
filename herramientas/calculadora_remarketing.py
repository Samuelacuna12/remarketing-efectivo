#!/usr/bin/env python3
"""Calculadora educativa de un holdout aleatorizado con datos agregados.

Sin dependencias externas. No identifica clientes, no carga audiencias, no envía
mensajes y no demuestra causalidad si el diseño de origen no es válido.
Ingresos netos: después de descuentos y devoluciones; sin impuestos recaudados.
Los costes de producto/variables NO deben incluir el coste de campaña, que se
resta una sola vez mediante coste_incremental_campana.
"""

import argparse
from dataclasses import dataclass
import json
import math
from pathlib import Path


@dataclass(frozen=True)
class Grupo:
    clientes: int
    compradores: int
    pedidos: int
    ingresos_netos: float
    coste_producto: float
    otros_costes_variables: float

    def __post_init__(self):
        for nombre in ("clientes", "compradores", "pedidos"):
            valor = getattr(self, nombre)
            if isinstance(valor, bool) or not isinstance(valor, int):
                raise ValueError(f"{nombre} debe ser un entero")
        if self.clientes <= 0:
            raise ValueError("clientes debe ser mayor que cero")
        if not 0 <= self.compradores <= self.clientes:
            raise ValueError("compradores debe estar entre cero y clientes")
        if self.pedidos < self.compradores:
            raise ValueError("pedidos debe ser al menos compradores")
        if self.compradores == 0 and self.pedidos != 0:
            raise ValueError("no puede haber pedidos sin compradores")
        for nombre in ("ingresos_netos", "coste_producto", "otros_costes_variables"):
            valor = getattr(self, nombre)
            if isinstance(valor, bool) or not isinstance(valor, (int, float)):
                raise ValueError(f"{nombre} debe ser un número")
            if not math.isfinite(valor) or valor < 0:
                raise ValueError(f"{nombre} debe ser finito y no negativo")

    @property
    def contribucion(self):
        return self.ingresos_netos - self.coste_producto - self.otros_costes_variables


def wilson(exitos, total, z=1.959963984540054):
    """Intervalo Wilson 95 % para una proporción binomial independiente."""
    p = exitos / total
    denominador = 1 + z * z / total
    centro = (p + z * z / (2 * total)) / denominador
    radio = z * math.sqrt(p * (1 - p) / total + z * z / (4 * total * total)) / denominador
    return max(0.0, centro - radio), min(1.0, centro + radio)


def calcular(tratamiento, control, coste_incremental_campana):
    """Compara tasas y escala el contrafactual al tamaño de tratamiento.

    El intervalo Newcombe sobre Wilson se limita al resultado binario compra.
    No es un intervalo para ingresos, contribución ni beneficio; esos agregados
    no proporcionan varianza a nivel de cliente. No usar para datos agrupados,
    asignación no aleatoria o consultas repetidas buscando significación.
    """
    coste = coste_incremental_campana
    if isinstance(coste, bool) or not isinstance(coste, (int, float)):
        raise ValueError("coste_incremental_campana debe ser un número")
    if not math.isfinite(coste) or coste < 0:
        raise ValueError("coste_incremental_campana debe ser finito y no negativo")
    factor = tratamiento.clientes / control.clientes
    p_t = tratamiento.compradores / tratamiento.clientes
    p_c = control.compradores / control.clientes
    diferencia = p_t - p_c
    l_t, u_t = wilson(tratamiento.compradores, tratamiento.clientes)
    l_c, u_c = wilson(control.compradores, control.clientes)
    limite_inferior = diferencia - math.sqrt((p_t - l_t)**2 + (u_c - p_c)**2)
    limite_superior = diferencia + math.sqrt((u_t - p_t)**2 + (p_c - l_c)**2)
    ingresos_incrementales = tratamiento.ingresos_netos - factor * control.ingresos_netos
    contribucion_incremental = tratamiento.contribucion - factor * control.contribucion
    beneficio = contribucion_incremental - coste
    return {
        "factor_normalizacion_control": factor,
        "tasa_compra_tratamiento": p_t,
        "tasa_compra_control": p_c,
        "diferencia_tasa_compra": diferencia,
        "intervalo_95_diferencia_tasa_compra": [max(-1.0, limite_inferior), min(1.0, limite_superior)],
        "lift_relativo_compra": diferencia / p_c if p_c > 0 else None,
        "compradores_incrementales_estimados": diferencia * tratamiento.clientes,
        "pedidos_incrementales_estimados": tratamiento.pedidos - factor * control.pedidos,
        "ingresos_incrementales_estimados": ingresos_incrementales,
        "contribucion_incremental_antes_campana": contribucion_incremental,
        "coste_incremental_campana": coste,
        "beneficio_incremental_estimado": beneficio,
        "beneficio_incremental_por_cliente_tratamiento": beneficio / tratamiento.clientes,
        "ingreso_incremental_sobre_coste_campana": ingresos_incrementales / coste if coste > 0 else None,
        "contribucion_incremental_sobre_coste_campana": contribucion_incremental / coste if coste > 0 else None,
        "aviso": "Estimaciones educativas. El intervalo solo describe compra binaria bajo independencia y asignación aleatoria. No estima incertidumbre del beneficio. Verificar contaminación, madurez de devoluciones y diseño antes de decidir.",
    }


DEMO = {
    "tratamiento": {"clientes": 4000, "compradores": 360, "pedidos": 360,
                    "ingresos_netos": 36000, "coste_producto": 14400,
                    "otros_costes_variables": 6000},
    "control": {"clientes": 1000, "compradores": 70, "pedidos": 70,
                "ingresos_netos": 7000, "coste_producto": 2800,
                "otros_costes_variables": 1100},
    "coste_incremental_campana": 2500,
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, help="JSON agregado con tratamiento, control y coste_incremental_campana. Sin esta opción se usa un ejemplo ficticio.")
    args = parser.parse_args()
    try:
        datos = json.loads(args.input.read_text(encoding="utf-8")) if args.input else DEMO
        if set(datos) != {"tratamiento", "control", "coste_incremental_campana"}:
            raise ValueError("el JSON debe contener exactamente tratamiento, control y coste_incremental_campana")
        resultado = calcular(Grupo(**datos["tratamiento"]), Grupo(**datos["control"]), datos["coste_incremental_campana"])
    except (OSError, ValueError, TypeError, KeyError) as error:
        parser.error(str(error))
    print(json.dumps({"ejemplo_ficticio": args.input is None, "resultados": resultado}, ensure_ascii=False, indent=2, allow_nan=False))


if __name__ == "__main__":
    main()
