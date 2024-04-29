# Prerequisites

- Docker
- Docker compose
- Python 3.12

# Start

```bash
docker compose up --build; docker compose down
```

# Run tests
```bash
cd src
python3 -m unittest test_utils.py
```