# 11. Privacidad, permisos y gobierno operativo

Una estrategia de recompra depende de confianza: el cliente entiende quién le contacta, recibe algo pertinente y puede decidir que ya no quiere publicidad. Este capítulo convierte esa idea en controles prácticos para una empresa pequeña o mediana.

Las recomendaciones de operación no sustituyen una revisión jurídica. Las obligaciones cambian según país, canal, tipo de destinatario, sector y uso de datos. Las referencias oficiales enlazadas se consultaron el **11 de noviembre de 2026**. Revisa sus versiones antes de una implementación real, especialmente si trabajas en varios países o en sectores regulados.

## 1. Una compra no responde todas las preguntas de permiso

El dato necesario para entregar un pedido puede tener una finalidad distinta del que se usa para enviar promociones, perfilar compras o compartir identificadores con una plataforma publicitaria. Conserva esas decisiones separadas en tu sistema.

Antes de activar un canal, identifica: qué dato utilizas, de dónde procede, para qué finalidad se obtuvo, qué información recibió la persona, qué autorización o base jurídica corresponde y cómo se puede ejercer una baja. Que el CRM permita seleccionar un contacto no demuestra que ese contacto sea elegible.

Como política operativa para este manual, utiliza solamente datos propios con procedencia documentada y permisos o bases aplicables verificadas; excluye los contactos dudosos mientras resuelves su situación. Evita listas compradas, copiadas de directorios o extraídas de redes. Una cuenta de empresa o un correo de trabajo tampoco debe considerarse automáticamente libre de restricciones.

## 2. Haz un inventario de tratamientos antes de elegir herramientas

No necesitas empezar comprando un sistema nuevo. Puedes comenzar con un inventario privado y mantenido por un responsable:

| Flujo | Datos mínimos | Finalidad | Destino | Evidencia y control |
|---|---|---|---|---|
| Confirmación de pedido | Identificador y contacto necesario | Atender la compra | Proveedor transaccional | Plantilla revisada y acceso limitado |
| Recordatorio de reposición | Cliente, categoría general y fecha | Promoción pertinente | CRM autorizado | Permiso/base y exclusiones |
| Audiencia publicitaria | Identificadores admitidos | Personalización publicitaria | Plataforma concreta | Condiciones, información y consentimiento cuando corresponda |
| Experimento de recompra | ID interno, grupo y resultado | Evaluar intervención | Almacén privado | Accesos y plazo definidos |
| Tablero de dirección | Agregados | Decisión de negocio | Herramienta de análisis | Sin contactos ni celdas que identifiquen personas |

Añade responsable, proveedor, país de tratamiento, plazo de retención y procedimiento de eliminación. Anota si el flujo usa datos de menores, información sensible o inferencias delicadas; este repositorio no propone campañas basadas en esos datos.

La utilidad del inventario aparece cuando alguien cambia una integración. Puedes comprobar qué finalidades y proveedores se ven afectados, en vez de descubrir después que una copia antigua sigue enviando promociones.

## 3. Registra preferencias con suficiente detalle

Un campo `acepta_marketing = sí` suele quedarse corto. Un modelo operativo más claro registra, en un entorno privado:

- Identificador interno del cliente y canal de contacto normalizado.
- Finalidad y canal a los que se refiere la preferencia.
- Estado: pendiente, permitido, retirado, bloqueado o por revisar.
- Fecha, origen y mecanismo mediante el que se registró la decisión.
- Versión del texto mostrado y prueba disponible.
- País o contexto de recogida cuando sea necesario para aplicar reglas.
- Fecha y causa de los cambios posteriores.

No inventes una fecha de consentimiento para rellenar campos vacíos. Si migras un CRM, conserva la evidencia original y marca incertidumbres. Una importación no debe convertir un estado desconocido en autorización.

Las preferencias también pueden cambiar por una respuesta humana. Si alguien escribe «no me envíen más promociones» al vendedor, ese mensaje debe llegar al sistema central de exclusión. No exijas que utilice una palabra exacta para respetar una decisión comprensible.

