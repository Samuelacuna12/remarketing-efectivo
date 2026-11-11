# 06. Email, WhatsApp y CRM: un sistema que responde al cliente

> Las recomendaciones operativas de este capítulo son un diseño de trabajo propuesto, no requisitos universales ni una promesa de resultados. Las referencias de plataforma se consultaron el **11 de noviembre de 2026**. Antes de activar mensajes, valida las reglas vigentes, la jurisdicción y los permisos de tu base.

## 1. El CRM decide; cada canal ejecuta una parte

Un cliente puede tener varios correos, un teléfono compartido con su empresa, pedidos en tienda y compras en la web. También puede abrir un reclamo mientras una automatización prepara una oferta. Si cada canal decide por separado, aparece el problema clásico: promociones repetidas, recordatorios de algo ya comprado y conversaciones que nadie atiende.

El CRM debe conservar una identidad interna estable, el historial necesario y el estado comercial actual. No tiene que ser una herramienta cara. En una operación pequeña puede empezar como una base estructurada con automatizaciones sencillas; cuando existen concurrencia, varios vendedores o muchas integraciones, conviene usar un sistema que soporte permisos, registros y colas. La elección depende del volumen y del riesgo de error, no del número de funciones del proveedor.

Define una única fuente para cada hecho. La plataforma de pedidos determina si una compra fue pagada o devuelta; soporte determina si hay una incidencia abierta; el centro de preferencias determina la autorización comercial; el proveedor de mensajería informa aceptación, entrega y errores. El CRM reúne esos hechos, pero no debe reemplazarlos por etiquetas manuales que nunca se actualizan.

La jerarquía recomendada es: primero respetar una baja; después resolver problemas de servicio; después atender una conversación activa; después avisar de una obligación o solicitud concreta; finalmente considerar una oportunidad comercial. Un cliente con una devolución pendiente necesita resolución. Convertir esa situación en un disparador de venta puede empeorar la relación.

## 2. Modelo mínimo de datos

| Grupo | Campos sugeridos | Para qué sirven |
|---|---|---|
| Identidad | `customer_id`, `account_id` B2B, identificadores de origen | Unir pedidos sin depender del email como clave principal |
| Contacto | email normalizado, teléfono normalizado, idioma, zona horaria | Elegir destino, formato y horario |
| Permisos | canal, finalidad, estado, fecha, fuente, versión de aviso, evidencia | Evaluar elegibilidad y atender cambios |
| Compra | pedido, fecha, categoría, SKU, estado, ingreso neto, margen estimado | Recomendar y medir valor real |
| Servicio | reclamo abierto, devolución, responsable, fecha de resolución | Evitar venta inoportuna |
| Relación | última interacción humana, propietario de cuenta, próxima tarea | Coordinar automatización y vendedor |
| Contactabilidad | rebote, bloqueo, baja, última validación, motivo de supresión | Evitar intentos que ya no corresponden |
| Automatización | flujo, versión, entrada, paso, estado, clave de envío | Impedir duplicados y explicar decisiones |

No guardes todo por si acaso. Cada campo debe tener una finalidad, un propietario y una regla de conservación. El repositorio público solo contiene estructuras y ejemplos ficticios; las bases reales y los registros de mensajes pertenecen a un entorno privado con acceso restringido.

Un permiso no debería modelarse como una sola casilla `acepta_marketing = sí`. Una persona puede aceptar correo promocional y rechazar mensajes comerciales por WhatsApp. También puede querer novedades de una categoría y dejar de recibir otra. Representa esas preferencias por canal y finalidad, conservando el historial de cambios sin sobrescribir la evidencia anterior.

## 3. Resolver identidad sin fusionar a personas distintas

1. Usa el identificador del sistema de origen y una tabla de correspondencias.
2. Normaliza espacios y formato de correo; conserva el valor original para auditoría. No elimines puntos ni modifiques proveedores indiscriminadamente.
3. Normaliza teléfonos con código de país y valida su formato antes de utilizarlos. Formato válido no significa que el número pertenezca todavía a la misma persona.
4. Exige una regla de coincidencia suficientemente sólida antes de fusionar. Dos personas que comparten domicilio, empresa o teléfono no son necesariamente el mismo cliente.
5. Cuando una identidad sea ambigua, detén la personalización sensible y envía el caso a revisión.
6. Conserva la posibilidad de deshacer una fusión equivocada y trasladar correctamente pedidos y permisos.

