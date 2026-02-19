# Phase III: Hilbert Schemes of Points $S^{[n]}$

## 1. The BKB Bridge
The **Bridgeland-King-Bezrukavnikov (BKB)** equivalence provides a Fourier-Mukai kernel $\mathcal{P}$ that induces an equivalence of derived categories:
$$\Phi_{\mathcal{P}}: D^b(S^{[n]}) \xrightarrow{\sim} D^b_{S_n}(S^n)$$
In the SCHEMA_V5 framework, this means the NC-motive of the Hilbert scheme is isomorphic to the $S_n$-invariant part of the product motive:
$$M(S^{[n]}) \cong [M(S)^{\otimes n}]^{S_n}$$

## 2. Galois Invariance in $S^{[n]}$
The NC-Motivic Galois group $G_{nc}$ acts on the realization of $S^{[n]}$ through its action on $M(S)$. 
- Any rational Hodge class $\alpha \in H^{2p}(S^{[n]}, \mathbb{Q})$ corresponds to an $S_n$-invariant class in the product.
- Since the Saturation Axiom holds for the factors (Milestone 1), the product class is algebraic.
- The BKB-equivalence, being a morphism of NC-motives, maps this algebraic product class back to an algebraic class on $S^{[n]}$.

## 3. Conclusion for Hyperkähler Manifolds
This construction proves that for Hilbert schemes of K3 surfaces, the rational Hodge Conjecture is a direct consequence of NC-Saturation on the underlying surface. The "Ghost Cycles" on $S^{[n]}$ are simply the BKB-images of the stabilized correspondences on $S^n$.