## 4. Crea una lista de supresión que gane a cualquier campaña

La lista de supresión impide que una automatización vuelva a activar a quien no debe recibir publicidad. No es una audiencia comercial que se pueda reutilizar para otra finalidad.

Define precedencia: una baja aplicable supera una selección por RFM, una compra reciente o una importación nueva. Antes de cada envío, evalúa otra vez el estado actual. Si el mensaje se programó ayer y la persona retiró permiso hoy, el sistema debe retirarla de la cola.

Diseña un circuito de propagación: canal de recepción → registro central → colas pendientes → automatizaciones → listas publicitarias pertinentes → confirmación operativa. Guarda evidencia del cambio y de los destinos actualizados. Concreta un objetivo interno de rapidez y monitorea fallos; el objetivo interno no sustituye plazos legales aplicables.

Puede ser necesario conservar un identificador mínimo para impedir recontactos accidentales, aunque se eliminen datos comerciales. Decide su base, finalidad, acceso y retención con asesoría adecuada. Borrar todo sin pensar puede permitir que una siguiente importación reincorpore a la misma persona.

## 5. Trata el hash como protección técnica, no como permiso

Hashear un correo antes de cargarlo ayuda a transformar el identificador para ciertos procesos de coincidencia. No convierte automáticamente la operación en anónima ni autoriza a compartirlo. Si una plataforma puede compararlo con una identidad, sigue existiendo una finalidad de vinculación que debe revisarse.

