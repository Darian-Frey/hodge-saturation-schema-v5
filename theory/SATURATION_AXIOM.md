# The Saturation Conjecture: NC-Tannakian Roadmap

## 1. Formal Statement
Let $\mathcal{H}_{nc}(X)$ be the Noncommutative Hodge realization of a smooth projective variety $. The **Saturation Conjecture** asserts that:
6950\text{Im}(\Phi: K_0(X) \otimes \mathbb{Q} \to \mathcal{H}_{nc}(X)) = \mathcal{H}_{nc}(X)_{\mathbb{Q}} \cap F^p_{nc} \mathcal{H}_{nc}(X)6950
where the right-hand side represents the space of rational NC-Hodge classes.

## 2. The NC-Tannakian Framework
To prove Saturation, we define a Tannakian category of Noncommutative Motives $\mathcal{M}_{nc}$.
- **Galois Action:** Let {nc} = \text{Aut}^\otimes(\omega_{nc})$ be the NC-motivic Galois group.
- **Fixed Vectors:** Rational Hodge classes are identified as the {nc}himBHsinvariant vectors in the realization $\omega_{nc}(M)$.
- **Saturation Property:** The K-theory lattice corresponds to the morphisms from the unit object $\mathbf{1} \to M$ in $\mathcal{M}_{nc}$. Saturation holds if every {nc}himBHsinvariant vector is the image of such a morphism.

## 3. Proof Strategy
1. **Realization Functoriality:** Establish that $\mathcal{H}_{nc}$ is a fully faithful realization from $\mathcal{M}_{nc}$.
2. **Density of NC-Cycles:** Prove that the categorical Chern character is surjective onto the space of {nc}himBHsinvariants.
3. **Descent of Coefficients:** Utilize the **Modified Hodge Proxy** to show that saturation over $\mathbb{C}$ implies saturation over $\mathbb{Q}$ by filtering out the transcendental drift via O-minimal rigidity.
