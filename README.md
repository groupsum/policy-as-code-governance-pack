# policy-as-code-governance-pack

<!-- readme-standards:begin branding -->
<p align="center"><a href="https://github.com/groupsum/readme-standards"><img src="https://raw.githubusercontent.com/groupsum/readme-standards/master/docs/assets/readme-standards.svg" alt="Groupsum README Standards" width="300"></a></p>
<p align="center"><strong>policy-as-code-governance-pack</strong></p>
<p align="center">Governance for policy language profiles, authoring, validation, testing, review, versioning, bundles, signing, distribution, promotion, rollback, and release evidence.</p>
<p align="center">
<a href="https://pypi.org/project/policy-as-code-governance-pack/"><img alt="pypi: policy-as-code-governance-pack" src="https://img.shields.io/pypi/v/policy-as-code-governance-pack?labelColor=1E293B&amp;color=1D4ED8"></a>
<a href="https://github.com/groupsum/policy-as-code-governance-pack/blob/master/pyproject.toml"><img alt="Source version: 0.1.0.dev2" src="https://img.shields.io/static/v1?label=Source%20version&amp;message=0.1.0.dev2&amp;labelColor=1E293B&amp;color=4338CA"></a>
<a href="https://github.com/groupsum/policy-as-code-governance-pack/blob/master/pyproject.toml"><img alt="Python: &gt;=3.10,&lt;3.15" src="https://img.shields.io/static/v1?label=Python&amp;message=%3E%3D3.10%2C%3C3.15&amp;labelColor=1E293B&amp;color=0F766E"></a>
<a href="https://github.com/groupsum/policy-as-code-governance-pack/blob/master/pyproject.toml"><img alt="Layer: governance" src="https://img.shields.io/static/v1?label=Layer&amp;message=governance&amp;labelColor=1E293B&amp;color=6D28D9"></a>
<a href="https://github.com/groupsum/policy-as-code-governance-pack/blob/master/README.md#lifecycle-and-migration"><img alt="Lifecycle: active" src="https://img.shields.io/static/v1?label=Lifecycle&amp;message=active&amp;labelColor=1E293B&amp;color=166534"></a>
<a href="https://github.com/groupsum/policy-as-code-governance-pack/blob/master/LICENSE"><img alt="License: Apache-2.0" src="https://img.shields.io/static/v1?label=License&amp;message=Apache-2.0&amp;labelColor=1E293B&amp;color=86198F"></a>
<a href="https://github.com/groupsum/policy-as-code-governance-pack/blob/master/README.md#notices"><img alt="Notice: not required" src="https://img.shields.io/static/v1?label=Notice&amp;message=not%20required&amp;labelColor=1E293B&amp;color=475569"></a>
</p>
<p align="center">
<a href="https://pypi.org/project/policy-as-code-governance-pack/"><img alt="Monthly PyPI downloads: policy-as-code-governance-pack" src="https://img.shields.io/pypi/dm/policy-as-code-governance-pack?labelColor=1E293B&amp;color=0E7490"></a>
<a href="https://github.com/groupsum/policy-as-code-governance-pack/blob/master/README.md"><img alt="README hits: policy-as-code-governance-pack" src="https://hits.sh/github.com/groupsum/policy-as-code-governance-pack/README.md.svg?label=README%20hits&amp;labelColor=1E293B&amp;color=0E7490"></a>
</p>
<p align="center">
<a href="https://github.com/groupsum/policy-as-code-governance-pack/actions/workflows/readme-standards.yml"><img alt="README standards: CI gate" src="https://img.shields.io/static/v1?label=README%20standards&amp;message=CI%20gate&amp;labelColor=1E293B&amp;color=1D4ED8"></a>
<a href="https://github.com/groupsum/policy-as-code-governance-pack/actions/workflows/readme-standards.yml"><img alt="Tests: package and example checks" src="https://img.shields.io/static/v1?label=Tests&amp;message=package%20and%20example%20checks&amp;labelColor=1E293B&amp;color=0F766E"></a>
<a href="https://github.com/groupsum/policy-as-code-governance-pack/blob/master/README.md#certification-status"><img alt="Certification: not certified" src="https://img.shields.io/static/v1?label=Certification&amp;message=not%20certified&amp;labelColor=1E293B&amp;color=92400E"></a>
<a href="https://github.com/groupsum/policy-as-code-governance-pack/blob/master/docs/governance/pack-authoring-guide.md"><img alt="Governance: pack governance" src="https://img.shields.io/static/v1?label=Governance&amp;message=pack%20governance&amp;labelColor=1E293B&amp;color=4338CA"></a>
<a href="https://github.com/groupsum/policy-as-code-governance-pack/actions/workflows/readme-standards.yml"><img alt="Evidence: README and wheel checks" src="https://img.shields.io/static/v1?label=Evidence&amp;message=README%20and%20wheel%20checks&amp;labelColor=1E293B&amp;color=6D28D9"></a>
</p>
<p align="center"><a href="#overview">Overview</a> · <a href="#installation">Installation</a> · <a href="#quick-start">Quick Start</a> · <a href="#usage">Usage</a> · <a href="#public-api-and-import-surfaces">API</a> · <a href="#contributing">Contributing</a> · <a href="#governance">Governance</a> · <a href="#license">License</a></p>
<!-- readme-standards:end branding -->

