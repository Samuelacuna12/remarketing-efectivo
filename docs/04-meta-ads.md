# 04. Ejecutar remarketing de clientes en Meta Ads

[Volver al índice](../README.md) · [Datos y segmentación](02-datos-y-segmentacion.md) · [Medición](08-medicion-experimentos-y-optimizacion.md)

> Manual operativo y recomendaciones de diseño. Revisión editorial: 11 de noviembre de 2026. Los nombres, controles y opciones cambian según la cuenta, el objetivo y el país. No se ha auditado ninguna cuenta publicitaria real para este repositorio. Los enlaces oficiales de Meta que exigen iniciar sesión se indican en [Fuentes](../FUENTES.md); sus pantallas actuales deben comprobarse antes del lanzamiento.

## 1. Define qué trabajo le vas a pedir a la publicidad

Meta puede ayudar a recordar una necesidad, explicar un producto complementario y presentar una razón para volver. No corrige una entrega incumplida, una política de cambios confusa ni la ausencia de una oferta relevante. Antes de abrir el administrador, escribe una hipótesis comercial concreta:

> Entre clientes que recibieron un equipo compatible y todavía no compraron su accesorio, una demostración de uso puede aumentar la contribución por cliente durante los próximos 30 días frente a no añadir esta campaña.

Esta frase identifica población, acción, resultado y comparación. Es mejor punto de partida que “hacer remarketing a todos los compradores”. El segundo enfoque mezcla clientes que necesitan ayuda, clientes que ya recompraron y clientes cuya necesidad no se repetirá durante meses.

Trabaja con cuatro piezas documentadas:

| Pieza | Pregunta | Ejemplo ficticio |
|---|---|---|
| Segmento | ¿Quién puede recibir la campaña? | Compradores de equipo A, pedido entregado, sin accesorio B |
| Mensaje | ¿Qué problema pendiente resuelve? | Cómo usar B con A y qué compatibilidad comprobar |
| Resultado | ¿Qué acción valiosa cuenta? | Compra confirmada de B con margen positivo |
| Salida | ¿Cuándo deja de ser pertinente? | Compra B, devolución de A, baja o fin de ventana |

No clasifiques como clientes a todos los visitantes del sitio o seguidores de Instagram. Esas señales permiten otros tipos de retargeting, pero no prueban una compra. Tampoco llames “retención” a una audiencia similar creada a partir de compradores: su propósito es descubrir personas nuevas.

## 2. Qué necesitas tener preparado

### 2.1 Activos y accesos

Identifica quién administra el negocio, la cuenta publicitaria, la página, la cuenta de Instagram, los datos de eventos y el catálogo si corresponde. Da al equipo acceso por funciones y evita compartir contraseñas. Establece un responsable del presupuesto y otro de comprobar pedidos y márgenes; una sola persona puede ejercer ambos roles, pero las tareas deben quedar claras.

No es necesario crear un negocio, instalar todas las herramientas ni rehacer una tienda para probar una hipótesis. Primero comprueba lo que ya existe. La proliferación de píxeles, integraciones y catálogos duplicados provoca datos inconsistentes y trabajo de mantenimiento.

### 2.2 Evidencia comercial

Reúne antes del lanzamiento:

- Definición exacta de cliente, compra válida y pedido entregado.
- Productos y variantes elegibles, compatibilidad, stock y precios.
- Margen de contribución esperado después de cualquier incentivo.
- Canales y finalidades para los que se dispone de autorización o fundamento válido.
- Audiencias de inclusión y de supresión, con responsable y fecha de actualización.
- Destino móvil funcional y eventos de prueba.
- Duración del experimento, pérdida máxima asumible y regla de pausa.

Una lista que contiene datos de clientes no es automáticamente una lista utilizable para publicidad. La revisión de permisos es independiente de que esos contactos puedan recibir un aviso de entrega o una respuesta de soporte.

## 3. Construye una audiencia que represente clientes

### 3.1 Fuente CRM o tienda

Para programas de recompra y venta cruzada, la información de pedidos suele ser más útil que una ventana general de visitas. En tu sistema de origen, crea un segmento con reglas comprensibles. Por ejemplo:

```text
compró categoría A
Y pedido entregado
Y producto no devuelto
Y no compró categoría B
Y autorización o fundamento válido para esta activación
Y no pertenece a supresión vigente
Y no pertenece al control del experimento
```

Después genera la audiencia mediante la función de lista de clientes disponible en tu cuenta. Usa la plantilla que Meta ofrezca en ese momento y sigue sus instrucciones de formato y tratamiento de identificadores. No copies una exportación del CRM con notas, direcciones completas, documentos, tickets de soporte o información sensible. Exporta únicamente los campos necesarios y autorizados para la coincidencia.

