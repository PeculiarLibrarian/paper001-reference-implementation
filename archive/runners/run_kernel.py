from meta.semantic_kernel_runtime import SemanticKernelRuntime

kernel = SemanticKernelRuntime()

# Example execution hook (replace with real seed)
kernel.execute_transaction(
    fy=2025,
    seed_rows=[
        {"metric": "revenue", "entity": "safaricom-group", "value": 371.42},
        {"metric": "mpesa", "entity": "kenya", "value": 161.13}
    ]
)
