from __future__ import annotations

from pydantic import Field
from piphi_runtime_kit_python import RuntimeConfig


class DeviceConfig(RuntimeConfig):
    host: str
    alias: str | None = None
    coordinator_token: str | None = None
    network_id: str | None = None
    actions_enabled: bool = False
    allowlisted_ieee_addresses: list[str] = Field(default_factory=list)
