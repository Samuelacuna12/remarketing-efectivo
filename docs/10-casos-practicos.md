# 10. Casos prácticos completos y decisiones con números

> Todos los negocios, clientes, importes, tamaños de audiencia y resultados de este capítulo son ficticios. Las unidades monetarias se escriben como UM para evitar mezclar monedas. Los ejemplos muestran cómo razonar y ejecutar; no son benchmarks, predicciones ni promesas de rendimiento.

## Caso 1: reposición en una tienda de café

### Situación y diagnóstico

Una tienda vende bolsas de un kilogramo y tiene 8.000 clientes históricos. El equipo observa que parte de los compradores vuelve entre 25 y 50 días, pero muchos reciben únicamente promociones generales. Las entregas están registradas y el catálogo permite repetir un pedido. La tienda quiere probar si un recordatorio útil genera contribución adicional, conservando una experiencia cómoda.

La base histórica no equivale a audiencia elegible. Después de revisar producto, entrega, permisos y compra posterior, existen 2.000 clientes adecuados para la prueba. Quedan fuera quienes compraron para regalo cuando ese dato fue declarado, quienes ya repusieron, quienes tienen una suscripción activa que cubrirá la necesidad, quienes solicitaron baja y quienes tienen una incidencia abierta.

El equipo no sabe exactamente cuánto café consume cada persona. Por eso la propuesta se presenta como una posibilidad y permite posponer el recordatorio. La hipótesis de momento se basa en la distribución interna de intervalos de compra, no en una regla universal.

### Diseño operativo

| Elemento | Decisión ficticia |
|---|---|
| Objetivo | Aumentar contribución por cliente elegible a 45 días |
| Audiencia | Compradores de 1 kg próximos al intervalo estimado |
| Unidad experimental | Cliente interno deduplicado |
| Asignación | 1.600 tratamiento y 400 control aleatorio |
| Intervención | Un recordatorio autorizado con recompra y postergación |
| Incentivo | Sin descuento en esta primera prueba |
| Exclusión durante prueba | Compra posterior, baja, incidencia o stock insuficiente |
| Responsable | CRM con validación de operaciones |
| Cierre | 45 días desde asignación y ajuste de devoluciones |

El mensaje dice: «Si estás cerca de terminar tu café, puedes repetir el pedido o ajustar la cantidad aquí. También puedes posponer el próximo recordatorio». La página muestra producto, molienda, cantidad, precio y entrega. No se fuerza al cliente a volver a buscar la variante correcta.

### Resultado y cálculo

Durante la ventana, 192 clientes del tratamiento y 32 del control compran al menos una vez. Para simplificar el ejemplo, cada comprador hace un único pedido comparable. Las tasas son 192 / 1.600 = 12 % y 32 / 400 = 8 %. El incremento observado es cuatro puntos porcentuales. Los compradores adicionales estimados en el tratamiento son 1.600 × 0,04 = 64.

Cada pedido deja 22 UM de contribución antes de esta campaña. Los costos de campaña son 500 UM entre producción, mensajería y operación incremental. Entonces:

```text
Contribución incremental estimada = 64 × 22 = 1.408 UM
Contribución incremental tras campaña = 1.408 − 500 = 908 UM
```

Los 192 pedidos tratados generan 4.224 UM de contribución antes de campaña, pero esa cifra completa no es incremento. Parte habría ocurrido igualmente. El control ayuda a estimar esa parte, sujeto a incertidumbre y a que no exista contaminación relevante.

### Decisión y siguiente prueba

El resultado sugiere una oportunidad, pero la tienda debe revisar intervalos de incertidumbre y la compra acumulada más allá de la ventana. Si el recordatorio simplemente adelantó un pedido que habría sucedido al día 50, el efecto de largo plazo será menor. La siguiente prueba podría comparar dos momentos de envío, manteniendo el mismo mensaje y una observación suficiente.

No se añade descuento automáticamente. Primero se estudia si facilitar la recompra ya cumple el objetivo. También se revisan las respuestas «todavía tengo» para mejorar periodicidad. El éxito operativo incluye aprender a no contactar a quien no necesita reponer.

