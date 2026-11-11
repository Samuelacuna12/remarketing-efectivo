# 2. Datos, segmentación y reglas de elegibilidad

> Las reglas numéricas de este capítulo son ejemplos de diseño. Sustitúyelas por tu distribución de compras, tus ciclos de consumo y las restricciones reales de tus canales. No publiques datos personales de clientes en un repositorio público.

## La audiencia empieza en una definición

Una lista de correos no es todavía un segmento útil. Un segmento necesita una condición comercial, un momento de entrada, una actualización, un conjunto de exclusiones y una decisión asociada. «Clientes interesantes» no permite operar. «Compradores con exactamente un pedido entregado de categoría café, sin devolución, con permiso vigente para email y sin un nuevo pedido desde la entrega» sí puede convertirse en una regla verificable.

Separa tres capas que suelen confundirse. La **población comercial** reúne a quienes tienen una necesidad probable. La **población contactable** filtra los permisos, datos válidos y restricciones de cada canal. La **audiencia alcanzable** depende además de coincidencias, actividad, políticas y posibilidades de entrega de la plataforma. No prometas alcanzar a 10.000 personas porque tu archivo tenga 10.000 filas.

## Un esquema mínimo de datos

| Entidad | Campos mínimos | Para qué sirve |
|---|---|---|
| Cliente | ID interno estable, fecha de alta, país, idioma, zona horaria si se conoce | Identidad y contexto básico |
| Preferencias | Canal, estado, fecha, fuente y finalidad del permiso; baja y fecha | Decidir si puede recibir la comunicación |
| Pedido | ID de pedido, cliente, fecha, estado, moneda, ingreso neto | Compras válidas y economía |
| Línea de pedido | Producto, variante, cantidad, categoría, importe y devolución | Compatibilidad y reposición |
| Entrega | Fecha real, incidencia, devolución, cancelación | Iniciar mensajes cuando existe producto recibido |
| Servicio | Caso abierto, severidad, resolución y responsable | Evitar vender sobre un problema pendiente |
| Contacto comercial | Campaña, canal, fecha, resultado y costo | Controlar presión y solapamientos |
| Cuenta B2B | ID de empresa, contrato, decisores autorizados, renovación y etapa | Coordinar a personas de la misma organización |
| Asignación experimental | ID del experimento, variante, fecha y unidad asignada | Mantener un control reproducible |

Si la fuente no ofrece un campo, documenta su ausencia y diseña una alternativa. Por ejemplo, cuando no existe confirmación de entrega, una espera conservadora desde el envío puede servir provisionalmente, siempre que no se describa al cliente como una entrega confirmada. Una automatización debe degradarse de forma segura cuando no conoce un dato.

### Un diccionario antes de integrar herramientas

Define qué cuenta como pedido válido. En un ecommerce podría ser un pedido pagado no cancelado, con sus devoluciones deducidas. En servicios podría ser un contrato activado y cobrado. Una cotización aprobada que todavía no inició no es idéntica a ingreso reconocido. La definición debe ser compartida entre ventas, operaciones y analítica.

Documenta también la fecha de referencia. Para frecuencia comercial puedes usar fecha del pedido; para educación poscompra suele ser más útil la entrega; para renovación importa el final del contrato. Usar la misma fecha para todos los trabajos crea recordatorios fuera de tiempo.

Elige una moneda de análisis y un método de conversión cuando existan varias monedas. Conserva la moneda original. Un cliente no debería cambiar de nivel VIP porque una tasa de cambio quedó mezclada con importes sin convertir. Identifica igualmente si los importes incluyen impuestos, envío o descuentos y evita sumar bases incompatibles.

## Limpieza de identidad sin suposiciones peligrosas

Empieza por un ID interno estable. Normaliza espacios y formatos de contacto según el uso permitido, pero conserva los datos originales con acceso restringido cuando sean necesarios para trazabilidad. Dos personas con el mismo apellido no son la misma persona. Un correo compartido por una familia o un departamento tampoco prueba que todas sus compras correspondan a un individuo.

En B2B, separa el nivel **cuenta** del nivel **contacto**. Una empresa puede tener cinco interlocutores; contactar a los cinco con la misma renovación puede generar confusión. Define un responsable de cuenta y una regla de coordinación. Si el cliente cambia de empresa, no arrastres automáticamente el contexto comercial de la organización anterior.

Una buena deduplicación permite explicar cada unión. Cuando la confianza no es suficiente, conserva registros separados o envía el caso a revisión. No compenses una mala identidad aumentando la cantidad de anuncios o mensajes.

## Un proceso de calidad semanal

1. Contar clientes totales, clientes con compra válida y contactables por canal.
2. Medir cuántos pedidos carecen de cliente, categoría o estado final.
3. Revisar duplicados de ID de pedido e importaciones repetidas.
4. Identificar compras con fechas futuras, importes negativos inesperados y monedas mezcladas.
5. Comprobar que devoluciones y cancelaciones actualizan segmentos.
6. Verificar que una baja llega a todos los destinos que deben respetarla.
7. Comparar una muestra de registros con la fuente transaccional.
8. Registrar fecha de última sincronización y responsable de cada problema.