**No subas el CSV real a este repositorio.** Las plantillas incluidas aquí son registros de planificación, no listas personales listas para cargar en una plataforma.

Define la actualización como un proceso con altas y bajas. Añadir a los nuevos compradores sin retirar devoluciones, revocaciones y compradores del complemento deja el segmento desactualizado. Si usas un conector, comprueba cómo maneja reemplazos y eliminaciones; “sincronización activa” no demuestra que las bajas se estén propagando.

### 3.2 Señales del sitio y eventos de compra

Una audiencia creada con una señal de compra puede servir como apoyo o punto de partida, sujeto a disponibilidad y políticas de la cuenta. Sin embargo, un evento técnico no explica siempre si el pedido fue entregado, cancelado o devuelto. Para decisiones de ciclo de vida, reconcilia los eventos con el sistema de pedidos.

Decide qué representa cada señal:

| Señal | Lo que permite inferir | Lo que no prueba |
|---|---|---|
| Visita a producto | Interés en esa página | Compra ni satisfacción |
| Inicio de pago | Intención más avanzada | Pago aprobado |
| Evento de compra | Acción registrada según integración | Entrega y margen final |
| Pedido entregado en CRM | Cumplimiento de la entrega registrada | Permiso para cualquier canal |
| Compra neta tras devoluciones | Resultado económico más sólido | Causalidad de la campaña |

