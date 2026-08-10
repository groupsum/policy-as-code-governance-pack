# policy-as-code-governance-pack

Governance for policy language profiles, authoring, validation, testing, review, versioning, bundles, signing, distribution, promotion, rollback, and release evidence.

## Package identity

- Pack ID: `pack:policy-as-code`
- PyPI distribution: `policy-as-code-governance-pack`
- Python import: `policy_as_code_governance_pack`
- Reservation owner: `extension-pack:policy-as-code-governance-pack`

## Normative ownership

This package is the canonical owner of the governance surfaces represented by its packaged ADRs and SPECs. Adjacent governance packs reference these documents rather than restating their requirements.

## Install

```bash
uv add policy-as-code-governance-pack
uv run ssot pack sync . policy_as_code_governance_pack --all --trust --yes
uv run ssot validate .
```

## Authority sources

- https://www.openpolicyagent.org/docs
- https://docs.cedarpolicy.com/
- https://www.oasis-open.org/standard/xacmlv3-0/
