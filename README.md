
# ESP32 Client and Django Server Developer

## Roadmap general (en hitos)

### Hito A — Contrato y base del sistema (sin DB)

1. **Definir el contrato de datos (JSON)**

* Qué campos viajan, tipos, unidades, timestamps, etc.
* Definir versión: `schema_version: 1`.

2. **Django: API mínima**

* Proyecto Django + app `api`.
* Endpoint GET que devuelva JSON estático (mock), ej: `/api/v1/data/`.

3. **ESP32: cliente HTTP mínimo**

* Conectar Wi-Fi.
* Hacer GET al endpoint.
* Parsear JSON y mostrar por serial.

✅ Objetivo: “ESP32 lee JSON real desde Django” aunque el JSON sea mock.

---

### Hito B — Persistencia (DB) + API real

4. **Modelo en Django + migraciones**

* Crear modelo `Record` (o el dominio que sea).
* Guardar algunos registros manualmente (admin o shell).

5. **API: devolver datos desde DB**

* Endpoint que liste últimos N registros.
* Paginación simple o `?limit=...`.

✅ Objetivo: “ESP32 lee datos reales que vienen desde DB”.

---

### Hito C — Ingesta: API calls + scraping

6. **Pipeline de ingesta**

* Un “provider” por fuente:

  * Provider API (requests + auth + rate limit)
  * Provider Scraping (requests + bs4/selectores)
* Normalizar al esquema interno.
* Guardar en DB.

7. **Ejecución programada**

* Opción 1: `cron` + management command de Django.
* Opción 2: Celery + beat (más pro, pero más setup).
* Empezar por cron/management command.

✅ Objetivo: “DB se actualiza sola desde fuentes externas”.

---

### Hito D — Robustez y producto

8. **Seguridad**

* API key simple o JWT (depende caso).
* TLS (HTTPS).
* Rate limit en API.

9. **Observabilidad**

* Logs, métricas básicas, errores de scraping.
* Alertas si falla una fuente.

10. **Deploy**

* Docker para Django.
* DB (Postgres recomendado).
* Reverse proxy (Nginx) + HTTPS.

✅ Objetivo: “sistema estable y desplegable”.

---

