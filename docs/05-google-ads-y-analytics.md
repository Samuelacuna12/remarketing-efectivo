# 05. Ejecutar remarketing con Google Ads y Analytics

[Volver al índice](../README.md) · [Meta Ads](04-meta-ads.md) · [Medición](08-medicion-experimentos-y-optimizacion.md)

> Fuentes oficiales consultadas el 11 de noviembre de 2026. El procedimiento describe decisiones y controles; las etiquetas exactas pueden variar por idioma y cuenta. No presupone disponibilidad universal de funciones.

## 1. Elige la función que corresponde a la necesidad

Hay diferencias entre recordar una marca a alguien que navega, aparecer cuando busca otra vez y aportar una señal a una campaña automatizada. Esas tres acciones pueden ayudar a vender, pero no representan el mismo experimento.

| Necesidad | Ruta posible | Verificación principal |
|---|---|---|
| Llegar a compradores conocidos | Lista propia mediante Customer Match si es elegible | Permisos, estado de lista y modo de segmentación |
| Activar por comportamiento registrado | Audiencia de Analytics o segmento de datos de Ads | Eventos correctos, vínculos y elegibilidad publicitaria |
| Aparecer cuando el cliente vuelve a buscar | Search con segmento de clientes | Targeting frente a Observation y búsquedas elegibles |
| Mostrar productos relevantes | Remarketing dinámico con feed adecuado | Concordancia de identificadores, inventario y destino |
| Ayudar a una campaña automatizada a encontrar valor | Señales de audiencia de Performance Max | La señal no restringe por sí sola el alcance a clientes |

Empieza por la hipótesis comercial. Si el problema es que un comprador no sabe qué recambio le corresponde, una guía de compatibilidad puede ser más útil que un anuncio genérico con descuento. Si vuelve por búsqueda orgánica sin necesidad de estímulo, una campaña puede capturar atribución sin añadir ventas.

## 2. Customer Match: activar datos propios con control

