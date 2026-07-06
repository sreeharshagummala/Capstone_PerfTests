import yaml


# =========================
# OPENAPI PARSER (YAML)
# =========================
def parse_openapi(file_path):
    """Parse OpenAPI specification file and extract endpoints."""
    with open(file_path, "r") as f:
        spec = yaml.safe_load(f)

    endpoints = []

    for path, methods in spec.get("paths", {}).items():
        for method, details in methods.items():
            endpoints.append({
                "path": path,
                "method": method.upper(),
                "summary": details.get("summary", ""),
                "auth": "security" in details
            })

    return endpoints


# =========================
# DEPLOYMENT YAML PARSER
# =========================
def parse_deployment(file_path):
    """Parse Kubernetes deployment YAML file and extract service configurations."""
    with open(file_path, "r") as f:
        docs = list(yaml.safe_load_all(f))

    services = []

    for doc in docs:
        if not doc:
            continue

        metadata = doc.get("metadata", {})
        spec = doc.get("spec", {})
        template = spec.get("template", {})
        container = template.get("spec", {}).get("containers", [{}])[0]

        resources = container.get("resources", {})

        services.append({
            "service": metadata.get("name"),
            "replicas": spec.get("replicas"),
            "cpu_request": resources.get("requests", {}).get("cpu"),
            "memory_request": resources.get("requests", {}).get("memory"),
            "cpu_limit": resources.get("limits", {}).get("cpu"),
            "memory_limit": resources.get("limits", {}).get("memory"),
        })

    return services

