# 08. Medición, experimentos y optimización

La pregunta de negocio es cuánto beneficio adicional produce volver a contactar a los clientes. El panel de anuncios responde otra pregunta: cuántas compras se atribuyeron a anuncios bajo sus reglas. Necesitas ambas lecturas para operar, pero cumplen funciones distintas.

Este capítulo propone un método de trabajo. Los importes, porcentajes y duraciones de sus ejemplos son ficticios; no son referencias de rendimiento del sector. Las decisiones reales dependen del ciclo de compra, el margen, la muestra disponible y la calidad de los datos.

## 1. Define una pregunta que pueda fallar

Una hipótesis útil describe población, intervención, comparación, plazo y criterio de éxito:

> En clientes de una categoría de reposición cuyo consumo estimado está próximo a terminar, una secuencia de recordatorio sin descuento aumentará la contribución por cliente elegible a 45 días frente a la comunicación habitual, después de costes de entrega y devoluciones, sin superar nuestro límite de bajas.

Antes de publicar, completa una ficha con estos campos:

| Campo | Decisión que debe quedar escrita |
|---|---|
| Población | Compradores de la categoría, fecha de compra, país y permisos necesarios |
| Exclusiones | Bajas, pedidos abiertos relevantes, reclamaciones, falta de stock, datos incompletos |
| Unidad | Cliente; cuenta empresarial si varias personas comparten la compra |
| Intervención | Canales, mensajes, oferta, número máximo de contactos |
| Comparación | Actividad habitual sin la intervención que se evalúa |
| Principal | Contribución incremental neta por cliente asignado |
| Secundarias | Compra, tiempo a segunda compra, importe, pedidos, visitas útiles |
| Salvaguardas | Bajas, quejas, devoluciones, saturación y capacidad operativa |
| Observación | Mismo tiempo de seguimiento por persona; plazo adicional para devoluciones |
| Decisión | Cuándo escalar, revisar o declarar resultado inconcluso |

Elige una métrica principal antes de mirar los resultados. Si luego eliges la que más creció entre veinte, el informe describe una búsqueda oportunista. Las exploraciones sirven para proponer el siguiente experimento, no para reescribir el anterior.

## 2. Construye una escalera de métricas

**Integridad de datos.** Eventos recibidos, pedidos conciliados, clientes con identidad resuelta, retraso de sincronización, permisos actualizados y exclusiones aplicadas. Si desaparece la mitad de compras por un error de integración, no hay una campaña que optimizar todavía.

**Entrega y alcance.** Envíos aceptados, entregas, clientes alcanzados, frecuencia y gasto. Un envío aceptado por el proveedor no garantiza lectura. Un cliente que no ve el anuncio sigue perteneciendo al grupo al que fue asignado.

**Respuesta.** Clics, respuestas útiles, sesiones con intención y solicitudes de ayuda. Úsalas para diagnosticar obstáculos. Evita equiparar una apertura de correo con atención real: mide acciones posteriores y observa cómo cambia el indicador según cliente de correo y medición disponible.

**Resultado comercial.** Compradores, pedidos, ingreso neto, segunda compra, renovación, cancelación y contribución. Cuenta pedidos válidos, distingue cancelados y conserva ajustes por devolución.

**Resultado incremental.** Diferencia frente al contrafactual, costes adicionales de la intervención y efectos posteriores. Este nivel decide si conviene invertir más.

Documenta cada indicador con numerador, denominador, moneda, zona horaria, fuente y fecha de cierre. «Conversión del 9 %» no significa mucho sin saber si se divide entre clics, clientes elegibles, mensajes entregados o sesiones.

## 3. Separa atribución de causalidad

ROAS atribuido = ingresos que la plataforma atribuye / gasto publicitario.

Es una señal útil para detectar cambios de entrega, comparar el comportamiento del panel y reconciliar campañas con reglas constantes. No descuenta automáticamente compras que habrían ocurrido sin anuncios, coste del producto, costes operativos ni promociones. Dos plataformas pueden reclamar la misma compra bajo sus respectivas ventanas; no sumes sus ingresos atribuidos como si fueran ventas diferentes.

En clientes existentes hay un problema adicional: los mejores compradores ya tenían alta probabilidad de volver. Mostrarles un anuncio puede producir un ROAS aparente alto y un incremento pequeño. Excluirlos indiscriminadamente también puede ser un error si hay una venta complementaria pertinente. Hace falta medir el efecto de la intervención concreta.

Mantén tres tablas distintas: pedidos reales conciliados; atribuciones reportadas por cada plataforma; asignaciones y resultados del experimento. Vincúlalas para investigar, pero conserva las definiciones originales. Si el control compra por búsqueda orgánica, esa compra forma parte de la comparación.

## 4. Diseña un grupo de control que conserve su significado