En Customer Match, Google limita la carga a información recogida directamente en un contexto propio, exige informar sobre determinados usos por terceros y obtener consentimiento cuando lo exijan las normas o políticas aplicables. También restringe usos relativos a categorías sensibles. Verifica la política completa y la elegibilidad de la cuenta antes de implementar. [Política oficial de Customer Match](https://support.google.com/adspolicy/answer/6299717?hl=en).

Para otras plataformas, lee sus condiciones vigentes desde la cuenta y documenta la revisión. No supongas que aceptar una política de cookies cubre cualquier carga de CRM, ni que un permiso para email cubre automáticamente publicidad personalizada o WhatsApp. La revisión debe seguir la finalidad y el canal concreto.

## 6. Mantén los eventos y enlaces libres de información indebida

Los errores no siempre ocurren en una carga de audiencias. Una URL puede contener un email; el título de una página puede revelar el asunto de una consulta; un campo de texto libre puede incluir información privada que termina en el píxel o la herramienta de análisis.

Como diseño técnico, utiliza una lista permitida de parámetros. Envía solo eventos y campos necesarios, definidos y revisados. Evita nombres, teléfonos, correos, direcciones completas, notas del vendedor, conversaciones y otros datos personales en URLs, UTMs, nombres de campañas y propiedades no destinadas a identificadores personales.

Revisa también páginas de confirmación, formularios, búsqueda interna, nombres de productos delicados y campos de errores. No construyas audiencias por condiciones de salud, dificultades económicas, creencias, vida íntima u otras categorías sensibles. Una inferencia puede ser tan delicada como un dato declarado.

Prueba con datos ficticios: navega, rechaza permisos cuando corresponda, actualiza preferencias y observa qué eventos se transmiten. Comprueba navegador y servidor; trasladar el envío a una integración de servidor no elimina la necesidad de respetar las decisiones de la persona.

## 7. Sitios web, cookies y preferencias regionales

No copies un banner de otra web suponiendo que cumple en todo lugar. Mapea las tecnologías que almacenan o acceden a información del dispositivo, sus finalidades, proveedores y regiones. La lógica de activación tiene que corresponder con las opciones que se muestran.

En el Reino Unido, el ICO explica que el uso de tecnologías de almacenamiento y acceso para publicidad online requiere consentimiento bajo PECR, además de cumplir las reglas de protección de datos cuando se utilizan datos personales. Este ejemplo regional no debe trasladarse sin análisis a todos los países. [ICO: planificación del marketing directo](https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/direct-marketing-guidance/plan-direct-marketing/).

Operativamente, define un estado inicial, cómo se guarda la elección, cómo llega a las integraciones y cómo se retira. Una herramienta de gestión de consentimiento puede ayudar, pero necesita configuración y pruebas. Si un nuevo proveedor empieza a recibir eventos, actualiza el inventario y revisa el alcance de las opciones antes de activarlo.

## 8. Colombia: puntos que conviene verificar expresamente

La Ley 1581 de 2012 establece principios, derechos de los titulares y deberes sobre tratamiento de datos personales. Su régimen incluye autorización previa, expresa e informada y excepciones específicas; no presupongas que una relación comercial resuelve cualquier uso publicitario. Revisa finalidad, información al titular, seguridad y procedimientos de derechos con quien lleve el cumplimiento de tu negocio. [Ley 1581 en Función Pública](https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=49981).

La SIC ha señalado que para marketing deben existir pruebas de la autorización correspondiente y debe atenderse la supresión o suspensión solicitada por el titular. En la práctica, conserva la evidencia y haz que la baja se propague a proveedores y automatizaciones. [SIC: tranquilidad y supresión de datos](https://sedeelectronica.sic.gov.co/publicaciones/boletin-juridico/concepto/derecho-la-tranquilidad-y-supresion-de-datos-personales).

La Ley 2300 de 2023 también contiene disposiciones de contacto comercial y publicitario. Su artículo 5 remite para esos mensajes a los horarios del artículo 3: lunes a viernes de 7:00 a 19:00; sábados de 8:00 a 15:00; se excluyen domingos y festivos. Incluye un mecanismo sencillo para cancelar mensajes y revisa la aplicación concreta de sus demás reglas, excepciones y regulación vigente. Evita convertir las disposiciones específicas de cobranza en una regla genérica sin análisis. [Texto oficial de la Ley 2300](https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=213990).

El RNE administrado por la CRC permite restringir contactos publicitarios en los canales previstos. Incorpora la consulta aplicable y sus resultados al proceso de elegibilidad; no lo trates como una revisión única al crear la base. El ABC oficial indica consultar antes del envío. La interacción entre autorizaciones y registro requiere aplicar la normativa y criterios vigentes al caso. [CRC: RNE](https://www.crcom.gov.co/es/micrositios/comunicados-como-es/registro-numeros-excluidos), [ABC oficial para empresas y usuarios](https://www.crcom.gov.co/sites/default/files/webcrc/noticias/documents/ABC-ACTUALIZACION-REGISTRO-NUMEROS-EXCLUIDOS-250424.pdf).

Para operar, asigna un responsable de calendario colombiano y festivos, registra zona horaria del destinatario cuando corresponda y configura las colas para no ejecutar una promoción fuera del horario permitido. Comprueba cómo actúan reintentos y tareas retrasadas: un envío inicialmente programado dentro de horario puede terminar ejecutándose después.

## 9. Si operas en Europa u otros mercados

El RGPD reconoce en su artículo 21 el derecho a oponerse al tratamiento con fines de marketing directo, incluido el perfilado relacionado, y establece que los datos dejen de tratarse con esos fines ante la oposición. La base jurídica, las normas de comunicaciones electrónicas y los requisitos locales deben evaluarse además según el caso. [RGPD: texto oficial, artículo 21](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32016R0679).

En una operación internacional, crea una matriz por país y canal mantenida por asesoría competente. Incluye requisitos de contacto, tecnologías de seguimiento, derechos, transferencias, proveedores y sectores especiales. Aplica a cada flujo la configuración validada para su contexto. Este manual no intenta sustituir esa matriz con una casilla universal de consentimiento.

Si no puedes determinar correctamente las reglas de una región, mantén esos contactos fuera del piloto mientras lo resuelves. Puedes avanzar con una población cuya elegibilidad ya esté comprobada.

## 10. Accesos, proveedores y retención

Otorga a cada persona el acceso que necesita para su función. Un diseñador puede trabajar con ejemplos de perfiles y mensajes sin descargar la base completa. Un analista puede recibir resultados seudonimizados y agregados sin números de teléfono. El responsable de campañas necesita permisos limitados a los destinos que administra.

Define quién aprueba proveedores, qué datos reciben, qué contrato o condiciones aplican, qué subproveedores intervienen y cómo se gestiona una retirada. Cuando una agencia deja de trabajar contigo, revoca sus accesos y confirma el tratamiento de las copias que conservaba.

Establece retención por tipo de dato y finalidad. No uses «para siempre» porque el almacenamiento sea barato. Programa revisiones, borrado o agregación donde corresponda y conservación separada de lo necesario para obligaciones contables u otras finalidades válidas. Borrar un contacto del CRM no garantiza que desaparezca de una exportación, una copia en la agencia o un proveedor de mensajería.

## 11. Gobierno pequeño pero verificable

| Función | Responsabilidad mínima |
|---|---|
| Dirección | Aprobar objetivo comercial, riesgo aceptable y recursos |
| Responsable de datos/privacidad | Validar usos, derechos, proveedores y evidencias |
| Operaciones CRM | Aplicar permisos, supresiones, calendario y deduplicación |
| Medios | Revisar audiencias, exclusiones y destinos publicitarios |
| Atención | Recibir bajas y reclamaciones y escalarlas al sistema central |
| Análisis/Finanzas | Conciliar pedidos, costes, devoluciones e informes |

En un equipo de dos personas, varias funciones pueden recaer en la misma persona. Sigue siendo útil escribir quién decide y quién verifica. Para cambios relevantes, registra fecha, motivo, configuración anterior, nueva configuración y resultado de la prueba.

Haz una revisión periódica corta: una muestra de bajas, una de contactos activos, una de eventos enviados y una de sincronizaciones fallidas. Investiga por qué un contacto quedó incluido, no solo si aparecía en una lista. La trazabilidad permite corregir la causa sin bloquear todo el sistema.

## 12. Qué hacer ante un error de contacto

Si una persona recibe una promoción después de retirarse, detén el flujo afectado, registra el incidente y aplica la supresión actual. Identifica si falló el dato central, una cola, una importación, un proveedor o un contacto manual. Conserva evidencia suficiente para investigar sin distribuir de nuevo los datos de la persona.

El responsable correspondiente debe evaluar las obligaciones de comunicación, respuesta y reporte según jurisdicción y gravedad. No existe una respuesta universal que se pueda automatizar desde este repositorio. Corrige la causa, prueba con registros ficticios y documenta cuándo se reanudó el flujo.

La misma lógica sirve para una carga errónea a publicidad: parar sincronización, identificar alcance, gestionar retirada o eliminación según los mecanismos disponibles y verificar la corrección. No intentes compensar una baja enviando otra promoción con disculpas.

## 13. Mantén este repositorio público limpio

Este repositorio contiene formación, plantillas y ejemplos sintéticos. Una plantilla de audiencias describe reglas; no debe convertirse en un archivo con los contactos de tus compradores.

No añadas correos reales, teléfonos, pedidos identificables, exports de CRM, capturas con clientes, claves, tokens, cookies, identificadores privados de plataformas ni enlaces temporales a bases. Guarda datos operativos en sistemas privados autorizados. Comprueba que muestras y capturas estén anonimizadas de forma efectiva; cambiar solo el nombre puede dejar suficientes detalles para reconocer a alguien.

Para pedir ayuda mediante una incidencia pública, describe el problema con un caso ficticio reproducible. Si detectas una credencial expuesta, su eliminación del archivo visible no basta: revócala y sigue el procedimiento de seguridad del servicio. Un repositorio público es un buen lugar para compartir el método; las decisiones y datos de contacto de cada cliente requieren su propio entorno protegido.