---

## Overview

### Summary

Governance for policy language profiles, authoring, validation, testing, review, versioning, bundles, signing, distribution, promotion, rollback, and release evidence.

### Why This Package

Use this package when a downstream repository needs governed decisions and implementation-ready requirements for policy as code, without copying those requirements into adjacent governance packs.

### When to Use

Use this pack when a downstream SSOT Registry needs reusable decisions and requirements for Policy as Code Governance.

### Features

**Included ADRs**

- [`adr:policy-engines-declare-language-version-and-evaluation-contract`](https://github.com/groupsum/policy-as-code-governance-pack/blob/master/src/policy_as_code_governance_pack/templates/adr/ADR-1000-policy-engines-declare-language-version-and-evaluation-contract.yaml) — Policy Engines Declare Language Version And Evaluation Contract
- [`adr:deny-paths-and-least-privilege-are-release-gated`](https://github.com/groupsum/policy-as-code-governance-pack/blob/master/src/policy_as_code_governance_pack/templates/adr/ADR-1001-deny-paths-and-least-privilege-are-release-gated.yaml) — Deny Paths And Least Privilege Are Release Gated
- [`adr:policy-artifacts-are-versioned-tested-and-promotable`](https://github.com/groupsum/policy-as-code-governance-pack/blob/master/src/policy_as_code_governance_pack/templates/adr/ADR-1002-policy-artifacts-are-versioned-tested-and-promotable.yaml) — Policy Artifacts Are Versioned Tested And Promotable

**Included SPECs**

- [`spc:policy-authoring-and-review-contract`](https://github.com/groupsum/policy-as-code-governance-pack/blob/master/src/policy_as_code_governance_pack/templates/specs/SPEC-2000-policy-authoring-and-review-contract.yaml) — Policy Authoring And Review Contract
- [`spc:cedar-policy-language-profile-contract`](https://github.com/groupsum/policy-as-code-governance-pack/blob/master/src/policy_as_code_governance_pack/templates/specs/SPEC-2001-cedar-policy-language-profile-contract.yaml) — Cedar Policy Language Profile Contract
- [`spc:opa-rego-policy-language-profile-contract`](https://github.com/groupsum/policy-as-code-governance-pack/blob/master/src/policy_as_code_governance_pack/templates/specs/SPEC-2002-opa-rego-policy-language-profile-contract.yaml) — OPA Rego Policy Language Profile Contract
- [`spc:xacml-language-compatibility-contract`](https://github.com/groupsum/policy-as-code-governance-pack/blob/master/src/policy_as_code_governance_pack/templates/specs/SPEC-2003-xacml-language-compatibility-contract.yaml) — XACML Language Compatibility Contract
- [`spc:policy-unit-negative-and-regression-test-contract`](https://github.com/groupsum/policy-as-code-governance-pack/blob/master/src/policy_as_code_governance_pack/templates/specs/SPEC-2004-policy-unit-negative-and-regression-test-contract.yaml) — Policy Unit Negative And Regression Test Contract
- [`spc:policy-bundle-signing-distribution-and-rollback-contract`](https://github.com/groupsum/policy-as-code-governance-pack/blob/master/src/policy_as_code_governance_pack/templates/specs/SPEC-2005-policy-bundle-signing-distribution-and-rollback-contract.yaml) — Policy Bundle Signing Distribution And Rollback Contract

### Non-Goals

The pack supplies governance records. A downstream application implements the controls and collects its own conformance evidence.

---

## Getting Started

### Prerequisites

Use Python `>=3.10,<3.15`. Downstream synchronization also requires SSOT Registry and permission to write the target registry.

### Installation

For a reproducible install of the [first PyPI prerelease](https://pypi.org/project/policy-as-code-governance-pack/0.1.0.dev2/), use `python -m pip install policy-as-code-governance-pack==0.1.0.dev2`.

#### uv

<!-- readme-standards:begin installation.uv -->
```bash
uv add policy-as-code-governance-pack
```
<!-- readme-standards:end installation.uv -->

#### pip

<!-- readme-standards:begin installation.pip -->
```bash
python -m pip install policy-as-code-governance-pack
```
<!-- readme-standards:end installation.pip -->

#### Poetry

<!-- readme-standards:begin installation.poetry -->
```bash
poetry add policy-as-code-governance-pack
```
<!-- readme-standards:end installation.poetry -->

### Quick Start

#### Example

<!-- readme-standards:begin example.quick-start -->
Source: [examples/quick_start.py](https://github.com/groupsum/policy-as-code-governance-pack/blob/master/examples/quick_start.py).

```python
"""Inspect the installed pack identity."""

from policy_as_code_governance_pack import load_pack_metadata

metadata = load_pack_metadata()
assert metadata["origin"]["id"] == "pack:policy-as-code"
print(metadata["origin"]["id"])
```
<!-- readme-standards:end example.quick-start -->

#### Expected Result

The script prints `pack:policy-as-code` from the installed pack metadata.

---

## Usage

### Common Workflows

<!-- readme-standards:begin example.usage -->
Source: [examples/usage.py](https://github.com/groupsum/policy-as-code-governance-pack/blob/master/examples/usage.py).

```python
"""Find a specification and its downstream path in the installed manifest."""

from policy_as_code_governance_pack import load_document_manifest

specification = next(
    row for row in load_document_manifest("spec")
    if row["id"] == "spc:policy-authoring-and-review-contract"
)
assert specification["target_path"] == ".ssot/specs/SPEC-2000-policy-authoring-and-review-contract.yaml"
```
<!-- readme-standards:end example.usage -->

Use the downstream environment that has both SSOT Registry and `policy-as-code-governance-pack` installed. Inspect the pack and preflight the target registry before approving synchronization.

```bash
uv run ssot pack inspect policy_as_code_governance_pack
uv run ssot pack preflight . policy_as_code_governance_pack --all
uv run ssot pack sync . policy_as_code_governance_pack --all --trust --yes
uv run ssot validate .
```

### Configuration

Select the installed import package `policy_as_code_governance_pack` in SSOT Registry. Review reservation owner `extension-pack:policy-as-code-governance-pack` and the target's trust policy before syncing.

### Error Handling

If preflight reports a schema, trust, or document-number conflict, resolve it in the target registry and repeat preflight before synchronization.

### Best Practices

Pin the pack version in downstream projects. Reference document IDs in local governance and inspect the change set before granting trust.

---

## Package Boundary

### What It Owns

This package is the canonical owner of the policy as code governance surfaces represented by its packaged ADRs and SPECs. Adjacent packs may define integration profiles, but must reference these document identities instead of restating their normative requirements.

### Public API and Import Surfaces

Import `load_pack_metadata`, `load_document_manifest`, and `read_packaged_document_text` from `policy_as_code_governance_pack` to inspect packaged records.

### Entry Points

<!-- readme-standards:begin entry-points -->
This package declares no command-line, GUI, or plugin entry points in its manifest.
<!-- readme-standards:end entry-points -->

### Injected Dependencies

The package binds its metadata and document loaders through `ssot-pack-contracts`. The caller supplies the target registry to SSOT Registry when synchronizing.

### Protocol Consumers

SSOT Registry uses the pack metadata, document manifests, and bundled templates during inspect, preflight, and sync.

### Extensions

Define downstream policies as local records and reference the pack's document IDs. Send proposed changes to the canonical pack through repository review.

---

## Operations and Readiness

### Operational Requirements

Local inspection reads installed package resources. Synchronization requires an initialized downstream registry and explicit operator approval.

### Health and Observability

Review the preflight and sync output, then use `ssot validate` to check the resulting registry.

### Security and Resource Limits

Implicit trust is disabled. Review the exact distribution, version, records, and reserved IDs before enabling trust in a target registry.

### Compatibility

- Python `>=3.10,<3.15`
- SSOT Registry schema `>=0.4.0`
- SSOT pack contracts `>=0.2.17,<0.3.0`

---

## Verification

### Tests

Run `python -m unittest discover -s tests -v` with the pack installed. The [README workflow](https://github.com/groupsum/policy-as-code-governance-pack/actions/workflows/readme-standards.yml) checks the source README and runs both examples against an installed wheel.

### Certification Status

The pack has no external certification. Downstream adoption requires evidence for the controls an application implements.

### Evidence

See the [README workflow](https://github.com/groupsum/policy-as-code-governance-pack/actions/workflows/readme-standards.yml) for package and documentation verification and the [packaged records](https://github.com/groupsum/policy-as-code-governance-pack/blob/master/src/policy_as_code_governance_pack/templates) for document-level sources.

---

## FAQ

### Why

**Why do document IDs matter?** Downstream records use them to trace an adopted decision or requirement to the pack that owns it.

### How

**How do I preview changes?** Use the registry's pack preflight before approving a sync.

### When

**When should I upgrade?** Read the changelog and preflight the new version against the target registry before applying it.

---

## Documentation and Related Packages

### More Documentation

See the [Pack guide](https://github.com/groupsum/policy-as-code-governance-pack/blob/master/docs/pack-guide.md), [changelog](https://github.com/groupsum/policy-as-code-governance-pack/blob/master/CHANGELOG.md), and [pack metadata](https://github.com/groupsum/policy-as-code-governance-pack/blob/master/src/policy_as_code_governance_pack/metadata.json).

### Related Packages

[SSOT Registry](https://pypi.org/project/ssot-registry/) manages downstream registries. [SSOT Pack Contracts](https://pypi.org/project/ssot-pack-contracts/) provides the shared pack interface.

### Project Links

<!-- readme-standards:begin project-links -->
- [Homepage](https://github.com/groupsum/policy-as-code-governance-pack)
- [Issues](https://github.com/groupsum/policy-as-code-governance-pack/issues)
- [Repository](https://github.com/groupsum/policy-as-code-governance-pack)
- [pypi: policy-as-code-governance-pack](https://pypi.org/project/policy-as-code-governance-pack/)
<!-- readme-standards:end project-links -->

---

## Contributing

### How to Contribute

Open an [issue](https://github.com/groupsum/policy-as-code-governance-pack/issues) or pull request describing the affected records, their authority, and the expected downstream effect.

### Development Setup

Install the checkout with `python -m pip install -e .`, then run `python -m unittest discover -s tests -v`. On Python 3.11 or newer, run `uvx --from readme-standards==0.1.3 readme-standards check`.

### Notes for Maintainers

Keep source links, document identifiers, and committed manifest hashes aligned. Run `uvx --from readme-standards==0.1.3 readme-standards render --write` after changing generated README inputs.

---

## Governance

### Ownership and Decision Making

Groupsum maintains `pack:policy-as-code`. The pack's reservation owner is `extension-pack:policy-as-code-governance-pack`. Downstream registry operators approve synchronization.

### Standards and Policies

**Authority Sources**

- [Open Policy Agent Documentation](https://www.openpolicyagent.org/docs)
- [Cedar Policy Documentation](https://docs.cedarpolicy.com/)
- [OASIS XACML 3.0](https://www.oasis-open.org/standard/xacmlv3-0/)

### Lifecycle and Migration

Review [release changes](https://github.com/groupsum/policy-as-code-governance-pack/blob/master/CHANGELOG.md) and preflight the chosen version against each downstream registry.

---

## License and Attribution

### License

<!-- readme-standards:begin license -->
Licensed under `Apache-2.0`. See [LICENSE](https://github.com/groupsum/policy-as-code-governance-pack/blob/master/LICENSE).
<!-- readme-standards:end license -->

### Notices

<!-- readme-standards:begin notices -->
No separate NOTICE file is declared. Review the license and bundled third-party attributions.
<!-- readme-standards:end notices -->
