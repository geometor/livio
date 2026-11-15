=====
livio
=====

Exact symbolic mathematical catalog, empirical myth-triage ledger, and 5-way golden-ratio concordance inspired by Mario Livio's *The Golden Ratio: The Story of Phi, the World's Most Astonishing Number* (Broadway Books, 2002).

Catalog Overview
----------------

- **Reference Work**: *The Golden Ratio: The Story of Phi, the World's Most Astonishing Number* (Mario Livio, Broadway Books, 2002/2003, ISBN ``978-0-7679-0816-0``)
- **Catalog Track**: ``docsrc/catalog/`` (``:layout: book``) — 9 Chapters + 10 Mathematical Appendices (``LIV-01.01``–``LIV-09.03``, ``LIV-APP.01``–``LIV-APP.10``, 48 atomic entries)
- **Exact Symbolic Engine**: ``src/geometor/livio/invariants.py`` — 100% exact ``SymPy`` verifiers (pentagram descent, Susa ``5/3`` vs. exact pentagon area, Khufu ``14/11`` *seked* vs. Herodotus quadratic, Platonic solid ``Q(phi)`` volumes & duals, al-Khwarizmi ``10/phi^2``, Fibonacci/bezant/congruent-square identities, Piero della Francesca 5-circle packing, Kepler's ``1:sqrt(phi):phi`` triangle, Curchin–Herz-Fischler ``M/(M+m)`` compression identity, Penrose kites & darts, Sturmian Golden Sequence, ``120 deg`` Golden Fractal Tree ``f = 1/phi``, and Benford's Law)
- **5-Way Concordance**: ``resources/concordance.json`` cross-referencing ``divine``, ``huntley``, ``knott``, ``livio``, and ``posamentier``

Verification & Build
--------------------

Managed with ``uv`` on Python 3.13:

.. code-block:: bash

   /home/phi/PROJECTS/geometor/.venv/bin/python -m pytest -v
   ruff check src tests demos
   publish build

Links
-----

- **Documentation**: https://geometor.github.io/livio
- **Repository**: https://github.com/geometor/livio
- **Issues**: https://github.com/geometor/livio/issues

License
-------

Licensed under the MIT License. See ``LICENSE`` for details.
