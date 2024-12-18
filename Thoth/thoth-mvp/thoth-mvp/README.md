# Thoth MVP
## Project Overview
Thoth is a secure communication system designed for offline, decentralized, and encrypted messaging.

## MVP Features
1. Peer discovery
2. Message routing
3. End-to-end encryption
4. Resilience to node disconnections

## Directory Structure
```
thoth-mvp/
├── src/
│   ├── discovery.py        # Peer discovery logic
│   ├── communication.py    # Messaging and encryption
│   ├── routing.py          # Message routing logic
│   ├── resilience.py       # Failure handling
│   └── main.py             # Entry point
├── tests/
│   ├── test_discovery.py
│   ├── test_communication.py
│   └── test_routing.py
├── requirements.txt        # Dependencies
└── README.md               # Project documentation
```

## How to Run
1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Run the main script:
   ```
   python src/main.py
   ```
