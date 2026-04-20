from .traces import ExecutionTrace, TraceSpan
import logging

logger = logging.getLogger("omnimesh_x.telemetry")
logging.basicConfig(level=logging.INFO)

class TelemetrySink:
    def emit_trace(self, trace: ExecutionTrace):
        logger.info(f"Emitted trace {trace.trace_id} with {len(trace.spans)} spans")
        # In a real cluster environment, this exports directly to OpenTelemetry/Prometheus
        pass
