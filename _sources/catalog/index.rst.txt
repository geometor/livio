:navigation: header
:order: 1
:type: book
:nav_title: Mathematical Catalog
:breadcrumb_title: Mathematical Catalog
:layout: book
:book_title: The Golden Ratio — Mathematical Catalog, Myth Triage & Concordance
:author: Mario Livio (2002) · Exact Synthesis by GEOMETOR
:year: 2002
:edition_year: 2026
:excerpt: A 48-entry exact symbolic mathematical catalog, empirical myth-triage ledger, and cross-corpus concordance inspired by Mario Livio's The Golden Ratio: The Story of Phi, the World's Most Astonishing Number.

.. _livio-catalog:

====================
Mathematical Catalog
====================

.. rubric:: Exact Symbolic Synthesis, Empirical Myth Triage & 5-Way Concordance — Inspired by Mario Livio (2002)

.. container:: title-page

   | **Reference Work:** *The Golden Ratio: The Story of Phi, the World's Most Astonishing Number* (Broadway Books, New York, 2002/2003, ISBN ``978-0-7679-0816-0``)
   | **Author:** Mario Livio (b. 1945), Astrophysicist
   | **Structure:** 9 Chapters + 10 Mathematical Appendices (128 Figures; 48 Atomic ``LIV-*`` Catalog Entries)
   | **Notation:** :math:`\phi = \frac{1+\sqrt{5}}{2}` (Mark Barr, early 20th c.) alongside professional :math:`\tau` (*tomē*) and negative conjugate :math:`\phi' = \frac{1-\sqrt{5}}{2} = -\frac{1}{\phi}`
   | **Digital Synthesis:** GEOMETOR (100% Exact ``SymPy`` Algebra in ``geometor.livio.invariants``, Zero Floating-Point Approximations)

Published by Broadway Books in 2002, Mario Livio's *The Golden Ratio* occupies a uniquely valuable position in the GEOMETOR golden-ratio canon alongside ``geometor/huntley`` (1970), ``geometor/knott`` (1996), ``geometor/divine``, and ``geometor/posamentier`` (2011). Whereas popular compendia frequently repeat 19th-century folklore from Adolf Zeising (1854) and Matila Ghyka (1927), Livio pairs genuine algebraic, geometric, and physical theorems—from Hippasus's pentagram descent and Piero della Francesca's polyhedra to Douady–Couder ferrofluid phyllotaxis, Penrose–Gummelt quasicrystals, Divakar Viswanath's random Fibonacci constant, and Benford's Law—with rigorous historiographic and statistical refutations grounded in Roger Herz-Fischler (1987/1998) and George Markowsky (1992).

Nine-Chapter & Ten-Appendix Map
-------------------------------