Si una compra se envía desde navegador y servidor, comprueba que la integración la trate como una sola acción. Haz una compra de prueba, revisa identificadores y diagnósticos disponibles, y compara con el pedido de origen. No instales dos integraciones de seguimiento completas sobre la misma tienda sin saber qué emite cada una. La referencia oficial de deduplicación está en [Meta for Developers](https://developers.facebook.com/documentation/ads-commerce/conversions-api/deduplicate-pixel-and-server-events); el acceso automatizado estuvo limitado durante esta revisión, por lo que deben comprobarse allí los parámetros y requisitos vigentes antes de implementar.

### 3.3 Catálogo para complementar, no repetir sin criterio

Un catálogo ayuda a mantener productos e información comercial conectados. Antes de usar anuncios basados en productos:

1. Verifica que el identificador de producto del evento corresponde al identificador del catálogo.
2. Comprueba cada variante, disponibilidad, imagen, precio, moneda y destino.
3. Crea conjuntos coherentes con la estrategia: compatibles, reposición o categoría complementaria.
4. Excluye productos agotados, de margen insuficiente o que no se pueden enviar al territorio elegido.
5. Comprueba manualmente varias combinaciones de producto base y complemento.
6. Define qué pasa cuando un producto se retira o cambia de variante.

No des por hecho que un anuncio de catálogo interpreta tu lógica de compatibilidad. Si el sistema no permite expresar una restricción importante, utiliza una selección controlada de productos o una página de recomendación con validación. Vender un accesorio incompatible puede incrementar ingresos hoy y devoluciones mañana.

## 4. Comprueba el alcance efectivo de la campaña

Este es uno de los controles más importantes de todo el proceso. Según configuración, una audiencia puede funcionar como límite o como sugerencia para la entrega. No presupongas que escribir el nombre de una lista en un campo garantiza alcance exclusivamente dentro de esa lista.

Antes de publicar, un responsable debe leer las aclaraciones visibles del administrador y responder:

- ¿La lista de clientes es una inclusión obligatoria o una sugerencia?
- ¿Existe ampliación automática y puede controlarse en esta combinación de objetivo y campaña?
- ¿Las exclusiones relevantes son controles efectivos o la pantalla muestra limitaciones?
- ¿Qué otros criterios pueden ampliar o reducir la población?
- ¿Qué información posterior permitirá saber a quién se entregó el anuncio, sin esperar datos individuales que la plataforma no expone?

Guarda en un registro interno la configuración, fecha y explicación de la interfaz. Si el alcance no puede restringirse como exige el experimento, cambia el diseño o denomina el resultado como campaña mixta. No la presentes como prueba pura de retención. Consulta en la cuenta la ayuda oficial sobre [controles y sugerencias de audiencia](https://www.facebook.com/business/help/938372127764391); esta página requirió acceso durante la revisión, por lo que aquí no se afirma que un interruptor concreto exista en todas las cuentas.

La misma precaución aplica a los grupos de control. Si un cliente del control puede entrar por otra campaña amplia, la comparación deja de medir la ausencia de publicidad de manera limpia. Documenta la exposición que no puedes controlar y define qué decisión todavía puede sostener el estudio.

## 5. Estructura inicial: suficientemente simple para aprender

No abras diez conjuntos de anuncios para una base pequeña. Cada subdivisión necesita entrega, revisión y contenido propio. La fragmentación puede convertir un presupuesto razonable en muchos experimentos sin información.

Una estructura de prueba podría ser:

```text
Programa: retención de clientes
└── Campaña: venta cruzada categoría A → B
    ├── Segmento elegible: clientes entregados sin B
    ├── Exclusiones: supresión + compradores de B + control
    ├── Creatividad 1: demostración de uso
    └── Creatividad 2: respuesta a objeción de compatibilidad
```

La asignación de impresiones entre anuncios puede ser desigual. Poner dos anuncios en un conjunto no equivale por sí mismo a un A/B aleatorizado. Para responder una pregunta causal sobre creatividad, utiliza una metodología experimental adecuada y revisa sus condiciones. Para explorar mensajes, puedes empezar con entrega normal, etiquetando el aprendizaje como orientativo.

Separa campañas cuando exista una razón para controlar de forma independiente presupuesto, oferta, población o experimento. Agrupa cuando el comportamiento y el destino sean equivalentes y la separación no cambie decisiones. No conviertas cada puntuación RFM en una campaña si no tienes un mensaje distinto para ella.

### Convención de nombres

Usa etiquetas descriptivas que no revelen datos personales:

```text
RMK_CLIENTES_CROSSSELL_A-B_CO_2026Q4_V1
AUD_A_ENTREGADO_SIN_B_REGLA_V1
AD_DEMO_COMPATIBILIDAD_VIDEO_V1
```

Documenta el significado en un diccionario. Evita nombres con diagnósticos, datos financieros personales o identificadores de clientes. Un nombre de campaña puede terminar en reportes, enlaces y capturas compartidas.

## 6. Selecciona resultado y presupuesto

Optimiza hacia una acción cercana al valor comercial que puedes medir con suficiente fiabilidad. Si el negocio cierra por conversación, no confundas conversación iniciada con compra: define el traspaso al vendedor y registra después venta, cobro, cancelación y margen en el CRM. Si el cierre ocurre en la tienda, revisa que el evento y el valor representen la operación correcta.

No elijas tráfico únicamente para abaratar el clic y después evalúes la campaña como si hubiera sido optimizada para ventas. El clic puede ser útil para validar un destino o estudiar interés, pero no sustituye el resultado económico.

### Ejemplo ilustrativo de presupuesto, no recomendación universal

Supón una audiencia alcanzable de 4.000 personas, una hipótesis de 3 impresiones por persona durante el periodo y un CPM supuesto de 18.000 COP:

```text
Impresiones orientativas = 4.000 × 3 = 12.000
Gasto orientativo = 12.000 / 1.000 × 18.000 = 216.000 COP
```

El tamaño alcanzable y el CPM no son conocidos de antemano con precisión. La subasta no garantiza esa cobertura ni esa frecuencia. Esta cuenta sirve para detectar órdenes de magnitud: si planeas gastar 3 millones sobre una base muy pequeña, revisa antes si terminarás insistiendo demasiado.

Luego compara el gasto con la contribución incremental que necesitarías recuperar. Si cada pedido adicional deja 30.000 COP antes de medios y la prueba cuesta 216.000, necesitas más de 7,2 pedidos adicionales para superar ese gasto, sin incluir otros costes del experimento. Ocho compras atribuidas no prueban que haya ocho compras adicionales.

Si la audiencia no tiene volumen suficiente para publicitar, usa un canal directo permitido, simplifica el segmento o acumula observación. No fabriques volumen incluyendo contactos sin permisos ni mezclando prospectos y clientes sin etiquetarlos.

## 7. Diseña una secuencia de mensajes que puedas operar

No prometas una secuencia individual exacta de anuncios salvo que tu configuración realmente pueda imponerla y verificarla. Muchas campañas entregan variantes en orden variable. Piensa en un conjunto de mensajes coherente y en ventanas de relevancia, no en una película que todas las personas verán igual.

### Reposición

- Momento: cerca del consumo estimado del producto, ajustado por cantidad y frecuencia real de compra.
- Mensaje inicial: utilidad y disponibilidad.
- Objeción siguiente: envío, presentación o facilidad para repetir pedido.
- Salida: compra confirmada de reposición, baja o agotamiento de ventana.
- Riesgo: recordar demasiado pronto o asumir que todo comprador consume a igual ritmo.

### Venta cruzada

- Momento: después de la entrega y de una experiencia de uso razonable.
- Mensaje inicial: problema que resuelve el complemento.
- Evidencia: demostración de compatibilidad y uso.
- Salida: compra del complemento, devolución del producto base o incidencia abierta.
- Riesgo: vender artículos que ya venían incluidos en el pedido original.

### Reactivación

- Momento: atraso respecto al patrón de compra de una cohorte comparable.
- Mensaje inicial: novedad relevante o mejora comprobable.
- Segunda opción: resolver una objeción o facilitar el regreso.
- Incentivo: solo cuando la economía y la hipótesis lo justifican.
- Salida: nueva compra o periodo máximo de contacto definido.
- Riesgo: confundir inactividad natural de un producto durable con abandono.

Ejemplo de texto neutral para un complemento: “Más opciones para tu equipo: revisa la guía de compatibilidad y descubre cuándo conviene incorporar [accesorio]”. Evita “sabemos exactamente lo que compraste ayer” o exponer hechos privados en un anuncio que otra persona podría ver.

## 8. Verificación previa al lanzamiento

Un responsable distinto al creador, cuando sea posible, comprueba:

1. La definición de audiencia coincide con el brief.
2. La compra más reciente retira al cliente del mensaje equivocado.
3. Las bajas y reclamaciones están en supresión.
4. El control del experimento no está en listas activas de esta intervención.
5. Se entiende si hay expansión y qué significa para la prueba.
6. El presupuesto, fecha final y moneda son correctos.
7. El producto está disponible y el incentivo es real y aprobado.
8. La página móvil muestra las mismas condiciones que el anuncio.
9. El pago funciona y no hay costes sorpresa ocultos.
10. La medición de prueba no duplica pedidos ni utiliza valor ficticio.
11. Los enlaces tienen etiquetas de campaña sin información personal.
12. Existe una persona responsable de pausar ante incidentes.

Esta comprobación debe completarse con evidencias, no con una colección automática de casillas marcadas. Un pedido de prueba con devolución registrada puede revelar más problemas que una presentación de veinte diapositivas.

## 9. Operación y decisiones

### Primeros días: comprobar integridad

Comprueba entrega, gasto y errores. Si la página está rota, no esperes a que “termine de aprender”. Pausa ante fallos de pago, productos sin stock, permisos inválidos o duplicaciones significativas. Conserva el historial del incidente y la corrección.

Si todo funciona, evita cambiar al mismo tiempo audiencia, oferta, creatividad y presupuesto por una fluctuación diaria. Define revisiones con suficiente tiempo para el ciclo de decisión y para recibir cancelaciones o devoluciones. Un producto que tarda semanas en decidirse no se evalúa igual que un consumible de compra inmediata.

### Revisión periódica

Mira la cadena completa: elegibles → coincidencias disponibles → alcance → visitas → pedidos válidos → contribución. Cada caída requiere una respuesta diferente. La baja coincidencia no se arregla cambiando el video; una tasa alta de devoluciones no se arregla ampliando audiencia.

La frecuencia es un diagnóstico, no un semáforo universal. Considera periodo, tamaño del público, variedad del mensaje y respuesta negativa. Una frecuencia media también oculta que algunas personas reciban muchas más impresiones. Si crece la presión y no mejora el resultado económico, reduce presupuesto, renueva el argumento o deja descansar el segmento.

### Tabla de diagnóstico

| Observación | Pregunta de comprobación | Acción razonable |
|---|---|---|
| No hay entrega | ¿Audiencia elegible, anuncio aprobado y configuración compatible? | Revisar estado y restricciones antes de aumentar gasto |
| Muchos clics, pocas compras | ¿Destino, compatibilidad, precio y pago funcionan? | Auditar experiencia móvil y calidad de visitas |
| Buen ROAS, poco cambio en ventas totales | ¿Se atribuyen compras que habrían ocurrido igual? | Medir con control y revisar cobertura cruzada |
| Compradores siguen viendo oferta antigua | ¿La supresión se actualiza y se aplica? | Corregir pipeline y considerar latencia de activación |
| Alto coste y saturación | ¿Base pequeña o mensaje agotado? | Limitar inversión y cambiar propuesta con evidencia |
| Ventas con devoluciones | ¿Promesa, variante o compatibilidad incorrecta? | Corregir oferta; evaluar margen neto maduro |

## 10. Qué debe quedar al cerrar la prueba

Entrega un informe de una página y adjunta los detalles: hipótesis, fechas, población, exclusiones, configuración efectiva, gastos, ventas netas y limitaciones. Separa la información de plataforma de la del sistema de pedidos. Si hubo control, informa el resultado por cliente asignado y la incertidumbre; no elimines después a quienes no vieron el anuncio para mejorar el indicador.

La decisión final puede ser escalar, repetir con un cambio, mantener con límite, o detener. “Aprendimos que esta base no justifica publicidad adicional” es un resultado válido. El programa existe para mejorar el negocio y la relación con el cliente, no para mantener campañas encendidas.
