import pandas as pd


# =========================
# CSV METRICS PARSER
# =========================
def parse_metrics(file_path):
    """Parse performance metrics CSV file and aggregate by endpoint."""
    df = pd.read_csv(file_path)

    grouped = df.groupby(["Endpoint"]).agg({
        "P95(ms)": "mean",
        "P99(ms)": "mean",
        "TPS": "mean",
        "ErrorRate(%)": "mean"
    }).reset_index()

    return grouped.to_dict(orient="records")


# =========================
# INFRASTRUCTURE METRICS
# =========================
def parse_infra(file_path):
    """Parse infrastructure metrics CSV file and aggregate by service."""
    df = pd.read_csv(file_path)

    grouped = df.groupby("Service").agg({
        "CPUUtilization(%)": "max",
        "MemoryUtilization(%)": "max",
        "RequestsPerSecond": "max",
        "P95Latency(ms)": "max",
        "HTTP5xxErrors": "sum"
    }).reset_index()

    return grouped.to_dict(orient="records")


# =========================
# WORKLOAD PROFILE
# =========================
def parse_workload(file_path):
    """Parse workload profile CSV file to get user journey distribution."""
    df = pd.read_csv(file_path)

    return {
        row["UserJourney"].lower().replace(" ", "_"): row["PercentageOfUsers"]
        for _, row in df.iterrows()
    }

