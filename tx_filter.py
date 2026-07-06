# Filter high-value transactions from a simulated batch
transactions = [
    {"tx_id": "0x1", "amount": 500},
    {"tx_id": "0x2", "amount": 15000},
    {"tx_id": "0x3", "amount": 45000},
    {"tx_id": "0x4", "amount": 200}
]

# Set whale alert threshold at 10,000 units
whale_threshold = 10000
whale_txs = [tx for tx in transactions if tx["amount"] >= whale_threshold]

print(f"Detected {len(whale_txs)} large transactions:")
for tx in whale_txs:
    print(f"ID: {tx['tx_id']} | Volume: {tx['amount']}")
