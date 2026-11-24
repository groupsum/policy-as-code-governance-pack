"""Resolve and read a packaged specification without synchronizing it."""

from policy_as_code_governance_pack import load_document_manifest, read_packaged_document_text

spec = next(row for row in load_document_manifest("spec") if row["id"] == "spc:policy-authoring-and-review-contract")
document = read_packaged_document_text("spec", spec["filename"])
assert spec["id"] in document
