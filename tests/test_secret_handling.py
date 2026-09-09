from __future__ import annotations

import json

from piphi_network_philips_hue_direct.schemas import DeviceConfig
from piphi_network_philips_hue_direct.state import _split_config, make_entry


def test_coordinator_token_is_kept_out_of_persisted_and_serialized_config() -> None:
    config = DeviceConfig(id="hue-test", host="http://zigbee.local", coordinator_token="top-secret")

    public, secrets = _split_config(config)
    entry = make_entry(config)

    assert "coordinator_token" not in public
    assert secrets == {"coordinator_token": "top-secret"}
    assert "top-secret" not in json.dumps(entry)