Una caída de audiencia puede significar una baja de ventas, una nueva exclusión, un cambio de permiso o una integración rota. Antes de modificar el presupuesto, revisa cuál de esas causas está actuando. El tablero debe mostrar tanto rendimiento comercial como salud de datos.

## Segmentación por ciclo de vida

Usa una segmentación sencilla antes de multiplicar cruces. La siguiente tabla es una arquitectura inicial; las ventanas son ilustrativas y no constituyen una norma del mercado.

| Estado | Regla conceptual | Acción principal | Salida |
|---|---|---|---|
| Primera compra reciente | Un pedido válido y producto recién entregado | Ayudar a obtener valor | Hito de uso, segunda compra o cierre del período |
| Listo para segunda compra | Un pedido, experiencia satisfactoria y necesidad complementaria | Propuesta específica | Segundo pedido o agotamiento de secuencia |
| Reposición probable | Consumo esperado cerca del agotamiento | Facilitar recompra | Nuevo pedido de categoría o postergación |
| Recurrente activo | Varias compras dentro de su ritmo habitual | Continuidad y descubrimiento | Caída relevante de actividad |
| Alto valor activo | Contribución y relación sostenidas | Servicio, acceso y reconocimiento | Cambio real del patrón |
| En riesgo | Retraso frente al patrón propio o de categoría | Diagnosticar barrera | Compra, respuesta o clasificación de inactividad |
| Inactivo | Ausencia prolongada según el negocio | Reactivación limitada | Regreso o fin de intentos |
| Suprimido | Baja, restricción, incidencia u otra regla | No enviar promoción | Resolución legítima de la causa |

Mantén la supresión como una capa independiente. Un cliente puede ser VIP y tener una queja abierta. Ser VIP no elimina la necesidad de pausar promociones. Si los estados se almacenan en un único campo, una actualización comercial podría sobrescribir accidentalmente una exclusión importante.

## RFM: recencia, frecuencia y valor monetario