## Caso 2: venta cruzada después de comprar un producto duradero

### Situación y diagnóstico

Una tienda vende escritorios y accesorios. Los clientes rara vez necesitan otro escritorio en pocos meses, de modo que una campaña genérica de «vuelve a comprar» resulta poco pertinente. Sin embargo, algunos accesorios compatibles pueden mejorar el uso del espacio.

El equipo de producto valida una matriz por modelo y tamaño. Se descartan recomendaciones que requieran perforaciones no previstas o accesorios ya incluidos. El equipo de servicio pide pausar promociones a entregas con daños o montaje pendiente. La primera comunicación después de entregar se concentra en instalación y cuidado; la propuesta comercial aparece cuando esa experiencia está resuelta.

### Ejecución

1. Obtener compras entregadas del modelo compatible.
2. Excluir accesorios ya comprados, devoluciones e incidencias.
3. Comprobar inventario y costo total del accesorio.
4. Preparar una demostración de uso en el modelo adquirido.
5. Ofrecer una selección pequeña con una explicación de compatibilidad.
6. Mantener un grupo comparable para evaluar contribución.
7. Medir devoluciones y satisfacción del complemento, además de compra.

La propuesta evita afirmar que el cliente tiene un problema. Dice: «Si quieres liberar espacio en la superficie, este soporte es compatible con el modelo que compraste. Puedes ver las medidas y cómo se instala aquí». La página muestra restricciones y herramientas necesarias.

### Economía del incentivo

El accesorio cuesta 80 UM de lista. Sus costos variables son 30 de producto, 6 de preparación y entrega subsidiada, y 4 de pago y otros costos. Sin descuento deja 40 UM. Con un descuento de 10 UM y los mismos costos simplificados, deja 30 UM.

En una comparación ficticia, dos grupos de 1.000 clientes generan estos resultados:

| Variante | Compradores | Ingreso por pedido | Contribución por pedido | Contribución total antes de campaña |
|---|---:|---:|---:|---:|
| Demostración sin descuento | 50 | 80 | 40 | 2.000 |
| Demostración con 10 UM de descuento | 60 | 70 | 30 | 1.800 |

El descuento aumenta compradores de 5 % a 6 %, pero reduce la contribución observada de 2 a 1,8 UM por cliente asignado, antes de costos de campaña. El grupo con descuento vende diez unidades más y aporta 200 UM menos. La decisión no debería basarse solo en conversión.

### Qué falta para concluir

La comparación necesita asignación adecuada y suficiente precisión. También podría haber un efecto en compras futuras, costos de servicio o devolución. Si no hay evidencia de esos beneficios, no deben inventarse para justificar el descuento. El equipo conserva la variante sin descuento como candidata y prueba una demostración más clara o un paquete cuyo costo permita mejorar valor sin erosionar contribución.

Este caso muestra por qué la venta cruzada debe basarse en la vida útil del producto. La ausencia de recompra del escritorio no constituye abandono; el objetivo razonable es satisfacción, recomendación y complementos pertinentes.

## Caso 3: renovación y expansión en una empresa de servicios B2B

### Situación y diagnóstico

Una empresa implementa sistemas comerciales y ofrece soporte mensual. Tiene 40 cuentas con contratos de alcance variable. Cinco cuentas representan una parte relevante del ingreso. Su problema no es alcanzar grandes audiencias; es llegar a tiempo con evidencia, al interlocutor adecuado y una propuesta que el equipo pueda cumplir.

El CRM contiene contactos duplicados y fechas de renovación incompletas. Antes de automatizar, el responsable comercial valida cada cuenta, contrato, fecha, persona que decide y persona que usa el servicio. No se dispara una secuencia hasta confirmar ese contexto. El seguimiento se organiza por cuenta para que distintos vendedores no contacten en paralelo a la misma empresa.

### Proceso de renovación

Como hipótesis operativa, la empresa inicia la preparación 90 días antes del vencimiento; en compras complejas podría necesitar más tiempo. El responsable de cuenta revisa objetivos originales, entregables, uso, incidencias y evidencia de valor. Alrededor de 60 días antes propone una revisión con los interlocutores adecuados. Posteriormente presenta alcance, condiciones y próximo paso según el calendario real de compra.

