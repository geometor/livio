:navigation: header
:order: 10

=====
About
=====

``geometor.livio`` is developed and maintained by **phiarchitect** as part of the **GEOMETOR** organization.

Exact symbolic mathematical catalog and concordance inspired by The Golden Ratio: The Story of Phi, the World's Most Astonishing Number (Mario Livio)

Repository Architecture
-----------------------

- **Python Package**: ``src/geometor/livio/`` (Python 3.13)
- **Mathematical Catalog**: ``docsrc/catalog/`` (``:layout: book``)
- **Manifest & Concordance**: ``resources/catalog_manifest.json``, ``resources/concordance.json``
- **Automated Verification**: ``tests/`` (``pytest`` + ``ruff``) and ``docsrc/`` (``publish build``)
