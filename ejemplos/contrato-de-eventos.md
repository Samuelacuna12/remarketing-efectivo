# Ejemplo de contrato de eventos y reglas de activación

[Volver al índice](../README.md)

Este es un acuerdo de diseño entre negocio, operaciones y quien mantiene los datos. No es un esquema oficial de Meta, Google ni un proveedor de mensajería, y no debe enviarse completo a ninguno de ellos. Los nombres son ilustrativos. Los datos reales se conservan en sistemas privados y se minimizan por destino.

## 1. Identidad y orden de autoridad

- `customer_id`: identificador interno opaco, nunca correo o teléfono dentro del nombre.
- `order_id`: identificador único del pedido en origen.
- `event_id`: identidad estable de un hecho, reutilizada al reintentar el mismo hecho.
- `occurred_at`: momento de ocurrencia con zona horaria.
- `received_at`: momento de recepción para detectar retrasos.
- `source_system`: sistema responsable y versión de la integración.
- `schema_version`: versión del contrato.

La contabilidad o el sistema de pedidos gobierna cobros y abonos. El sistema de preferencias gobierna permisos. El CRM organiza la relación y los responsables. Un evento de navegador no sobrescribe por sí mismo una devolución o una baja verificada.

## 2. Tabla de hechos

| Hecho interno | Condición de emisión | Uso posible | Comprobación |
|---|---|---|---|
| `order_paid` | Pago confirmado según el negocio | Reconciliar compra y detener mensajes de pago pendientes | Mismo pedido no se suma dos veces |
| `order_delivered` | Entrega confirmada | Iniciar periodo de uso antes de venta cruzada | No se usa fecha de compra como entrega sin indicarlo |
| `order_refunded` | Abono confirmado total o parcial | Actualizar valor neto y retirar recomendaciones incompatibles | Mantiene vínculo con pedido y productos |
| `service_completed` | Servicio prestado según registro operativo | Preparar cuidado, revisión o renovación | No equivale a reserva creada |
| `consent_withdrawn` | Retiro efectivo de permiso | Supresión de finalidad y canales correspondientes | Prioridad sobre campañas pendientes |
| `support_case_opened` | Incidencia relevante registrada | Pausar presión comercial según política interna | No exporta contenido sensible del caso |
| `support_case_resolved` | Cierre validado | Revisión de elegibilidad, sin venta automática obligatoria | No restaura un permiso retirado |
| `repeat_order_paid` | Nueva compra válida, ligada al cliente | Salida de reposición y actualización de cohorte | No confunde reintento con nueva compra |

## 3. Ejemplo sintético de hecho mínimo

```json
{
  "schema_version": "1.0",
  "event_id": "synthetic-order-001-delivered-v1",
  "event_type": "order_delivered",
  "customer_id": "synthetic-customer-001",
  "order_id": "synthetic-order-001",
  "occurred_at": "2026-11-01T10:00:00-05:00",
  "received_at": "2026-11-01T10:00:05-05:00",
  "source_system": "demo_orders",
  "category": "consumible_demo",
  "contains_real_personal_data": false
}
```

## 4. Reglas de procesamiento

1. Validar el esquema y los campos requeridos.
2. Identificar si `event_id` ya fue procesado para esa operación.
3. Registrar el hecho antes de ejecutar una acción externa.
4. Recalcular elegibilidad con el estado más reciente de compra, permiso e incidencia.
5. Dar prioridad a supresión y baja sobre envíos comerciales.
6. Verificar grupo experimental y política de presión.
7. Crear una orden de envío con clave idempotente por cliente, flujo, ciclo y paso.
8. Antes de enviar, consultar otra vez elegibilidad si pasó tiempo en cola.
9. Registrar resultado, errores y siguiente revisión.
10. Reintentar solo fallos apropiados; una baja o rechazo definitivo no se reintenta como si fuera un error temporal.

No asumas entrega exactamente una vez en una red distribuida. Un proveedor puede aceptar una solicitud y perderse su respuesta. Diseña una conciliación de estados y usa sus mecanismos oficiales de idempotencia cuando existan. El objetivo es evitar mensajes duplicados y conservar evidencia para investigar.

## 5. Eventos tardíos y correcciones

Si una devolución llega después de preparar el segmento, retira al cliente antes del siguiente paso comercial. Si llega después de enviar, evita continuar el flujo y registra el incidente. No puedes deshacer un mensaje ya entregado; sí impedir los siguientes y corregir el proceso.

Si dos sistemas discrepan, utiliza una cola de revisión y aplica la regla conservadora definida para el caso. No soluciones conflictos borrando silenciosamente la evidencia. Documenta quién puede corregir un pedido, un permiso o una identidad.

## 6. Pruebas de aceptación

| Caso | Resultado esperado |
|---|---|
| Se recibe dos veces la misma entrega | Una sola entrada al ciclo correspondiente |
| El cliente compra antes de salir el recordatorio | Cancelar el mensaje pendiente |
| Baja recibida mientras hay mensajes en cola | Bloquear los envíos de la finalidad afectada |
| Se abre incidencia importante | Pausar venta cruzada hasta revisión |
| Se devuelve el producto base | No recomendar su accesorio como si siguiera usándolo |
| Un miembro del control cumple el disparador | Registrar elegibilidad, sin ejecutar la intervención |
| Falla el proveedor temporalmente | Reintento limitado y trazable, sin duplicar |
| La sincronización deja de funcionar | Alerta y pausa del flujo dependiente según riesgo |
| Cambia la cantidad del pedido | Recalcular reposición con la regla y versión acordadas |

## 7. Entrega al equipo

Añade al contrato: propietario, fecha de cambio, sistemas afectados, política de retención, alcance de acceso, plazo de corrección y responsables de incidentes. Un cambio en la definición de compra o permiso debe pasar por revisión antes de alterar audiencias activas.
