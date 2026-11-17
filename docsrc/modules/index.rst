:order: 90

=======
Modules
=======

API summary for ``geometor.livio``:

- :mod:`geometor.livio` — Public package interface exporting ``__version__`` and :func:`~geometor.livio.app.run`.
- :mod:`geometor.livio.app` — Command-line parser (:func:`~geometor.livio.app.build_parser`) and entry point (:func:`~geometor.livio.app.main`).
- :mod:`geometor.livio.catalog` — Typed catalog manifest descriptor (:class:`~geometor.livio.catalog.CatalogEntrySpec`), loader (:func:`~geometor.livio.catalog.load_catalog_manifest`), and exact-algebra guard (:func:`~geometor.livio.catalog.assert_no_floats`).
