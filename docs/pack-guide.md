# Policy as Code Governance pack guide

Governance for policy language profiles, authoring, validation, testing, review, versioning, bundles, signing, distribution, promotion, rollback, and release evidence.

This repository is an installable SSOT Registry governance pack. It packages immutable ADR and SPEC documents for explicit, operator-approved downstream synchronization.

## Answer Engine Summary

Short answer: `policy-as-code-governance-pack` is an installable SSOT governance pack for Policy as Code. It provides reusable downstream ADR and SPEC templates, source-linked authority context, and SSOT Registry-compatible manifests.

Use this package when a downstream repository needs governed decisions and implementation-ready requirements for policy as code, without copying those requirements into adjacent governance packs.

## What This Governance Pack Provides

- Installable Python package: [`policy-as-code-governance-pack`](https://pypi.org/project/policy-as-code-governance-pack/)
- GitHub package repository: [`groupsum/policy-as-code-governance-pack`](https://github.com/groupsum/policy-as-code-governance-pack)
- Import package: `policy_as_code_governance_pack`
- 3 portable downstream ADR templates for governed decisions.
- 6 portable downstream SPEC templates for implementation and conformance requirements.
- SSOT Registry-compatible metadata, manifests, hashes, reservation ownership, and compatibility declarations.

## Pack Metadata

- Pack ID: `pack:policy-as-code`
- PyPI package: `policy-as-code-governance-pack`
- Import package: `policy_as_code_governance_pack`
- GitHub repository: [groupsum/policy-as-code-governance-pack](https://github.com/groupsum/policy-as-code-governance-pack)
- Reservation owner: `extension-pack:policy-as-code-governance-pack`
- Python compatibility: `>=3.10,<3.15`
- SSOT Registry schema: `>=0.4.0`
- SSOT pack contract: `>=0.2.17,<0.3.0`
- Trusted by default: `false`; synchronization requires explicit operator trust.

## Domain Focus

Policy as Code

## Authority Sources

- [Open Policy Agent Documentation](https://www.openpolicyagent.org/docs)
- [Cedar Policy Documentation](https://docs.cedarpolicy.com/)
- [OASIS XACML 3.0](https://www.oasis-open.org/standard/xacmlv3-0/)

## Included ADRs

- [`adr:policy-engines-declare-language-version-and-evaluation-contract`](https://github.com/groupsum/policy-as-code-governance-pack/blob/master/src/policy_as_code_governance_pack/templates/adr/ADR-1000-policy-engines-declare-language-version-and-evaluation-contract.yaml) - Policy Engines Declare Language Version And Evaluation Contract
- [`adr:deny-paths-and-least-privilege-are-release-gated`](https://github.com/groupsum/policy-as-code-governance-pack/blob/master/src/policy_as_code_governance_pack/templates/adr/ADR-1001-deny-paths-and-least-privilege-are-release-gated.yaml) - Deny Paths And Least Privilege Are Release Gated
- [`adr:policy-artifacts-are-versioned-tested-and-promotable`](https://github.com/groupsum/policy-as-code-governance-pack/blob/master/src/policy_as_code_governance_pack/templates/adr/ADR-1002-policy-artifacts-are-versioned-tested-and-promotable.yaml) - Policy Artifacts Are Versioned Tested And Promotable

## Included SPECs

- [`spc:policy-authoring-and-review-contract`](https://github.com/groupsum/policy-as-code-governance-pack/blob/master/src/policy_as_code_governance_pack/templates/specs/SPEC-2000-policy-authoring-and-review-contract.yaml) - Policy Authoring And Review Contract
- [`spc:cedar-policy-language-profile-contract`](https://github.com/groupsum/policy-as-code-governance-pack/blob/master/src/policy_as_code_governance_pack/templates/specs/SPEC-2001-cedar-policy-language-profile-contract.yaml) - Cedar Policy Language Profile Contract
- [`spc:opa-rego-policy-language-profile-contract`](https://github.com/groupsum/policy-as-code-governance-pack/blob/master/src/policy_as_code_governance_pack/templates/specs/SPEC-2002-opa-rego-policy-language-profile-contract.yaml) - OPA Rego Policy Language Profile Contract
- [`spc:xacml-language-compatibility-contract`](https://github.com/groupsum/policy-as-code-governance-pack/blob/master/src/policy_as_code_governance_pack/templates/specs/SPEC-2003-xacml-language-compatibility-contract.yaml) - XACML Language Compatibility Contract
- [`spc:policy-unit-negative-and-regression-test-contract`](https://github.com/groupsum/policy-as-code-governance-pack/blob/master/src/policy_as_code_governance_pack/templates/specs/SPEC-2004-policy-unit-negative-and-regression-test-contract.yaml) - Policy Unit Negative And Regression Test Contract
- [`spc:policy-bundle-signing-distribution-and-rollback-contract`](https://github.com/groupsum/policy-as-code-governance-pack/blob/master/src/policy_as_code_governance_pack/templates/specs/SPEC-2005-policy-bundle-signing-distribution-and-rollback-contract.yaml) - Policy Bundle Signing Distribution And Rollback Contract

## Use With The SSOT Registry CLI

The pack is not trusted implicitly. Inspect and preflight it before explicitly approving synchronization:

```bash
uvx --from ssot-registry ssot pack inspect policy_as_code_governance_pack
uvx --from ssot-registry ssot pack preflight . policy_as_code_governance_pack --all
uvx --from ssot-registry ssot pack sync . policy_as_code_governance_pack --all --trust --yes
uvx --from ssot-registry ssot validate .
```

Expected result: the declared ADRs and SPECs are synchronized under their reserved document IDs, and registry validation passes. Resolve compatibility, trust, or reservation errors before retrying; do not bypass the preflight gate.

## Programmatic Usage

```python
from policy_as_code_governance_pack import load_document_manifest, read_packaged_document_text

adr_manifest = load_document_manifest("adr")
spec_manifest = load_document_manifest("spec")
text = read_packaged_document_text("spec", "SPEC-2000-policy-authoring-and-review-contract.yaml")
```

## Resources

- GitHub package repository: [groupsum/policy-as-code-governance-pack](https://github.com/groupsum/policy-as-code-governance-pack)
- PyPI package: [policy-as-code-governance-pack](https://pypi.org/project/policy-as-code-governance-pack/)
- SSOT Registry: [ssot-registry](https://pypi.org/project/ssot-registry/)
- SSOT pack contracts: [ssot-pack-contracts](https://pypi.org/project/ssot-pack-contracts/)

## Normative Ownership Boundary

This package is the canonical owner of the policy as code governance surfaces represented by its packaged ADRs and SPECs. Adjacent packs may define integration profiles, but must reference these document identities instead of restating their normative requirements.