Estos días son un ejemplo, no un requisito de plataforma ni una norma contractual. El contrato y el proceso de compras del cliente determinan los avisos necesarios. Si el cliente necesita aprobación presupuestaria en otra fecha, la planificación se adapta.

La revisión no se limita a «hicimos 25 reuniones». Distingue actividades de resultados: qué proceso se implementó, qué usa el equipo, qué problema sigue pendiente y qué indicadores pueden vincularse de manera defendible al trabajo. Si hubo crecimiento de ventas, no se atribuye completo al proveedor sin evidencia.

### Renovar antes de ampliar

Una cuenta paga 2.000 UM mensuales y requiere 1.200 UM de costo directo mensual de prestación. Deja 800 UM antes de gastos generales. Se ofrece una ampliación a 2.800 UM que elevaría el costo directo a 1.600 UM. Si el alcance se cumple con esos costos, la contribución sube de 800 a 1.200 UM: 400 UM adicionales por mes.

La propuesta incluye 250 UM de costo inicial de incorporación. Si la ampliación permanece seis meses, la contribución adicional antes de otros costos sería:

```text
(2.800 − 1.600 − 800) × 6 − 250 = 2.150 UM
```

La fórmula resta los 800 UM que ya se obtenían con el plan anterior. Contar toda la nueva facturación como ganancia de expansión exageraría el efecto. Si el costo directo esperado aumenta por personal adicional, se vuelve a calcular. No se vende una ampliación que operaciones no puede prestar.

### Métricas y responsabilidad

Se registran cuentas elegibles, renovadas, perdidas, ingreso renovado, contribución retenida, expansión y causa de decisión. El responsable de cuenta tiene un siguiente paso por oportunidad; operaciones valida el alcance; finanzas revisa margen y cobranza. Una campaña publicitaria puede mantener presencia de marca cuando sea apropiado, pero la renovación depende de este trabajo concreto.

En una base de 40 cuentas, puede ser difícil obtener conclusiones estadísticas rápidas. La empresa combina seguimiento longitudinal, revisión de casos y mejora del proceso. No compara sin más el porcentaje de renovación de un trimestre con el anterior si la mezcla de cuentas es distinta.

## Caso 4: reactivación de clientes inactivos sin regalar margen

### Situación y diagnóstico

Una tienda de materiales de oficina define inactividad según la última compra y el ciclo de cada tipo de cliente. No usa el mismo corte para un comprador ocasional y para una pequeña empresa que habitualmente repone cada mes. De 12.000 registros históricos, solo 3.000 cumplen necesidad probable, datos válidos, permisos y ausencia de una incidencia abierta.

Las entrevistas de servicio señalan dos barreras frecuentes: dudas sobre disponibilidad y dificultad para repetir una lista larga de productos. La primera prueba ofrece una lista reutilizable y disponibilidad actualizada, sin descuento. Una segunda variante añade un incentivo. El control no recibe esta acción adicional; las comunicaciones necesarias y el servicio continúan de forma consistente según el diseño del experimento.

### Comparar contribución por asignado

Tres grupos aleatorios de 1.000 clientes generan resultados ficticios. Cada comprador hace un único pedido y los importes ya reflejan devoluciones. Para simplificar, los costos variables de producto y servicio por pedido son iguales entre grupos, salvo el descuento reflejado en contribución.

| Grupo | Compradores | Contribución por pedido | Costo de campaña | Contribución total tras campaña |
|---|---:|---:|---:|---:|
| Control | 40 | 35 | 0 | 1.400 |
| Lista fácil sin incentivo | 65 | 35 | 250 | 2.025 |
| Lista fácil con incentivo | 80 | 25 | 300 | 1.700 |

La mejora observada de contribución frente al control es 625 UM para la lista sin incentivo y 300 UM para la variante con incentivo. Por cliente asignado son 0,625 y 0,30 UM. La variante con descuento reactiva más compradores, pero el costo del incentivo afecta también a quienes habrían comprado sin él.

