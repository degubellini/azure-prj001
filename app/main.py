from datetime import datetime, timezone

from fastapi import FastAPI


app = FastAPI(
    title="azure-lab001 API",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "service": "azure-lab001",
        "version": "0.1.0",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


@app.get("/ready")
def readiness():
    return {
        "status": "ready",
    }


@app.get("/api/v1/orders")
def get_orders():
    return {
        "orders": [
            {
                "id": 1,
                "product": "network-monitoring-service",
                "status": "complete",
            },
            {
                "id": 2,
                "product": "managed-api-service",
                "status": "processing",
            },
        ]
    }