Un holdout es un conjunto de personas elegibles que no recibe la intervención evaluada. No significa abandonar la atención al cliente, impedir compras o suspender información necesaria sobre un pedido.

1. Congela las reglas de elegibilidad y calcula la población antes de la campaña.
2. Resuelve identidades duplicadas. Dos correos del mismo cliente no deben terminar en grupos distintos.
3. Asigna aleatoriamente con una herramienta que permita reproducir la asignación. Conserva versión de reglas, semilla o procedimiento y fecha.
4. Si la categoría, la recencia o el país afectan mucho a la compra, aleatoriza dentro de estratos definidos de antemano. No crees tantos estratos que cada uno quede vacío.
5. Guarda la asignación en una tabla privada con permisos limitados. No publiques identificadores en GitHub.
6. Aplica exclusiones de la intervención en todos los canales que correspondan.
7. Verifica con una muestra de prueba que el control efectivamente queda fuera.
8. Sigue a todos los asignados durante el mismo horizonte y concilia resultados con el sistema de pedidos.

No existe un reparto universal 90/10 u 80/20. Un control pequeño reduce el coste de oportunidad aparente, pero también reduce precisión. Estima el tamaño requerido con la tasa base, el efecto mínimo que cambiaría tu decisión y el diseño. Si no puedes reunir una muestra suficiente, usa el piloto para aprender sobre operación y mensajes; declara incierto el efecto económico.

La asignación debe permanecer estable durante el experimento. No muevas al control a tratamiento porque mostró interés. No elimines del análisis a quien recibió el mensaje y luego se dio de baja: ese efecto forma parte del resultado de tu política de contacto. Cumple la baja inmediatamente para las comunicaciones siguientes.

### Qué significa «comunicación habitual»

Si el tratamiento añade anuncios a un flujo de email ya existente, ambos grupos conservan el mismo email habitual y solo cambia la posibilidad de recibir esos anuncios. Si evalúas una secuencia combinada de email y WhatsApp, el control debe quedar excluido de esa secuencia completa. Escribe exactamente qué actividad continúa en cada grupo.

No mezcles resultados de estas dos preguntas:

- ¿Qué aporta añadir un canal a nuestro sistema actual?
- ¿Qué aporta todo nuestro sistema de remarketing frente a mantener solo la atención y comunicaciones indispensables?

Ambas son válidas y necesitan controles distintos.

## 5. Analiza por intención de tratar

La comparación principal incluye a todos los clientes asignados originalmente a cada grupo, recibieran o no el contacto. Es el principio de intención de tratar: mide el efecto de activar la política en una población elegible, con sus fallos reales de entrega y coincidencia publicitaria.

Comparar «quienes abrieron» con «quienes no abrieron» rompe la aleatorización. Quien abre puede tener más interés previo. Comparar clientes alcanzados con no alcanzados también puede introducir selección: la subasta y el uso de la plataforma influyen en el alcance.

Sí puedes publicar entrega, coincidencia y alcance como diagnósticos secundarios. Si un canal apenas entrega, el resultado por asignado informa de que esa implementación todavía aporta poco. Arregla el problema y realiza otra prueba; no conviertas retrospectivamente la muestra en una que sí recibió anuncios.

En B2B, varias personas pueden pertenecer a la misma cuenta y compartir la decisión. Considera aleatorizar por empresa, no por contacto. Entonces la precisión y el tamaño de muestra deben calcularse respetando esa agrupación; los intervalos para personas independientes no se aplican automáticamente.

## 6. Controla la contaminación entre canales

Una persona excluida de una lista puede seguir viendo anuncios de otra campaña. Un cupón puede compartirse con el control. Un vendedor puede contactar manualmente a clientes reservados al experimento. Estos casos reducen la diferencia efectiva entre grupos y cambian la interpretación.

Mantén un mapa de campañas y responsables. Define una exclusión global para la intervención evaluada, revisa automatizaciones y registra excepciones. Si una persona del control inicia una conversación de soporte, atiéndela; registra el hecho si altera la exposición y conserva su grupo original.

Si evalúas solo anuncios de una plataforma, otras campañas pueden continuar iguales en ambos grupos. Entonces el resultado es el efecto adicional bajo ese entorno, no el efecto aislado de toda la publicidad. Si además cambias precios, disponibilidad, vendedores o plazos de entrega, anota las fechas y limita la conclusión.

No uses un antes/después simple como prueba causal. Puede ayudar a observar estacionalidad y tendencias, pero las compras también cambian por calendario, promociones generales, competidores y composición de clientes. Cuando no puedas aleatorizar, describe el diseño alternativo y sus supuestos; solicita apoyo analítico para comparaciones geográficas o controles sintéticos.

## 7. Calcula contribución, no solo facturación

Para cada grupo y ventana, calcula:

