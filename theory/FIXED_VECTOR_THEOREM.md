# Proposed Theorem: The Fixed-Vector Criterion

## Status: Conditional Result
This document outlines a **Proposed Theorem** within the SCHEMA_V5 framework. Its validity is contingent upon the existence of a neutral Tannakian category $\mathcal{M}_{nc}$ and its associated Galois group $G_{nc}$, as described in `theory/NC_GALOIS_GROUP.md`.

## Statement of the Proposed Theorem
Let $X$ be a smooth projective variety and $\omega_{nc}(M_X)$ its NC-realization. If $\mathcal{M}_{nc}$ satisfies the properties of a neutral Tannakian category over $\mathbb{Q}$, then a vector $v \in \omega_{nc}(M_X)$ is the image of a $K$-theory class $\alpha \in K_0(X) \otimes \mathbb{Q}$ if and only if $v$ is invariant under the action of the NC-Motivic Galois group $G_{nc}$.

## Proof Strategy (Conditional)
1. **Assumed Duality:** Under the assumption of Tannakian Duality for $\mathcal{M}_{nc}$, the invariant subspace $(\omega_{nc}(M_X))^{G_{nc}}$ is isomorphic to $\text{Hom}_{\mathcal{M}_{nc}}(\mathbf{1}, M_X)$.
2. **Morphism Mapping:** By the construction of morphisms in the NC-category:
   $$\text{Hom}_{\mathcal{M}_{nc}}(\mathbf{1}, M_X) \cong K_0(\mathcal{A}_{pt}^{op} \otimes \mathcal{A}_X) \otimes \mathbb{Q} \cong K_0(X) \otimes \mathbb{Q}$$
3. **Saturation Conclusion:** If these isomorphisms hold, then every $G_{nc}$-invariant vector represents a morphism from the unit motive and is thus algebraic.

## Critical Gaps for Future Proof
- **Faithfulness of $\omega_{nc}$:** It must be shown that the realization functor is fully faithful, or at least that its restriction to the Hodge locus does not create "spurious" invariants.
- **Categorical Completeness:** The proof assumes that all morphisms in $\text{Vect}_{\mathbb{Q}}$ between realizations that commute with the $G_{nc}$ action actually originate from $K_0$.