En B2B, diferencia empresa y contacto. Una compra de la empresa no autoriza automáticamente a enviar mensajes a todos sus empleados. Un nuevo responsable de compras puede necesitar una relación propia, mientras que el antiguo contacto ya no debería recibir información contractual. El historial de la cuenta sirve para orientar al vendedor; no justifica compartir datos de otras personas.

## 4. Elegibilidad antes de cada envío

La entrada a un flujo no garantiza el derecho a recibir todos sus pasos. Una persona puede comprar, darse de baja o abrir un ticket durante la espera. Por eso se evalúan las condiciones al entrar y nuevamente justo antes de enviar.

Un evaluador de elegibilidad debería contestar, en este orden:

1. ¿Existe un destino válido y una identidad suficientemente clara?
2. ¿La comunicación encaja en el permiso y la finalidad correspondientes?
3. ¿Hay baja, bloqueo, queja, rebote definitivo o una restricción aplicable?
4. ¿El cliente ya realizó la acción que intentamos conseguir?
5. ¿Hay una incidencia abierta o una conversación humana prioritaria?
6. ¿El producto sigue disponible y la oferta sigue vigente?
7. ¿Otro flujo tiene prioridad o se alcanzó el límite global de contacto?
8. ¿Estamos en un horario permitido y razonable para el destinatario?
9. ¿El canal y el mensaje cumplen sus condiciones actuales?
10. ¿La misma acción ya fue aceptada por el proveedor?

Registrar `suppressed_reason = compra_posterior` es mejor que borrar silenciosamente al cliente de la cola. El dato permite entender por qué no se ejecutó un paso y comprobar que las exclusiones funcionan.

## 5. Email: preparación de entrega

