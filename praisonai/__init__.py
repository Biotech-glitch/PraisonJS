from .cli import PraisonAI
from .version import __version__

def configure_telemetry():
    """Configure telemetry settings to disable OpenTelemetry SDK."""
    import os
    os.environ["OTEL_SDK_DISABLED"] = "true"
    os.environ["EC_TELEMETRY"] = "false"