```text
Ingreso neto = venta antes de descuentos
              - descuentos
              - devoluciones y reembolsos
              - impuestos recaudados para terceros, si estaban incluidos

Contribución antes de campaña = ingreso neto
                              - coste del producto o servicio entregado
                              - otros costes variables pertinentes

Otros costes variables: comisiones de pago, preparación, envío subsidiado,
coste variable de atención, devolución y otros costes definidos por Finanzas.
```

Decide con Finanzas cómo tratar producto recuperable, portes cobrados, reembolsos parciales, coste de prestación y pasivos de puntos o bonos. Aplica el mismo criterio a ambos grupos. No restes un descuento otra vez si el ingreso ya viene neto. No restes medios en la contribución y luego otra vez al calcular beneficio.

Cuando los grupos tienen distinto tamaño:

```text
Contribución por cliente T = contribución T / clientes asignados T
Contribución por cliente C = contribución C / clientes asignados C

Contribución incremental estimada del grupo T
    = (contribución por cliente T - contribución por cliente C) × clientes T

Beneficio incremental estimado
    = contribución incremental estimada - coste adicional de campaña
```

El coste adicional puede incluir medios, envíos de mensajes, producción adicional, horas extra de operación o costes fijos necesarios para la decisión. Define el alcance antes de comparar alternativas. El coste habitual que existe en ambos grupos no se resta de nuevo salvo que sea pertinente a la decisión y esté calculado de manera consistente.

## 8. Ejemplo completo: las ventas suben, el margen decide

Ejemplo ficticio en unidades monetarias de una misma moneda. Se asignaron 4.000 clientes a tratamiento y 1.000 a control, con idéntico seguimiento. Los ingresos ya excluyen descuentos, devoluciones e impuestos; los costes de campaña todavía no están restados.

| Variable | Tratamiento | Control |
|---|---:|---:|
| Clientes asignados | 4.000 | 1.000 |
| Compradores | 360 | 70 |
| Pedidos | 360 | 70 |
| Ingresos netos | 36.000 | 7.000 |
| Coste de producto | 14.400 | 2.800 |
| Otros costes variables | 6.000 | 1.100 |
| Contribución antes de campaña | 15.600 | 3.100 |

La tasa de compra es 9 % frente a 7 %. La diferencia es **2 puntos porcentuales**, equivalente a un lift relativo de aproximadamente **28,6 %**. No confundas estas unidades.

Normaliza el control multiplicando por cuatro: para una población de 4.000 clientes esperaríamos 280 compradores, 28.000 de ingreso y 12.400 de contribución si se comportara como el control. La estimación es de 80 compradores adicionales, 8.000 de ingreso incremental y 3.200 de contribución incremental antes del coste de campaña.

Si medios cuestan 2.200 y mensajes adicionales 300, el coste incremental total es 2.500. Quedan **700 de beneficio incremental estimado**, o 0,175 por cliente tratado. Ingreso incremental / coste total = 3,2; contribución incremental / coste total = 1,28. Estos ratios no son el ROAS atribuido de una plataforma. Si se calcula iROAS con medios solamente, sería 8.000 / 2.200 ≈ 3,64; declara siempre el denominador.

El punto estimado positivo todavía no demuestra rentabilidad con precisión suficiente. Hay que revisar dispersión por cliente, devoluciones pendientes y estabilidad de la asignación. Una diferencia de pocas compras grandes puede explicar gran parte del margen.

### Ejemplo de una promoción destructiva

Supón 100 clientes por grupo. Tratamiento vende 1.800, tiene coste de producto de 1.200 y otros costes de 500: su contribución es 100. Control vende 1.000 con costes 400 y 100: contribución 500. El tratamiento factura 800 más, pero aporta 400 menos antes de pagar la campaña. Si contactar cuesta 100, el efecto estimado es -500. Un incremento de ventas no rescata una oferta cuyo margen se deteriora tanto.

## 9. Trata la incertidumbre como parte del resultado

La incertidumbre no desaparece porque el panel muestre decimales. Para compra sí/no puedes estimar un intervalo de diferencia de proporciones si hay asignación aleatoria e independencia apropiadas. Para contribución necesitas información de la variabilidad a nivel de cliente, incluidos quienes compraron cero, o un resumen estadístico suficiente preparado correctamente.

La calculadora de este repositorio muestra un intervalo orientativo de compra mediante Wilson y diferencia Newcombe. No calcula incertidumbre financiera con agregados que no contienen varianza. No sirve sin ajustes para aleatorización por empresas, tiendas u otros grupos.

Antes del lanzamiento, fija efecto mínimo económicamente relevante, tamaño de muestra, horizonte y regla de parada. No pares cuando aparezca por primera vez un resultado favorable si el diseño no contempla análisis secuencial. Revisar la salud de la entrega es distinto de buscar repetidamente una conclusión estadística.