No sería correcto calcular 40 compradores adicionales × 35 y restar solo medios para la variante incentivada: su contribución por pedido ya cambió a 25. La comparación de contribución total entre grupos conserva ese efecto.

### Continuidad y decisión

El equipo observa la continuidad de los reactivados durante un horizonte pertinente y calcula contribución acumulada por cliente originalmente asignado. Si la variante con incentivo trae clientes que regresan después sin descuentos, podría cambiar la decisión, pero debe medirse. No se presume una fidelización futura para justificar una pérdida presente.

La siguiente acción es mejorar la lista reutilizable, preguntar de manera opcional por la periodicidad y cerrar la secuencia a quienes no muestran interés. Quienes responden que ya no necesitan el servicio salen de esa propuesta; quienes tienen un problema pasan a atención.

## Caso 5: suscripción con retención de ingresos y adopción

### Situación y diagnóstico

Una herramienta B2B tiene 100 cuentas activas al comenzar el mes, con 20.000 UM de ingreso recurrente mensual. El equipo quiere reducir cancelación y ampliar cuentas con una necesidad real. Primero separa señales de salud, contrato y uso: una cuenta puede pagar y estar poco activa, o utilizar mucho el servicio y necesitar ayuda para incorporar usuarios.

El programa tiene dos rutas: una intervención de éxito para cuentas que no alcanzaron un hito de valor y una conversación de ampliación para las que se aproximan a un límite útil. No se manda automáticamente una oferta de plan superior a quienes apenas utilizan lo contratado.

### Un ejemplo de GRR y NRR

Al final del mes, la cohorte de cuentas iniciales pierde 1.000 UM por cancelación y 500 por reducción; gana 2.000 por ampliaciones. Nuevos clientes aportan además 3.000 UM, que se excluyen de estas métricas de retención de la base inicial.

```text
GRR de ingresos = (20.000 − 1.000 − 500) / 20.000 = 92,5 %

NRR de ingresos = (20.000 − 1.000 − 500 + 2.000) / 20.000 = 102,5 %
```

La retención bruta de ingresos muestra las pérdidas sin expansión; la neta incorpora expansión de la misma base. Una NRR superior al 100 % no significa que no haya cancelaciones: aquí la expansión las supera en ingreso. Tampoco significa rentabilidad, pues no incluye costos de prestación ni adquisición. Documenta el tratamiento de cambios de moneda, pausas, reactivaciones y componentes no recurrentes.

### Ejecución y aprendizaje

Cada ruta tiene un dueño y una salida. Si una cuenta completa el hito, deja de recibir ayuda repetida. Si inicia una negociación de ampliación, el contacto queda coordinado con su responsable. Si reporta un problema, se pausa la promoción correspondiente.

El tablero combina cuentas retenidas, ingresos retenidos, contribución, uso de funciones y motivos de cancelación. Las aperturas de los mensajes de ayuda sirven para diagnosticar entrega, pero no prueban adopción. El siguiente experimento compara una intervención centrada en un obstáculo concreto con la orientación habitual, evitando privar a un grupo del soporte que le corresponde.

## Plantilla para crear tu propio caso

Antes de copiar una estrategia, completa estos campos con hechos de tu negocio:

1. **Situación:** qué comportamiento se observa y qué evidencia lo respalda.
2. **Necesidad del cliente:** qué problema se pretende resolver.
3. **Población:** quién entra, quién queda fuera y por qué.
4. **Momento:** qué evento inicia la acción y qué latencia tienen los datos.
5. **Propuesta:** beneficio, condiciones, disponibilidad y costo total.
6. **Economía:** contribución por pedido, costo del incentivo y costo de operación.
7. **Comparación:** cómo se distinguirá una mejora real de compras que ya iban a ocurrir.
8. **Ejecución:** canales, secuencia, responsables, salida y manejo de respuestas.
9. **Decisión:** condiciones para detener, corregir, mantener o ampliar.
10. **Seguimiento:** qué horizonte permitirá ver devoluciones, repetición y desplazamiento de compras.

Una campaña que no puede completar estos campos todavía es una idea. Completarla no exige un gran presupuesto: exige claridad sobre la relación, la contribución y el aprendizaje que se busca.
