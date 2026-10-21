from datetime import datetime, timezone
from time import perf_counter

from fastapi import FastAPI, Request, Response
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST

app = FastAPI(
    title="azure-prj001 API",
    version="0.1.0",
)

REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total number of HTTP requests",
    ["method", "path", "status"],
)

REQUEST_DURATION = Histogram(
    "http_request_duration_seconds",
    "HTTP request duration in seconds",
    ["method", "path"],
)

@app.middleware("http")
async def metrics_middleware(request: Request, call_next):
    start = perf_counter()

    response = await call_next(request)

    duration = perf_counter() - start

    REQUEST_COUNT.labels(
        method=request.method,
        path=request.url.path,
        status=response.status_code,
    ).inc()

    REQUEST_DURATION.labels(
        method=request.method,
        path=request.url.path,
    ).observe(duration)

    return response

@app.get("/")
def root():
    return {
        "service": "azure-prg001",
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

@app.get("/metrics")
def metrics():
    return Response(
        content=generate_latest(),
        media_type=CONTENT_TYPE_LATEST,
    )