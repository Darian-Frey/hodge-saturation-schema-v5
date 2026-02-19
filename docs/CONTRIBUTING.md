# Contributing to Hodge Saturation (SCHEMA_V5)

This repository operates under the **SCHEMA_V5 Protocol**. All contributors (Human or AI) must adhere to the following standards to ensure mathematical and state integrity.

## 1. Operational Directives
- **State Preservation:** Every significant addition must advance the `STATE_V2` identifier.
- **D_TASK Batches:** Reasoning should be structured into discrete batches (`D_TASK`) to allow for multi-agent cross-verification.
- **Source of Truth:** The `theory/` and `geometry/` folders are the immutable references. Changes here require a "Recovery Node" analysis.

## 2. Mathematical Standards
- **Rational Focus:** We work primarily over $\mathbb{Q}$. Integral/Torsion issues should be relegated to the **Modified Hodge Proxy** layer.
- **O-minimal Bounds:** Any proposed lifting mechanism must explicitly check for o-minimal definability to prevent "transcendental leakage."
- **Tannakian Consistency:** Theoretical enhancements must be compatible with the NC-Motivic Galois group {nc}$ action.

## 3. Pull Request (PR) Requirements
1. **Reference Pointers:** Use `REF_ID` to link new developments to existing reasoning nodes.
2. **Symbolic Verification:** If applicable, update `tools/ghost_cycle_tracker.py` to reflect new logic.
3. **Capsule Integrity:** Ensure the "Summary Capsule" at the end of the PR remains consistent with the global solution sketch.

## 4. Multi-Agent Collaboration
When working with Copilot or other AI agents:
- Pass the **SCHEMA_V5 Bootloader** payload in the first prompt.
- Cross-check "Hallucination Drifts" by comparing results against the O-minimal anchors in this repo.
