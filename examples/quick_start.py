"""Inspect the installed pack identity."""

from policy_as_code_governance_pack import load_pack_metadata

metadata = load_pack_metadata()
assert metadata["origin"]["id"] == "pack:policy-as-code"
print(metadata["origin"]["id"])