Para Gmail personal, Google exige autenticación y condiciones de envío; para remitentes de gran volumen —alrededor del umbral de 5.000 mensajes diarios según su definición— añade SPF, DKIM, DMARC, alineación del remitente y baja con un clic en mensajes comerciales o de suscripción. También indica TLS, DNS/PTR válidos y una tasa de spam inferior a 0,30%. Ese límite es un requisito de plataforma, no una meta aceptable de quejas. Verifica el conjunto completo y su definición de remitente en las [directrices de Gmail](https://support.google.com/mail/answer/81126?hl=en) y sus [preguntas frecuentes](https://support.google.com/mail/answer/14229414?hl=en).

En la práctica, pide al responsable del dominio y al proveedor de email que documenten: qué servicios envían en tu nombre, qué dominio ve el usuario, si la autenticación pasa en mensajes reales, dónde se reciben respuestas y quién procesa las bajas. Un dominio bonito en la plantilla no demuestra que la configuración esté bien.

Haz una prueba desde el flujo real con un contacto interno de prueba. Revisa el remitente, el enlace, la versión móvil, el texto alternativo de imágenes, el precio y las condiciones. Comprueba que responder llega a una bandeja atendida. Usa el mecanismo de baja del proveedor; no construyas una página que exija iniciar sesión para dejar de recibir promociones.

No lances una base antigua completa en una sola acción. Primero verifica su origen y los permisos; después separa los registros válidos y recientes de los dudosos. Aumentar volumen gradualmente puede ayudar a observar problemas, pero no sanea una base sin autorización. Tampoco cambies de dominio para esquivar una mala reputación: resuelve la causa de las quejas.

Las aperturas son una señal imperfecta, afectada por carga de imágenes y mecanismos de privacidad. Para decidir qué flujo genera valor, combina clics depurados, compras registradas, respuestas, bajas y grupos de comparación. No reenvíes automáticamente a todos los que aparecen como “no abiertos”: pueden haber leído el mensaje sin activar el rastreo.

## 6. WhatsApp: conversación con una responsabilidad operativa

La política vigente requiere que la persona proporcione su contacto y otorgue permiso para comunicaciones posteriores; hay que respetar bajas solicitadas dentro o fuera de WhatsApp. En **WhatsApp Business Platform**, iniciar conversaciones requiere una plantilla aprobada; las respuestas libres se permiten en la ventana de atención de 24 horas, que se abre o reinicia con un mensaje del usuario. Fuera de ella se usan plantillas aprobadas. La automatización debe ofrecer una vía clara de atención humana. Consulta la [política oficial](https://business.whatsapp.com/policy). Estas reglas de Platform no deben extrapolarse sin más a todas las funciones de la aplicación Business.

Una plantilla aprobada no equivale a permiso del destinatario ni asegura entrega. Antes de programarla, el responsable verifica finalidad, categoría, idioma, variables, destino y vigencia. Si el mensaje promociona una oferta, no se debe presentar como una simple actualización de servicio para conseguir otra clasificación. Revisa la categoría efectiva que devuelve la plataforma y los costes actuales en tu proveedor; no uses una tarifa escrita meses antes como presupuesto definitivo.

WhatsApp funciona especialmente bien cuando el siguiente paso es resolver una duda concreta: elegir talla, confirmar compatibilidad o coordinar una renovación compleja. Si nadie puede atender las respuestas, empieza con email y una agenda clara. “Enviar a diez mil contactos” es una operación distinta de “mantener diez mil conversaciones”. Dimensiona la capacidad con un piloto y registra cuántas respuestas requieren intervención.

Para cada envío define una salida humana: equipo, horario, plazo interno de atención y un mensaje de recepción que no prometa una respuesta inmediata inexistente. Cuando el cliente escribe, pausa promociones durante la conversación. El agente debe ver el mensaje que originó la respuesta, la oferta vigente y las compras relevantes, sin pedir otra vez información que ya tiene.

## 7. Ejemplo de flujo de reposición

**Supuesto ficticio:** una tienda vende un consumible cuyo intervalo observado de recompra está cerca de seis semanas. El número es ilustrativo; se sustituye por datos de categoría y comportamiento del negocio.

| Paso | Condición y acción | Salida o pausa |
|---|---|---|
| Entrada | Pedido entregado y no devuelto; calcular fecha estimada de reposición | Si no hay permiso comercial, no entrar en marketing |
| Preparación | Unos días antes de la estimación, revisar nueva compra y stock | Si ya repuso, recalcular desde la nueva compra |
| Mensaje 1 | Email con forma de repetir pedido y opción de ajustar frecuencia | Si compra, terminar objetivo y pasar a poscompra |
| Espera | Esperar un intervalo definido en el experimento | Si hay reclamo o baja, cancelar pasos pendientes |
| Mensaje 2 | Solo si sigue elegible; resolver una objeción distinta | Si responde, transferir a atención y pausar promoción |
| Cierre | Finalizar secuencia; no repetir indefinidamente | Registrar resultado y próxima revisión de elegibilidad |

Antes de usar WhatsApp como segundo canal, comprueba permiso y condiciones del canal. No conviertas “no hizo clic en email” en “quiere que lo contacten por teléfono”. Puede no necesitar nada. La secuencia necesita una fecha de caducidad y un límite de intentos. Un objetivo sensato es facilitar una decisión, no agotar toda la lista.

## 8. Ejemplo de renovación B2B

La renovación empieza por la cuenta: contrato, fecha, responsable, uso, incidencias y proceso de compra. El contacto comercial trabaja con una tarea en el CRM, no con un descuento masivo. Un primer recordatorio puede invitar a revisar necesidades; otro puede resumir alcance y pendientes; el último debe indicar una fecha contractual real si existe.

Configura una regla que impida que la automatización envíe una oferta genérica mientras hay una negociación abierta. Si el vendedor cambió el alcance, el mensaje automático anterior puede contradecir la propuesta. Para cuentas con varios contactos, designa quién recibe cada comunicación: decisor, usuario y facturación no necesitan el mismo contenido.

Mide renovaciones sobre contratos elegibles, margen retenido y tiempo de resolución, además de respuestas. Una respuesta negativa rápida puede ser útil para planificar capacidad, pero no es una renovación. Separa “reunión agendada”, “propuesta enviada”, “acuerdo verbal” y “contrato confirmado”.

## 9. Deduplicación e idempotencia

Los sistemas reintentan cuando no reciben confirmación. Si llega dos veces el evento de entrega de un pedido, el flujo no debe empezar dos veces. Si un proveedor aceptó el mensaje pero tu integración perdió la respuesta, repetir a ciegas puede duplicar el contacto.

Diseño recomendado:

- Un identificador único por evento de origen y una tabla de eventos procesados.
- Una inscripción por combinación de cliente, flujo, versión y ciclo comercial.
- Una clave de envío estable, por ejemplo `customer_id + flow_id + cycle_id + step_id`.
- Una restricción de unicidad que reserve esa clave antes del envío.
- Un registro del identificador devuelto por el proveedor y de cada transición de estado.
- Reintentos controlados que consulten la situación anterior, sin generar una nueva clave para la misma acción.

No reutilices el `order_id` como única clave de todos los mensajes: un pedido puede necesitar varios pasos legítimos. Tampoco generes un identificador aleatorio nuevo en cada reintento: deja de ser una protección contra duplicados.

La promesa razonable es reducir duplicados y hacerlos investigables. No presupongas entrega “exactamente una vez” entre proveedores independientes. Diseña para eventos repetidos, retrasados y fuera de orden. Si una baja llega después de reservar un envío pero antes de ejecutarlo, el último control de elegibilidad debe detenerlo.

## 10. Estados y fallos

| Estado | Significado operativo | Acción |
|---|---|---|
| Pendiente | Existe una intención, todavía no enviada | Reevaluar permisos y vigencia |
| Reservado | Un proceso obtuvo la clave única | Evitar que otro trabajador envíe lo mismo |
| Aceptado | El proveedor recibió la solicitud | Guardar identificador; no marcar como leído |
| Entregado | Hay confirmación de entrega disponible | Actualizar registro sin inferir interés |
| Respondido | El cliente escribió | Asignar atención, pausar flujo comercial |
| Error temporal | Hay una causa potencialmente recuperable | Reintentar con límite y espera definida |
| Error definitivo | Destino inválido o rechazo no recuperable | Suprimir ese destino y revisar causa |
| Desconocido | Se perdió confirmación | Conciliar con proveedor antes de repetir |
| Cancelado | Ya no es elegible | Conservar razón y evitar reingreso accidental |

Una cola de fallos debe tener propietario. Revisarla semanalmente no sirve si contiene mensajes de una promoción que termina hoy. Define caducidad por mensaje: después de cierta hora, la oferta ya no se debe enviar, aunque el problema técnico se resuelva.

No uses automáticamente otro canal después de un rechazo. Si el teléfono está bloqueado, no significa que el cliente desee recibir lo mismo por email. Un cambio de canal exige su propia elegibilidad y una razón de servicio o comercial documentada.

## 11. Límite global de contacto y prioridad

Empieza con un límite interno conservador definido por tu negocio y el tipo de mensaje; no existe una frecuencia óptima universal. Incluye campañas, automatizaciones y contactos manuales comerciales en el mismo registro. El límite debe poder reducirse para segmentos con señales de cansancio.

Un orden inicial para conflictos puede ser: atención de solicitud, renovación próxima, reposición probable, segunda compra, venta cruzada, campaña general. Si dos acciones tienen prioridad similar, usa la más relevante y cancela o pospone la otra. No envíes ambas para “aprovechar el día”.

Las comunicaciones necesarias de servicio deben gestionarse según su finalidad propia y las obligaciones aplicables. No añadas una promoción a un aviso crítico para saltarte una baja comercial. Documenta cómo se clasifican y revisa ese criterio con los responsables correspondientes.

## 12. Panel de salud y rutina

Cada día de piloto: revisar mensajes aceptados, errores, bajas, quejas y conversaciones sin asignar. Cada semana: revisar compras posteriores, margen, duplicados, incumplimientos del límite, retraso de sincronización y razones de exclusión. Cada mes: revisar segmentos, permisos, conservación y flujos que siguen activos sin aportar valor.

Alerta útil: “hay 27 conversaciones comerciales sin atender desde ayer”. Alerta poco útil: “la tasa de apertura bajó dos puntos” sin muestra, contexto ni decisión asociada. Define quién puede pausar el flujo y cómo se reanuda después de corregir la causa.

**Criterio de terminado:** puedes explicar por qué una persona recibió un mensaje, demostrar que era elegible en ese momento, identificar la oferta y la versión del texto, mostrar qué ocurrió después y detener todos los pasos pendientes cuando corresponde.

---

[Volver al índice](../README.md) · [Siguiente: mensajes y ofertas](07-mensajes-ofertas-y-creatividades.md)
