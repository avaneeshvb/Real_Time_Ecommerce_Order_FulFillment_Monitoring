# 🚀 Real-Time Ecommerce Risk Monitoring Platform

A real-time streaming data engineering system that monitors ecommerce operational risks such as SLA breaches, fulfillment bottlenecks, and inventory stockouts using Shopify event streams.

---

# 📌 Problem Statement

Ecommerce platforms often face delays in detecting operational issues such as:
- Late order deliveries
- Warehouse bottlenecks
- Inventory shortages

Batch processing systems detect these issues too late.

This project builds a **real-time streaming pipeline** to detect such issues instantly.

---

# 🏗️ Architecture

                ┌────────────────────────────┐
                │   Shopify Webhooks        │
                │ (Orders / Fulfillments /  │
                │  Inventory Events)        │
                └────────────┬──────────────┘
                             │
                             ▼
                ┌────────────────────────────┐
                │   FastAPI Ingestion Layer │
                │ - Signature verification  │
                │ - Event normalization     │
                └────────────┬──────────────┘
                             │
                             ▼
                ┌────────────────────────────┐
                │   Redpanda (Kafka)        │
                │ - ecommerce_events topic  │
                └────────────┬──────────────┘
                             │
          ┌──────────────────┴──────────────────┐
          ▼                                     ▼
┌──────────────────────┐          ┌──────────────────────┐
│ PyFlink Streaming     │          │  Dead Letter Queue   │
│ - SLA breach          │          │  (invalid events)    │
│ - Bottlenecks         │          └──────────────────────┘
│ - Inventory risk      │
└───────────┬───────────┘
            │
            ▼
┌────────────────────────────┐
│   BigQuery (GCP Warehouse)│
│ - orders_raw              │
│ - fulfillment_raw         │
│ - inventory_raw           │
│ - alerts tables           │
└────────────┬──────────────┘
             │
             ▼
┌────────────────────────────┐
│       dbt Layer           │
│ - SLA metrics             │
│ - Bottleneck analysis     │
│ - Inventory risk marts    │
└────────────┬──────────────┘
             │
             ▼
     ┌─────────────────┐
     │ KPI Dashboards  │
     │ (Looker / BI)   │
     └─────────────────┘

---

# ⚙️ System Design

## Data Flow

1. Shopify Webhooks send events (orders, fulfillment, inventory)
2. FastAPI receives and normalizes events
3. Events are published to Redpanda (Kafka)
4. PyFlink processes streams in real time
5. Data is stored in BigQuery
6. dbt transforms data into analytical models
7. KPIs are generated for monitoring

---

# 📊 Key KPIs

## 1. SLA Breach Detection
Detects orders not fulfilled within X hours.

## 2. Fulfillment Bottleneck Detection
Identifies congestion in fulfillment pipelines.

## 3. Inventory Stockout Risk
Detects products running below safe stock thresholds.

---

# 🧰 Tech Stack

- FastAPI
- Redpanda (Kafka-compatible streaming)
- PyFlink (stream processing engine)
- Google BigQuery
- dbt (data transformations)
- Docker

---

# 📁 Project Structure
app/ # FastAPI webhook + Kafka producer
flink/ # PyFlink streaming jobs
bigquery/ # BigQuery schemas + sink logic
dbt_project/ # dbt models (staging + marts)
docker-compose.yml # Local orchestration



---

# 🚀 How to Run

## 1. Start infrastructure
```bash
docker-compose up

2. Run FastAPI
uvicorn app.main:app --reload

3. Run streaming jobs
python flink/jobs/sla_breach.py
python flink/jobs/inventory_risk.py

📡 Example Webhook Payload
{
  "id": 12345,
  "created_at": "2025-04-21T10:00:00Z",
  "total_price": "2500",
  "line_items": [ ... ]
}


📈 Output Example
SLA_BREACH: order_123
BOTTLENECK_ALERT: warehouse_2
STOCKOUT_RISK: product_456


🧠 Key Learnings
Real-time streaming architecture design
Event-driven data pipelines
Stateful stream processing using PyFlink
Data warehousing with BigQuery
ELT modeling using dbt


🔮 Future Improvements
Add anomaly detection using ML models
Add real-time dashboards (Looker / Grafana)
Add schema registry for Kafka events
Deploy on Kubernetes
