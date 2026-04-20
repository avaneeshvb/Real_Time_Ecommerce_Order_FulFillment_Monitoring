🚀 Real-Time Ecommerce Risk Monitoring Platform

A real-time streaming data engineering system that detects operational risks in ecommerce workflows such as SLA breaches, fulfillment bottlenecks, and inventory stockouts using event-driven architecture.

Built using Shopify webhooks, Redpanda (Kafka-compatible streaming), PyFlink, BigQuery, and dbt.

📌 Problem Statement

Modern ecommerce systems generate continuous streams of events across orders, fulfillment, and inventory.

However, traditional batch pipelines:

Detect failures too late
Lack real-time visibility
Fail to capture operational bottlenecks as they occur
🎯 Goal of this project

To build a real-time streaming system that detects operational risks instantly using event-driven architecture.

🏗️ Architecture
Shopify Webhooks
        |
        v
FastAPI Ingestion Layer
- Signature verification
- Event normalization
        |
        v
Redpanda (Kafka-compatible broker)
        |
        v
PyFlink Streaming Engine
- Stateful stream processing
- Real-time KPI detection
        |
        +----------------------+
        |                      |
        v                      v
BigQuery (GCP Warehouse)   Dead Letter Queue
- Raw event storage        - Invalid events
- Analytics layer
        |
        v
dbt Transformation Layer
- SLA metrics
- Bottleneck analysis
- Inventory risk models
        |
        v
BI Dashboards (Looker / Visualization Layer)
⚙️ System Design Overview

The system is built as a fully streaming pipeline:

Shopify emits webhook events (orders, fulfillment, inventory)
FastAPI ingests and normalizes events
Events are streamed into Redpanda
PyFlink processes events in real time
Clean data is stored in BigQuery
dbt transforms raw data into analytical models
KPIs are computed for operational monitoring
📊 Key KPIs Implemented
1. SLA Breach Detection

Detects orders not fulfilled within a defined time threshold (e.g., 6 hours).

Business Impact:

Identifies delayed deliveries
Improves customer satisfaction tracking
2. Fulfillment Bottleneck Detection

Detects accumulation of orders in specific statuses or warehouses.

Business Impact:

Identifies operational inefficiencies
Helps optimize warehouse throughput
3. Inventory Stockout Risk

Detects when product inventory falls below a safe threshold.

Business Impact:

Prevents lost sales
Improves stock planning
🧰 Tech Stack
FastAPI → Webhook ingestion layer
Redpanda (Kafka-compatible) → Event streaming backbone
PyFlink → Real-time stream processing engine
Google BigQuery → Cloud data warehouse
dbt → Data transformation and modeling
Docker → Local orchestration
📁 Project Structure
app/                → FastAPI webhook + Kafka producer
flink/jobs/        → PyFlink streaming jobs (KPI logic)
bigquery/          → Schemas + sink integration
dbt_project/       → Transformation models (staging + marts)
docker-compose.yml → Local infrastructure setup
🚀 How to Run
1. Start infrastructure
docker-compose up
2. Run FastAPI server
uvicorn app.main:app --reload
3. Run streaming jobs
python flink/jobs/sla_breach.py
python flink/jobs/inventory_risk.py
4. Simulate webhook event
curl -X POST http://localhost:8000/shopify \
-H "X-Shopify-Topic: orders/create" \
-H "X-Shopify-Hmac-Sha256: test" \
-d '{...json payload...}'
📡 Example Event Payload
{
  "id": 12345,
  "created_at": "2025-04-21T10:00:00Z",
  "total_price": "2500",
  "line_items": [
    {
      "product_id": "p1",
      "quantity": 2
    }
  ]
}
📈 Output / Alerts

The system generates real-time alerts such as:

SLA_BREACH: order_123
BOTTLENECK_ALERT: warehouse_2
STOCKOUT_RISK: product_456
🧠 Key Learnings
Designed a real-time event-driven architecture
Implemented streaming pipelines using Kafka-compatible Redpanda
Built stateful stream processing logic using PyFlink concepts
Modeled analytical data using dbt
Integrated cloud data warehouse (BigQuery)
🔮 Future Improvements
Add anomaly detection using ML models (BigQuery ML / Vertex AI)
Add real-time dashboarding (Looker / Grafana)
Add schema registry for event contracts
Deploy on Kubernetes for production scaling
👨‍💻 Conclusion

This project demonstrates a production-style real-time data engineering pipeline capable of detecting operational risks in ecommerce systems using streaming architecture.

It showcases:

Event-driven system design
Real-time stream processing
Cloud data warehousing
Modern ELT workflows
🏁 End Result

A complete end-to-end streaming ecommerce intelligence system built with modern data engineering tools and patterns, aligned with real-world production architectures.