RFM resume cuánto tiempo pasó desde la última compra, cuántas compras hizo el cliente y cuánto gastó dentro de un alcance definido. Puede ayudar a ordenar prioridades, pero no identifica por sí solo necesidades, satisfacción o margen. Las implementaciones pueden usar escalas y reglas diferentes; consulta la configuración de tu herramienta antes de comparar puntuaciones. [Referencia oficial: análisis RFM de Shopify](https://help.shopify.com/en/manual/reports-and-analytics/shopify-reports/report-types/default-reports/customers-reports).

### Construir una versión propia transparente

1. Fija una fecha de corte, por ejemplo el último día del mes.
2. Elige una ventana, por ejemplo los 12 meses previos, y anota por qué representa tu negocio.
3. Cuenta solo compras válidas según tu diccionario.
4. Calcula R como días desde la última compra, F como número de pedidos y M como ingreso neto en la ventana.
5. Decide si usarás umbrales comerciales o grupos de distribución.
6. Asigna una puntuación alta a recencia más reciente, frecuencia mayor y monetario mayor.
7. Conserva los valores originales junto al puntaje y valida casos manualmente.

Un esquema ficticio podría usar R = 3 para hasta 30 días, R = 2 para 31–90 y R = 1 para más de 90; F = 3 para cuatro o más pedidos, F = 2 para dos o tres y F = 1 para uno; M = 3 para al menos 600 unidades, M = 2 para 200–599,99 y M = 1 para menos de 200. Esos cortes solo tendrían sentido si coinciden con el negocio y la moneda analizada.

| Cliente ficticio | Días desde compra | Pedidos | Ingreso neto | RFM | Interpretación para investigar |
|---|---:|---:|---:|---|---|
| C-001 | 12 | 5 | 720 | 333 | Recurrente valioso, conservar experiencia |
| C-002 | 15 | 1 | 240 | 312 | Nuevo con compra relevante, activar antes de vender más |
| C-003 | 120 | 5 | 680 | 133 | Históricamente valioso y ausente, investigar causa |
| C-004 | 70 | 2 | 170 | 221 | Repetidor moderado, revisar categoría y ritmo |

No sumes los tres dígitos y presupongas que todas las combinaciones con la misma suma requieren lo mismo. Un cliente reciente con un pedido costoso y otro antiguo con muchas compras pequeñas pueden sumar igual y necesitar acciones distintas. Mantén el contexto.

### Cuándo falla RFM

En productos duraderos, una recencia baja puede ser normal. Una compra anual no significa abandono al día 91. En negocios muy estacionales, compara contra la temporada equivalente. En empresas jóvenes, los clientes antiguos tienen más oportunidades de acumular frecuencia que los recién incorporados. En productos con devoluciones altas, gasto bruto puede premiar una contribución real baja.

Añade, cuando aporte valor, contribución, categoría, antigüedad de relación, uso, estado de servicio y permisos. No agregues veinte variables si nadie va a tomar una decisión distinta con ellas. Cada dato adicional debería mejorar una acción o evitar un error concreto.

## Segmentar por tiempo relativo, no solo por calendario

Dos clientes que compraron hace 45 días pueden estar en momentos distintos. Para quien repone cada 30 días existe un retraso; para quien suele comprar cada 120 todavía es pronto. Cuando hay suficiente historia por cliente, calcula su intervalo típico con medidas robustas y revisa variabilidad. Cuando no la hay, usa categoría y cantidad como aproximación.

```text
Índice de retraso = días desde última compra / intervalo esperado
```

Si el intervalo esperado es 40 días y han pasado 60, el índice es 1,5. No lo conviertas automáticamente en probabilidad de pérdida; es una señal operativa. Un retraso puede responder a vacaciones, cambio de consumo, stock acumulado o compra en otro canal de la misma empresa. Permite al cliente posponer un recordatorio y actualizar su preferencia.

Para reposición, considera cantidad comprada, frecuencia de uso declarada y plazos de entrega. Una estimación simple es unidades disponibles divididas entre uso esperado por día. Si no sabes si la persona ya abrió el producto, presenta el mensaje como una posibilidad: «Si estás cerca de terminarlo…», evitando afirmar un conocimiento que no tienes.

## Cohortes para comparar relaciones con la misma edad

Una cohorte agrupa clientes que comparten un evento inicial, como el mes de su primera compra. Luego se observa qué ocurre a edades comparables. No compares una cohorte que lleva un año acumulando pedidos con otra que solo tuvo dos semanas para hacerlo. Las herramientas de analítica permiten definir criterios de inclusión y retorno; verifica qué identidad y eventos utiliza cada informe. [Referencia oficial: exploración de cohortes en GA4](https://support.google.com/analytics/answer/9670133?hl=es).

Construye una tabla con filas por mes de primera compra y columnas por meses transcurridos. Elige si la celda expresa compra en ese mes, compra acumulada, ingreso o contribución por cliente original. Esas son preguntas diferentes. Una celda de 20 % de compra en el mes dos no significa que 20 % de los clientes haya hecho una segunda compra en total si algunos ya repitieron en el mes uno.

Compara cohortes también por primera categoría, canal de adquisición y oferta inicial. Un descuento de entrada puede generar un ticket inicial parecido y relaciones posteriores distintas. La interpretación correcta combina tamaño, madurez, margen y circunstancias del período; no atribuye cualquier diferencia a una campaña sin diseño causal.

## Exclusiones y prioridad entre campañas

Una lista de exclusiones debe consultarse al construir la audiencia **y otra vez al ejecutar cada envío**. Entre ambos momentos puede ocurrir una compra, una baja o una queja. No basta con exportar una lista el lunes y usarla sin cambios durante todo el mes.

| Situación | Acción sugerida |
|---|---|
| El cliente compró el producto objetivo | Salir del flujo de recompra y pasar a poscompra |
| Tiene devolución o reclamación relevante abierta | Pausar promociones y asignar servicio |
| Revocó un permiso | Aplicar la supresión del canal o finalidad correspondiente |
| Está en una prueba con control asignado | Respetar las reglas del experimento |
| Producto sin stock o incompatible | Retirar la oferta o proponer alternativa validada |
| Recibió otra comunicación comercial reciente | Aplicar prioridad y período de descanso definido |
| La información es incierta o antigua | Revisar elegibilidad; no completar con suposiciones |

Una prioridad inicial puede ser servicio urgente, comunicación contractual necesaria, activación, reposición solicitada y finalmente promoción general. Esta es una regla de operación propuesta; el negocio debe decidir cómo clasifica sus comunicaciones y qué requisitos aplican. No disfraces publicidad de servicio para saltarte una preferencia.

## La ficha que debe tener cada segmento

```text
Nombre: reposicion_cafe_1kg_v1
Propósito: facilitar la reposición de café de la categoría elegida
Población: clientes con compra entregada válida de ese producto
Fecha de referencia: entrega real; alternativa documentada si falta
Entrada: proximidad al intervalo estimado de consumo
Canales: solo los autorizados y técnicamente disponibles
Exclusiones: compra posterior, incidencia, baja, control, stock insuficiente
Actualización: según latencia documentada de las fuentes
Salida: compra, postergación, baja, fin de secuencia o pérdida de elegibilidad
Responsable: CRM; validación de producto por operaciones
Métrica: contribución y recompra por cliente asignado
Versión y fecha: conservar para poder reconstruir el experimento
```

Antes de activarlo, prueba registros ficticios que deban entrar y registros que deban quedar fuera. Incluye una baja justo antes del envío, una compra en otro canal, una devolución parcial y dos eventos duplicados. La mejor segmentación es la que puede explicarse y detenerse cuando el contexto cambia.

Continúa con [las estrategias y sus reglas de ejecución](03-estrategias-del-ciclo-de-vida.md).
