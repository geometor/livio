GEOMETOR • livio
================

**Visit the Online Archive:** https://geometor.github.io/livio/

**Mario Livio • The Golden Ratio & Myth Triage • semantic digital archive**

Mission
-------

``geometor/livio`` is part of the interconnected `GEOMETOR <https://geometor.com>`_ semantic digital archive. It formalizes Mario Livio's landmark treatise *The Golden Ratio: The Story of Phi, the World's Most Astonishing Number* (2002) into an exact symbolic mathematical catalog, empirical myth-triage ledger, and cross-corpus concordance. By distinguishing mathematically verified golden theorems from numerological fallacies through exact SymPy invariants over :math:`\mathbb{Q}(\phi)`, the archive liberates historical and aesthetic claims into rigorously testable units across the GEOMETOR corpus.

Catalogs in This Archive
------------------------

- `The Golden Ratio — Mathematical Catalog, Myth Triage & Concordance <https://geometor.github.io/livio/catalog/>`_ — Exact symbolic catalog across nine chapters and ten mathematical appendices, featuring 48 verified entries and cross-corpus concordance.

Python Package & Modules
------------------------

The ``geometor-livio`` Python package (``import geometor.livio``) provides the executable symbolic geometry, construction, and compilation modules powering this archive:

- ``catalog.py`` — Catalog manifest loader and exact-symbolic validation helpers.
- ``invariants.py`` — Exact symbolic verification of theorems, appendices, and residuals in ``geometor.livio``.
- ``app.py`` — Command-line interface for ``geometor.livio``.

See the `API Reference <https://geometor.github.io/livio/modules/>`_ for full module documentation.

Repository Contents
-------------------

- ``docsrc/`` — RST catalog tracks, myth-triage ledgers, and guides compiled by `PHOTON publish <https://github.com/photon-platform/publish>`_.
- ``resources/`` — Curated mathematical manifests and 5-way concordance registries.
- ``src/geometor/livio/`` — Exact symbolic verifiers, invariant engines, and CLI tools.

Local Build & Verification
--------------------------

.. code-block:: bash

   publish build
   uv run --no-sync pytest

Part of the GEOMETOR Knowledge Archive
--------------------------------------

Explore all **74 Book Codices** and **11 Mathematical Catalogs** at https://geometor.com/books/.
