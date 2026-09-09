from __future__ import annotations

from typing import Any

ENDPOINTS = {
    "health": "/health",
    "diagnostics": "/diagnostics",
    "discover": "/discover",
    "entities": "/entities",
    "state": "/state",
    "config": "/config",
    "config_sync": "/config/sync",
    "deconfigure": "/deconfigure",
    "ui_config": "/ui-config",
    "events": "/events",
    "command": "/command",
}

REQUIRED_ENDPOINTS = ["health", "entities", "command", "config", "ui_config"]

CAPABILITIES: dict[str, dict[str, Any]] = {
    "connected": {"kind": "sensor", "unit": "bool"},
    "refresh": {"kind": "action"},
}

COMMANDS: dict[str, dict[str, Any]] = {
    "refresh": {
        "description": "Refresh the integration state.",
        "timeout_ms": 5000,
    },
}

CONFIG_SCHEMA: dict[str, Any] = {
    "schema": {
        "title": "PiPhi Network Philips Hue Direct Setup",
        "type": "object",
        "required": ["host"],
        "properties": {
    "host": {
        "type": "string",
        "title": "Coordinator Runtime URL"
    },
    "alias": {
        "type": "string",
        "title": "Profile Name"
    },
    "coordinator_token": {
        "type": "string",
        "title": "Coordinator Token",
        "format": "password",
        "writeOnly": True
    },
    "network_id": {
        "type": "string",
        "title": "Zigbee Network ID"
    },
    "actions_enabled": {
        "type": "boolean",
        "title": "Enable Light Actions",
        "default": False
    },
    "allowlisted_ieee_addresses": {
        "type": "array",
        "title": "Allowed IEEE Addresses",
        "items": {
            "type": "string"
        },
        "default": []
    }
},
    },
    "uiSchema": {
        "host": {"placeholder": "http://piphi-zigbee:8090"},
        "alias": {"placeholder": "Philips Hue Zigbee Device"},
    },
}

FALLBACK_ENTITY: dict[str, Any] = {
    "id": "hue-zigbee-device",
    "name": "Philips Hue Zigbee Device",
    "device_id": "hue-zigbee-device",
    "entity_type": "zigbee_hue_device",
    "capabilities": ["connected", "refresh"],
    "available_commands": [
        {"id": "refresh", "label": "Refresh", "kind": "action"},
    ],
    "dashboard": {
        "allowed_widgets": [
    "light-card",
    "scene-card",
    "battery-fleet-card",
    "tile"
],
        "default_widget": "light-card",
    },
}
