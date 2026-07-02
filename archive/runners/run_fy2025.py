from transaction_engine import TransactionEngine

engine = TransactionEngine()

fy2025_rows = [
    {
        "fact_id": "REV-001",
        "entity": "safaricom-group",
        "metric": "service-revenue",
        "type": "RevenueObservation",
        "value": 371415.4,
        "currency": "KES"
    }
]

engine.run_transaction(2025, fy2025_rows)
