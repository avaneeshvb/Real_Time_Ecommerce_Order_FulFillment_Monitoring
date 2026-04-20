def inventory_risk(event_str):
    import json
    e = json.loads(event_str)

    if e["type"] == "inventory":
        if e["qty"] < 5:
            print("STOCKOUT_RISK", e["product_id"])