.. list-table::
   :header-rows: 1
   :widths: 10 24 12 54

   * - Locus
     - Title
     - Print pp.
     - Atomic ``LIV-*`` Entries & Core Mathematical Content
   * - **Ch. 1**
     - *Prelude to a Number*
     - ``1–11``
     - Chocolate-bar :math:`n-1` invariant & Buffon's needle :math:`P = 2/\pi` (``LIV-01.01``); Euclid ``VI.def.3`` & Martin Ohm (1835) / Mark Barr nomenclature audit (``LIV-01.02``).
   * - **Ch. 2**
     - *The Pitch and the Pentagram*
     - ``12–41``
     - :math:`\sin 666^\circ + \cos 216^\circ = -\phi` (``LIV-02.01``); Pythagorean dissection & :math:`(p^2-q^2, 2pq, p^2+q^2)` (``LIV-02.02``); monochord ratios (``LIV-02.03``); nested pentagram infinite-descent irrationality of :math:`\phi` (``LIV-02.04``).
   * - **Ch. 3**
     - *Under a Star-y-Pointing Pyramid?*
     - ``42–61``
     - Susa tablet pentagon constant :math:`1;40 = 5/3` vs. exact :math:`\frac{5\phi}{4\sqrt{3-\phi}}` (``LIV-03.01``); dimension-juggling error propagation (``LIV-03.02``); Great Pyramid Taylor/Herodotus fabrication vs. :math:`5\frac{1}{2}`-palm *seked* :math:`h/a = 14/11 \implies s/a = \sqrt{317}/11` (``LIV-03.03``).
   * - **Ch. 4**
     - *The Second Treasure*
     - ``62–91``
     - Platonic solid :math:`\mathbb{Q}(\phi)` volumes, dual edge ratio :math:`\phi^2/\sqrt{5}` & 3 orthogonal Golden Rectangles (``LIV-04.01``); Parthenon audit (``LIV-04.02``); Euclid ``II.11``, ``IV.10–11``, ``VI.30``, ``XIII`` & Golden Triangle/Gnomon (``LIV-04.03``); nested radical & ``[1; 1, 1, ...]`` (``LIV-04.04``); whirling squares & Pickover's *Eye of God* (``LIV-04.05``); al-Khwarizmi :math:`10x = (10-x)^2 \implies 10/\phi^2`, Abu Kamil & Abu'l-Wafa (``LIV-04.06``).
   * - **Ch. 5**
     - *Son of Good Nature*
     - ``92–123``
     - *Liber abaci* bezant shares (:math:`E=36, x=6`), *Liber quadratorum* :math:`(41/12)^2 \pm 5` & rabbit recurrence (``LIV-05.01``); 2-plate reflections :math:`F_{k+2}`, stairs & bee ancestry (``LIV-05.02``); :math:`11 F_{k+6}`, Pisano :math:`15 \cdot 10^{k-1}`, :math:`1/89` & Raine Pythagorean Fibonaccis (``LIV-05.03``); Golden Angle :math:`360^\circ/\phi^2` & Douady–Couder droplets (``LIV-05.04``); *Spira mirabilis* vs. quarter-circle arcs & *Nautilus* audit (``LIV-05.05``).
   * - **Ch. 6**
     - *The Divine Proportion*
     - ``124–158``
     - Piero della Francesca's *Libellus* & 5-circle packing :math:`\frac{\sqrt{3-\phi}}{2+\sqrt{3-\phi}}` (``LIV-06.01``); Pacioli's *Divina Proportione* & Book III plagiarism (``LIV-06.02``); Leonardo's 60 polyhedra vs. *Vitruvian Man* myth (``LIV-06.03``); Dürer's net & :math:`80^\circ` solid refutation (``LIV-06.04``); Kepler's :math:`1:\sqrt{\phi}:\phi` triangle, Cassini/Loyd ``64 = 65`` & pentagonal tilings (``LIV-06.05``).
   * - **Ch. 7**
     - *Painters and Poets Have Equal License*
     - ``159–200``
     - Fine-art audits (``LIV-07.01``); Le Corbusier's Red/Blue *Modulor* (``LIV-07.02``); Fechner–Markowsky rectangle psychophysics (``LIV-07.03``); Stradivari, Putz on Mozart, Lendvai–Somfai on Bartók, Howat on Debussy & Schillinger (``LIV-07.04``); Sanskrit *mātrā-vṛtta* prosody & Curchin–Herz-Fischler :math:`M/(M+m)` compression theorem (``LIV-07.05``).
   * - **Ch. 8**
     - *From the Tiles to the Heavens*
     - ``201–228``
     - Penrose kites/darts/rhombi & Ammann 3D golden rhombohedra (``LIV-08.01``); Gummelt single-decagon covering & Shechtman–Steinhardt quasicrystals (``LIV-08.02``); Sturmian Golden Sequence ``10110101...`` (``LIV-08.03``); :math:`120^\circ` Golden Fractal Tree :math:`f=1/\phi, D=\log 2/\log \phi` (``LIV-08.04``); Elliott Wave critique & Viswanath's :math:`1.13198824\dots` (``LIV-08.05``).
   * - **Ch. 9**
     - *Is God a Mathematician?*
     - ``229–253``
     - Newcomb–Benford's Law :math:`\log_{10}(1 + 1/D)`, Hill's theorem & Fibonacci leading digits (``LIV-09.01``); Fibonacci prime index theorem :math:`F_{19} = 37 \times 113` (``LIV-09.02``); Wigner & invention–discovery complementarity (``LIV-09.03``).
   * - **Apps. 1–10**
     - *Appendices 1–10*
     - ``255–268``
     - Complete self-contained proofs ``LIV-APP.01`` through ``LIV-APP.10`` (Pythagorean triples, pentagram descent, pyramid quadratic, :math:`36^\circ\text{-}72^\circ\text{-}72^\circ` similarity, quadratic formula, bezant shares, Koch dimension, :math:`120^\circ` Golden Tree self-contact, Benford's Law, and Euclid ``IX.20``).

Exact Symbolic Verifiers (``geometor.livio.invariants``)
--------------------------------------------------------

Every constructive theorem and quantitative myth-audit residual in ``geometor/livio`` is verified in exact ``SymPy`` arithmetic (guarded by ``assert_no_floats``):

- **Pentagram Infinite Descent** (``LIV-02.04``, ``LIV-APP.02``): :math:`d_1 = \phi s_1,\ d_2 = d_1 - s_1,\ s_2 = s_1 - d_2 \implies d_2 / s_2 = \phi` and :math:`s_2 / s_1 = 1/\phi^2 = 2 - \phi`.
- **Old Babylonian Susa Pentagon** (``LIV-03.01``): Exact unit-edge area :math:`\frac{5\phi}{4\sqrt{3-\phi}} = \frac{\sqrt{5(5+2\sqrt{5})}}{4}` vs. rational heuristic :math:`R_{\text{Susa}} = 5/6 \implies A_{\text{Susa}} = 5/3` (``1;40`` base 60).
- **Khufu Pyramid Seked vs. Herodotus Myth** (``LIV-03.03``, ``LIV-APP.03``): Egyptian :math:`5\frac{1}{2}`-palm *seked* per :math:`7`-palm royal cubit yields :math:`h/a = 14/11`, simultaneously producing slant ratio :math:`s/a = \sqrt{317}/11 \approx 1.61859` and perimeter-to-height :math:`8a/h = 44/7 \approx 2\pi` without irrational constants.
- **Platonic Solids in** :math:`\mathbb{Q}(\phi)` (``LIV-04.01``): Unit-edge dodecahedron surface :math:`\frac{15\phi}{\sqrt{3-\phi}}`, dodecahedron volume :math:`\frac{5\phi^3}{6-2\phi} = \frac{15+7\sqrt{5}}{4}`, icosahedron volume :math:`\frac{5\phi^2}{6}`, and concentric dual edge ratio :math:`\phi^2/\sqrt{5}`.
- **Al-Khwarizmi's Golden Division** (``LIV-04.06``): :math:`10x = (10 - x)^2 \implies x = 15 - 5\sqrt{5} = 10/\phi^2`.
- **Piero della Francesca's Five-Circle Packing** (``LIV-06.01``): Five congruent circles inscribed tangentially in a ring inside a unit circle have diameter ratio :math:`\frac{\sin 36^\circ}{1 + \sin 36^\circ} = \frac{\sqrt{3-\phi}}{2 + \sqrt{3-\phi}}`.
- **Kepler's Triangle** (``LIV-06.05``): Hypotenuse segments :math:`AD = \phi,\ DB = 1 \implies CD = \sqrt{\phi},\ CB = \phi,\ AC = \phi\sqrt{\phi},\ AB = \phi^2`.
- **Major-to-Whole Compression Identity** (``LIV-07.05``): For :math:`0 < m < M` with :math:`r = m/M`, :math:`\left|\frac{M}{M+m} - \frac{1}{\phi}\right| = \frac{|r - 1/\phi|}{\phi(1 + r)}`, shrinking arbitrary deviations toward :math:`1/\phi` by an exact factor :math:`\phi(1 + m/M) > \phi`.
- **Penrose Kite & Dart / Golden Tree / Benford's Law** (``LIV-08.01``, ``LIV-08.04``, ``LIV-09.01``): Exact kite-to-dart area ratio :math:`\phi`, :math:`120^\circ` tree self-contact :math:`f = f^3/(1-f) \implies f = 1/\phi`, and telescoping :math:`\sum_{D=1}^9 \log_{10}(1 + 1/D) = 1`.

Historical & Empirical Myth-Triage Ledger
-----------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 28 20 52

   * - Claim / Monument / Work
     - Livio Verdict
     - Primary Evidence & Exact Mathematical Mechanism
   * - **Great Pyramid of Khufu** (Ch. 3)
     - **Refuted Myth**
     - John Taylor (1859) fabricated the Herodotus II.124 ``h^2 = face area`` passage (Herz-Fischler, Markowsky); :math:`5\frac{1}{2}`-palm *seked* (:math:`h/a = 14/11`) explains both :math:`\phi` and :math:`\pi` coincidences.
   * - **Parthenon & Greek Vases** (Ch. 4)
     - **Refuted Myth**
     - Arbitrary bounding-box selection; actual facade width/height is :math:`2.25` (or :math:`\approx 1.72` with steps).
   * - **Nautilus pompilius, Horns, Falcon & M51** (Ch. 5)
     - **Refuted** (:math:`\phi`-specificity)
     - Scale-invariant growth produces general equiangular logarithmic spirals (:math:`\ln(r/r_0) = k\theta`), not specifically the Golden Spiral rate.
   * - **Piero della Francesca & Leonardo's 60 Polyhedra** (Ch. 6)
     - **Confirmed Intentional**
     - Exact pentagon/icosahedron/dodecahedron algebra in Piero's *Libellus* (plagiarized by Pacioli) and Leonardo's 60 *vacuus*/*solidus* plates (1496–1498).
   * - **Leonardo's Vitruvian Man, Mona Lisa & St. Jerome** (Chs. 6–7)
     - **Refuted Myth**
     - Drawn/painted prior to meeting Pacioli (1496); *Vitruvian Man* explicitly encodes Vitruvius's rational fractions (:math:`1/10, 1/8, 1/4`).
   * - **Dürer's Solid in Melencolia I** (Ch. 6)
     - **Refuted Myth**
     - Perspectival reconstruction (Lynch 1982; MacGillavry) proves an :math:`80^\circ` truncated rhombohedron on a :math:`4 \times 4` grid, not :math:`72^\circ`.
   * - **Seurat (Parade de cirque) & Mondrian** (Ch. 7)
     - **Refuted Myth**
     - Seurat used simple rational divisions (:math:`3:2, 8:5`, Herz-Fischler 1980); Mondrian worked intuitively by eye to "destroy mathematical formulas" (Yve-Alain Bois).
   * - **Sérusier, Lipchitz/Gris, Severini, Dalí & Le Corbusier's Modulor** (Chs. 1, 7)
     - **Confirmed Intentional**
     - Documented primary grids, Kepler triangles (*Arlequin* 1918), Dalí's dodecahedral *Last Supper*, and Le Corbusier's post-1945 Red/Blue *Modulor* scales.
   * - **Fechner's Golden Rectangle Preference** (Ch. 7)
     - **Refuted Myth**
     - Stimulus-range bias (Godkewitsch 1974), unpublished null ellipse test, and flat preference across :math:`1.5\text{–}1.75` in 48-rectangle arrays (McManus 1980; Markowsky 1992).
   * - **Mozart Sonatas & Vergil's Aeneid** (Ch. 7)
     - **Refuted Myth**
     - Algebraic compression artifact of :math:`M/(M+m) \in (0.5, 1)` (Curchin & Herz-Fischler 1981; Putz 1995); direct :math:`m/M` scatter is random.
   * - **Sanskrit Prosody (Virahāṅka, Gopāla, Hemacandra)** (Ch. 7)
     - **Confirmed Intentional**
     - Exact :math:`M_n = M_{n-1} + M_{n-2}` enumeration of short/long syllabic *mātrā* combinations centuries prior to Fibonacci (Singh 1985).
   * - **Douady–Couder Phyllotaxis & Icosahedral Quasicrystals** (Chs. 5, 8)
     - **Confirmed Physics**
     - Repulsive magnetic droplets converge dynamically to :math:`137.5^\circ`; Al–Mn/Al–Cu–Fe quasicrystals exhibit tenfold diffraction and :math:`\phi`-step STM terraces.

Catalog Apparatus
-----------------

- **Catalog Manifest**: ``resources/catalog_manifest.json`` (48 atomic entries)
- **5-Way Cross-Corpus Concordance**: ``resources/concordance.json`` (``divine``, ``huntley``, ``knott``, ``livio``, ``posamentier``)
- **People**: :ref:`persons`
- **Bibliography**: :ref:`bibliography`
