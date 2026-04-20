from fastapi import APIRouter, Request
import hmac, hashlib, base64, json, os
from app.producer import publish

router = APIRouter()

SECRET = os.getenv("SHOPIFY_SECRET", "test")


def verify(body, header):
    digest = hmac.new(SECRET.encode(), body, hashlib.sha256).digest()
    return hmac.compare_digest(base64.b64encode(digest).decode(), header)


@router.post("/shopify")
async def shopify_webhook(request: Request):
    body = await request.body()

    if not verify(body, request.headers.get("X-Shopify-Hmac-Sha256", "")):
        return {"error": "invalid signature"}

    topic = request.headers.get("X-Shopify-Topic")
    payload = json.loads(body)

    event = normalize(topic, payload)

    publish(event)

    return {"status": "ok"}


def normalize(topic, p):
    if "orders" in topic:
        return {
            "type": "order",
            "order_id": str(p["id"]),
            "created_at": p["created_at"],
            "amount": float(p.get("total_price", 0)),
            "items": len(p.get("line_items", []))
        }

    if "fulfillments" in topic:
        return {
            "type": "fulfillment",
            "order_id": str(p["order_id"]),
            "status": p["status"],
            "updated_at": p["updated_at"]
        }

    if "inventory" in topic:
        return {
            "type": "inventory",
            "product_id": str(p["inventory_item_id"]),
            "qty": p["available"]
        }

    return {"type": "unknown"}