Con muestra pequeña, un resultado razonable es: «La operación funcionó, el intervalo sigue admitiendo pérdidas y ganancias relevantes, necesitamos más observación o una prueba mejor dimensionada». Un resultado no concluyente no prueba ausencia de efecto. Tampoco autoriza escalar sin límite.

## 10. Mide cohortes, recompra y efectos tardíos

Una cohorte agrupa clientes por un evento de entrada: primera compra en un mes, compra de una categoría o inicio de contrato. Compara cohortes con la misma edad. Una cohorte creada hace 90 días tuvo más oportunidad de recomprar que otra creada ayer.

Para segunda compra, define qué pedidos cuentan, cómo tratas compras del mismo día, cancelaciones y clientes aún sin tiempo completo de seguimiento. Publica por ejemplo «segunda compra a 60 días entre clientes con 60 días de observación». Para tiempo hasta recompra con seguimiento desigual, utiliza métodos adecuados de supervivencia con apoyo analítico.

En suscripción distingue cancelación solicitada, fin de servicio, impago y recuperación de pago. En servicios distingue reserva, asistencia, factura y cobro. En B2B separa reunión, oportunidad aceptada, contrato e ingreso realizado. Ninguno sustituye automáticamente al siguiente.

Un recordatorio puede adelantar una compra que ocurriría después. Revisa una ventana posterior para detectar ese desplazamiento. Una oferta puede elevar devoluciones o enseñar a esperar descuentos. Incluye seguimiento suficiente para captar esos efectos, sin atribuir a la campaña todo el valor futuro observado.

## 11. Usa un tablero semanal que termine en decisiones

| Lectura | Pregunta | Acción posible |
|---|---|---|
| Datos | ¿Pedidos y permisos están conciliados? | Pausar interpretación y corregir integración |
| Entrega | ¿El público recibe la intervención prevista? | Revisar coincidencia, rechazos y exclusiones |
| Mensaje | ¿Se comprende la propuesta y el siguiente paso? | Revisar respuestas, pruebas de usabilidad y claridad |
| Negocio | ¿Aumenta contribución neta, con costes maduros? | Mantener prueba, revisar oferta o reducir coste |
| Cliente | ¿Aumentan bajas, quejas o problemas? | Reducir presión y corregir motivo concreto |
| Experimento | ¿La asignación sigue íntegra? | Investigar contaminación y documentar alcance |

No optimices cambiando público, oferta, creatividad y calendario a la vez si quieres aprender qué causó la mejora. Prioriza una pregunta y cambia el componente necesario. Si ocurre una incidencia material, registra su fecha, corrige el servicio y decide si el experimento debe reiniciarse como una versión nueva.

## 12. Uso de la calculadora y plantillas

Desde la raíz del repositorio, con Python 3:

```bash
python3 herramientas/calculadora_remarketing.py
python3 -m unittest discover -s herramientas -p 'test_*.py' -v
```

El primer comando usa únicamente el ejemplo ficticio anterior y devuelve JSON. Para un análisis propio, crea fuera de este repositorio público un JSON con las claves `tratamiento`, `control` y `coste_incremental_campana`. Cada grupo requiere `clientes`, `compradores`, `pedidos`, `ingresos_netos`, `coste_producto` y `otros_costes_variables`. Después:

```bash
python3 herramientas/calculadora_remarketing.py --input /ruta/privada/resumen_agregado.json
```

Usa enteros para clientes, compradores y pedidos; una sola moneda para importes. La herramienta valida cantidades y divisiones por cero, pero no puede validar por ti la aleatorización, la veracidad de costes ni los permisos. Los casos con ajustes contables que producen ingresos agregados negativos requieren una conciliación aparte y no se aceptan en esta calculadora educativa.

Complementa el análisis con [KPIs semanales](../plantillas/kpis-semanales.csv), [matriz de priorización](../plantillas/matriz-priorizacion.csv) y el registro de experimentos del repositorio. Conservar una decisión argumentada vale más que almacenar cientos de capturas sin definición de métricas.

## 13. Qué debe decir el informe final

Incluye pregunta, asignación, tamaño inicial de grupos, seguimiento, intervención, costes incluidos, incidencias, resultado principal, incertidumbre, salvaguardas y decisión. Distingue análisis previsto de exploraciones posteriores. Publica limitaciones en la misma página que el resultado.

Una conclusión útil sería: «En esta población elegible y con esta implementación, el punto estimado de beneficio fue positivo. La incertidumbre financiera sigue siendo elevada y hubo baja coincidencia de anuncios; mantendremos el presupuesto del piloto y repetiremos con asignación estable y mejor conciliación». Otra puede ser: «La contribución cayó por descuentos; retiramos esa oferta y probaremos recordatorio de utilidad». Ambas permiten actuar sin convertir una observación parcial en una promesa general.
