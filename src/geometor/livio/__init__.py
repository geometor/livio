"""Public package interface for ``geometor.livio``."""

from __future__ import annotations

from .app import main, run
from .catalog import CatalogEntrySpec, assert_no_floats, load_catalog_manifest
from .invariants import (
    PHI,
    PHI_CONJ,
    golden_sequence_word,
    verify_alkhwarizmi_ten_division,
    verify_benford_exact_identities,
    verify_fibonacci_identities,
    verify_golden_fractal_tree_contact,
    verify_golden_triangle_similarity,
    verify_kepler_triangle,
    verify_major_to_whole_compression,
    verify_penrose_kite_and_dart,
    verify_pentagram_descent_step,
    verify_piero_five_circle_packing,
    verify_platonic_icosa_dodec_metrics,
    verify_pyramid_herodotus_and_seked,
    verify_pythagorean_triple_identity,
    verify_recreational_666_identity,
    verify_susa_pentagon_area,
)

__version__ = "0.1.0"

__all__ = [
    "CatalogEntrySpec",
    "PHI",
    "PHI_CONJ",
    "__version__",
    "assert_no_floats",
    "golden_sequence_word",
    "load_catalog_manifest",
    "main",
    "run",
    "verify_alkhwarizmi_ten_division",
    "verify_benford_exact_identities",
    "verify_fibonacci_identities",
    "verify_golden_fractal_tree_contact",
    "verify_golden_triangle_similarity",
    "verify_kepler_triangle",
    "verify_major_to_whole_compression",
    "verify_penrose_kite_and_dart",
    "verify_pentagram_descent_step",
    "verify_piero_five_circle_packing",
    "verify_platonic_icosa_dodec_metrics",
    "verify_pyramid_herodotus_and_seked",
    "verify_pythagorean_triple_identity",
    "verify_recreational_666_identity",
    "verify_susa_pentagon_area",
]
