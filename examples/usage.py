"""Find a specification and its downstream path in the installed manifest."""

from policy_as_code_governance_pack import load_document_manifest

specification = next(
    row for row in load_document_manifest("spec")
    if row["id"] == "spc:policy-authoring-and-review-contract"
)
assert specification["target_path"] == ".ssot/specs/SPEC-2000-policy-authoring-and-review-contract.yaml"