Customer Match permite construir segmentos a partir de datos propios para encontrar coincidencias en el ecosistema de Google. [La guía oficial](https://support.google.com/google-ads/answer/10550383) explica la función; la implementación comercial de este manual es una propuesta de trabajo, no una garantía de rendimiento.

### Paso 1. Comprueba acceso y políticas

La cuenta debe cumplir requisitos de historial de políticas y pagos. No asumas acceso por haber creado una cuenta o por tener un número elevado de correos. Revisa el estado efectivo y las funciones disponibles en la cuenta. La política también limita los datos y usos admitidos y exige los permisos aplicables. [Política de Customer Match](https://support.google.com/google-ads/answer/6299717).

Las listas no deben tratarse como archivos permanentes. Google indica una duración máxima de membresía de 540 días y una condición de actividad de al menos 100 miembros añadidos o actualizados dentro de ese periodo para mantener elegibilidad. Estos valores pertenecen a esta política y no son un mínimo universal de entrega para todos los formatos; confirma por separado el tamaño y estado utilizables en tu campaña. [Política de Customer Match](https://support.google.com/google-ads/answer/6299717).

### Paso 2. Diseña el segmento en origen

Crea reglas de negocio antes de exportar identificadores. Para un ejemplo de reposición:

```text
Cliente con compra válida y entregada de producto consumible
Sin reposición posterior registrada
Dentro de la ventana de necesidad definida para su cohorte
Elegible para activación publicitaria
Sin baja, reclamación pendiente ni devolución relevante
No asignado al control de esta intervención
```

Revisa cuánto cambia el segmento cada día. Una lista estática puede ser suficiente para una prueba corta con supresión frecuente; para un programa recurrente, diseña altas y bajas mantenidas por un proceso supervisado.

### Paso 3. Elige una vía de incorporación

La documentación recomienda Data Manager o Data Manager API para flujos nuevos. Si no necesitas una integración, evalúa una carga manual controlada. No desarrolles una conexión a medida solo porque existe una API: compara mantenimiento, borrado, trazabilidad y capacidad de recuperación. [Guía de Customer Match](https://support.google.com/google-ads/answer/10550383).

En una carga manual, usa el flujo oficial para archivo de clientes, descarga el esquema vigente, selecciona correctamente el tratamiento del archivo y conserva la confirmación. La interfaz distingue datos en texto y datos preprocesados; no improvises formatos ni apliques hash dos veces. [Crear una lista mediante archivo](https://support.google.com/google-ads/answer/10589050).

Revisa además la inclusión automática de listas Customer Match en Smart Bidding o segmentación optimizada. Google documenta una opción de cuenta para ese uso de listas no aplicadas. Desvincular una lista de una campaña no basta para auditar todos sus usos; comprueba esa configuración al diseñar finalidades y controles experimentales. [Guía de Customer Match](https://support.google.com/google-ads/answer/10550383).

### Paso 4. Registra la activación

El registro interno debería incluir nombre de lista, reglas, responsable, fecha, cantidad de registros autorizados enviados, resultado agregado del procesamiento, fecha de actualización siguiente y procedimiento de retiro. No almacenes los identificadores personales junto con el reporte que compartes públicamente.

El número de filas del CRM, el de coincidencias y el de personas alcanzables son conceptos distintos. Una carga correcta no implica que todas las personas puedan recibir anuncios ni que se vaya a consumir el presupuesto estimado. Utiliza el diagnóstico de la plataforma y evita identificar a los no coincidentes mediante inferencias individuales.

### Paso 5. Ensaya una baja

Con una identidad interna de prueba autorizada, valida el recorrido de supresión: cambio en el origen, actualización de audiencia y estado del proceso. Ten en cuenta que el procesamiento y la entrega pueden tener latencias. Si el conector falla, la operación debe enterarse y poder detener campañas dependientes; no basta con que el error quede en un registro que nadie revisa.

## 3. Analytics: de los eventos a una audiencia útil

### 3.1 Define el significado del evento

Antes de crear una audiencia, establece qué significa compra, devolución, entrega y servicio completado. Una página de agradecimiento que puede recargarse no es por sí sola una fuente económica fiable. La tienda o el sistema de facturación debe ser el lugar de reconciliación de pedidos y valores.

Construye un mapa de eventos con nombre, disparador, responsable y comprobación. Ejemplo de diseño propio:

| Evento interno | Cuándo ocurre | Campos útiles sin identidad directa |
|---|---|---|
| Pedido pagado | Confirmación del pago en origen | ID opaco de transacción, valor, moneda |
| Pedido entregado | Transportista o sistema confirma entrega | ID opaco, fecha, categoría |
| Devolución procesada | Abono validado | ID de transacción, valor devuelto |
| Reposición completada | Nueva compra de la categoría definida | Categoría, fecha, valor neto |
| Permiso retirado | Preferencia efectiva del cliente | Estado y sistema de origen, en entorno protegido |

Esta tabla no es un esquema de envío automático a Google. Determina qué eventos y parámetros admite cada destino y qué datos pueden compartirse antes de implementar. El registro de permisos debe gobernar la activación; no se publica como evento abierto con datos personales.

### 3.2 Crea una audiencia con criterios verificables

En GA4, el constructor de audiencias permite expresar condiciones sobre los datos disponibles. La documentación explica que las audiencias acumulan usuarios que cumplen los criterios desde su creación. No planifiques suponiendo que una audiencia nueva contendrá automáticamente todo el histórico que aparece en tus informes. [Crear y editar audiencias](https://support.google.com/analytics/answer/9267572).

Hay una excepción relevante para la activación: las listas correspondientes en Google Ads pueden prepopularse con hasta 30 días de datos disponibles. Distingue ese comportamiento del histórico de informes y verifica el tamaño activable. [Misma documentación oficial](https://support.google.com/analytics/answer/9267572).

Para activar las audiencias en Ads, comprueba vínculo con la cuenta correcta y las opciones de publicidad personalizada y recogida aplicables. La documentación de GA4 detalla la exportación de audiencias a cuentas vinculadas. [Audiencias y vínculos](https://support.google.com/analytics/answer/9267572).

Prueba la lógica con casos sintéticos:

1. Cliente que compró A ayer, aún sin entrega.
2. Cliente que recibió A y compró B.
3. Cliente que recibió A y no compró B.
4. Cliente que devolvió A.
5. Cliente que retiró su permiso.
6. Cliente del control.

Define qué debe pasar en cada caso y verifica que el origen y la activación coincidan. Si el constructor no puede expresar una regla clave con fiabilidad, prepara el segmento en el CRM y evalúa Customer Match en lugar de simular precisión con condiciones incompletas.

### 3.3 Diferencias de recuentos

No esperes que usuarios de GA4, clientes del CRM y personas alcanzables de Ads coincidan. Intervienen identificación, permisos, dispositivos, procesamiento, ventanas y requisitos de activación. Usa diferencias agregadas como diagnóstico; no “corrijas” permisos para forzar que los números cuadren.

Para un negocio que vende también en tienda física o por teléfono, la parte registrada en web puede ser solo una fracción. Evalúa el resultado comercial con el registro de todas las ventas que puedas asociar lícitamente a los grupos del experimento, no únicamente las compras posteriores a un clic.

## 4. Search: intención explícita y clientes existentes

Una persona que compró antes puede volver a buscar el mismo producto o uno complementario. Search puede cubrir esa necesidad, pero debes decidir si quieres observar cómo se comportan los clientes o restringir una prueba a ese segmento.

Google distingue **Targeting**, que restringe la elegibilidad según el criterio, de **Observation**, que permite analizar el segmento sin limitar el alcance. Añadir clientes en observación no convierte una campaña general en remarketing exclusivo. [Configuraciones oficiales](https://support.google.com/google-ads/answer/7365594).

### Procedimiento propuesto

1. Elige un segmento disponible que represente compradores pertinentes.
2. Decide si la pregunta exige restricción o solo análisis.
3. Comprueba que la configuración seleccionada sea compatible con ese tipo de campaña y lista.
4. Usa palabras relacionadas con la necesidad: recambio, repuesto, mantenimiento o categoría complementaria.
5. Revisa términos de búsqueda y negativos para evitar intenciones irrelevantes.
6. Envía a una página adecuada a la tarea: no siempre la página de inicio.
7. Mide venta válida y contribución, no solamente el clic.
8. Audita cambios de configuración después del lanzamiento.

No dupliques campañas de marca sin una razón de medición. Un cliente que busca tu nombre ya tiene intención y podría haber comprado por otro camino. Si pruebas Search adicional, el control debe reflejar con claridad qué publicidad se retira y qué actividad habitual continúa.

### Ejemplo de anuncio para servicio recurrente

```text
Titular: Revisa tu plan de mantenimiento
Descripción: Consulta disponibilidad, alcance del servicio y condiciones.
Destino: página de renovación con opciones y asistencia.
```

Evita titular con afirmaciones privadas como “Tu contrato está a punto de vencerse” si no corresponde a un contexto seguro y verificado. Un anuncio no es un canal privado autenticado. Usa el CRM para comunicaciones individualizadas cuando esté permitido y sea necesario.

## 5. Display y campañas con expansión

Las campañas visuales pueden recordar una propuesta fuera de una búsqueda explícita. Su alcance debe evaluarse con atención: la segmentación optimizada puede ir más allá de las señales seleccionadas. La ayuda oficial describe esta expansión y los controles disponibles. [Uso de segmentación optimizada](https://support.google.com/google-ads/answer/10538014).

Si necesitas una prueba limitada a clientes, verifica la configuración que permita ese alcance, incluyendo cualquier opción de expansión. No basta con seleccionar una lista si otras funciones amplían la entrega. Cuando no puedas imponer la población requerida, utiliza un diseño alternativo o informa la campaña como mixta.

Haz una revisión de ubicaciones, contenido y calidad de experiencia. Un clic barato desde un contexto inadecuado puede generar poco valor. El objetivo de la revisión no es eliminar por prejuicio todo inventario de bajo coste, sino comprobar si produce acciones comerciales válidas y si es adecuado para la marca.

La evaluación debe incluir:

- Alcance y presión publicitaria durante el periodo.
- Comportamiento en la página móvil y errores de carga.
- Ventas netas y devoluciones posteriores.
- Quejas o señales de confusión.
- Ubicaciones y configuraciones de seguridad de marca disponibles.
- Solapamiento con otras campañas de retención.

## 6. Remarketing dinámico: feed y eventos deben hablar el mismo idioma

Los anuncios dinámicos utilizan información de productos o servicios almacenada en un feed. Para comercio minorista, Google remite a Merchant Center; otros negocios tienen configuraciones específicas. [Guía de feeds dinámicos](https://support.google.com/google-ads/answer/6053288).

### Lista de comprobación del feed

| Campo o relación | Qué comprobar | Fallo frecuente |
|---|---|---|
| ID | Coincide entre evento, producto y variante | Evento usa padre y feed usa variante |
| Precio | Es vigente y con moneda correcta | Oferta antigua aún publicada |
| Stock | Refleja disponibilidad real | Se anuncia algo que no se puede entregar |
| URL | Abre el artículo y variante correctos | Redirección a inicio o producto distinto |
| Imagen | Describe exactamente lo vendido | Accesorios de la foto no incluidos |
| Territorio | Puede enviarse a la ubicación objetivo | Pedido cancelado por cobertura |
| Conjunto | Cumple la lógica comercial | Se recomiendan productos incompatibles |

La ejecución requiere conectar feed, eventos y configuración del formato compatible. Google mantiene un [procedimiento de configuración](https://support.google.com/google-ads/answer/6287125). Sigue la ruta que corresponda a tu negocio y valida el diagnóstico antes de activar inversión.

Para clientes existentes, cuidado con mostrar insistentemente el producto ya adquirido. En consumibles puede tener sentido; en bienes durables suele ser más útil enseñar uso, mantenimiento o complementos. El comportamiento pasado debe interpretarse con el conocimiento del producto.

### Prueba de extremo a extremo

Elige tres productos representativos y uno retirado. Recorre visita, compra, entrega y eventual devolución en un entorno de prueba o con pedidos controlados. Comprueba la información del feed y las reglas de exclusión. Documenta qué se actualiza al instante y qué depende de una sincronización periódica. No prometas al equipo comercial supresión inmediata si el sistema no puede cumplirla.

## 7. Performance Max: señales no son límites de remarketing

Google explica que las señales de audiencia de Performance Max son sugerencias y que la campaña puede llegar a otras personas. Por eso, cargar compradores como señal no demuestra que todo el gasto se destine a clientes existentes. [Preguntas oficiales sobre Performance Max](https://support.google.com/google-ads/answer/14587068).

Puede ser útil como parte de una estrategia de crecimiento, pero no etiquetes automáticamente sus resultados como retención. Para evaluarla:

1. Declara el objetivo global y las restricciones efectivas.
2. Mantén una definición de nuevo cliente y cliente existente en el sistema comercial.
3. Comprueba cualquier función de ciclo de vida disponible en la cuenta y sus requisitos actuales.
4. Registra cómo se usan las listas: señal, exclusión, identificación o ajuste de valor.
5. Revisa resultados por tipo de cliente usando datos verificables, sin confundir una etiqueta de plataforma con identidad perfecta.
6. Si quieres causalidad, diseña un experimento adecuado a la configuración; no deduzcas incrementalidad del nombre de la campaña.

No copies ajustes de adquisición de nuevos clientes dentro de una campaña cuyo propósito es volver a vender a clientes actuales sin comprobar sus efectos. Las funciones automatizadas deben servir al objetivo comercial definido, no sustituirlo.

## 8. Presupuesto, valor y conversiones

### Evita el objetivo equivocado

Si un formulario es solo un paso para una venta, mide calidad y cierre. Si tu integración registra una compra con valor bruto pero después hay muchos reembolsos, el rendimiento aparente puede mejorar mientras el negocio pierde contribución. Define el tratamiento de ajustes y evalúa datos maduros.

No mezcles moneda ni periodo. Un gasto en COP y un valor importado como USD pueden producir un indicador absurdo que parezca excelente. Verifica moneda del sistema, conversiones, feed y reportes. El detalle de moneda debe estar en el brief.

### Ejemplo ficticio

Una campaña gasta 400.000 COP y Ads atribuye 2.400.000 COP de ingresos. El ROAS atribuido es 6. Si la contribución de esos pedidos antes de medios es 720.000 COP, quedan 320.000 COP al restar gasto, pero aún no sabemos qué parte es adicional. Si sin la campaña habrían ocurrido 600.000 COP de esa contribución, el cambio neto sería 720.000 − 600.000 − 400.000 = −280.000 COP.

Esta cuenta ilustra por qué un buen ROAS no garantiza una buena inversión. El contrafactual debe estimarse con un diseño válido, no inventarse para justificar una conclusión. El capítulo de [medición](08-medicion-experimentos-y-optimizacion.md) desarrolla el procedimiento.

## 9. Operación, diagnóstico y cierre

### Antes de activar

Comprueba lista, permisos, modo de segmentación, expansión, exclusiones, presupuesto, destinos, eventos, feed y registro del experimento. Revisa en móvil y en el territorio de venta. Una persona debe firmar el lanzamiento en [la lista de verificación](../plantillas/checklist-lanzamiento.md).

### Durante la campaña

Separa fallos operativos de desempeño comercial. Un feed rechazado o pago roto requiere corrección inmediata. Una diferencia pequeña de tasa de compra con pocos clientes requiere paciencia y un análisis de incertidumbre. Evita cambiar reglas para favorecer retrospectivamente el resultado.

| Síntoma | Revisión prioritaria |
|---|---|
| Lista sin entrega | Estado, elegibilidad, tamaño activable y campaña compatible |
| Público mayor que la lista | Observation, expansión, señales y otras inclusiones |
| Productos erróneos | IDs, variantes, conjuntos y feed |
| Valor desproporcionado | Moneda, duplicados y configuración de conversiones |
| Alta atribución con poco crecimiento | Compras orgánicas, solapamiento y diseño de control |
| Clientes que ya compraron siguen activos | Latencia, origen de supresión y altas/bajas del conector |

### Al cerrar

Conserva configuración y definición de listas junto con el informe. Incluye fechas de maduración de devoluciones, gastos y cambios de campaña. Clasifica cada conclusión: observación de plataforma, resultado comercial o inferencia experimental. Una recomendación de presupuesto debe indicar cuánto riesgo asume y qué evidencia adicional la haría cambiar.

## 10. Entregable mínimo para que otra persona pueda operarlo

Una campaña bien documentada permite reemplazar al operador sin perder el criterio. Entrega: objetivo, reglas de población, modo de activación, fuentes, responsables, permisos, ventanas, exclusiones, oferta, anuncios, destinos, presupuesto, métricas, cambios y procedimiento de pausa. Añade un ejemplo de cliente ficticio que entra y otro que debe salir. Esa pequeña prueba suele detectar ambigüedades antes de que cuesten dinero.
