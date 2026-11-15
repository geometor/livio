"""Comprehensive exact-symbolic verification tests for ``geometor.livio``."""

from __future__ import annotations

import json
from pathlib import Path

import pytest
import sympy as sp

from geometor.livio import (
    PHI,
    PHI_CONJ,
    CatalogEntrySpec,
    __version__,
    assert_no_floats,
    golden_sequence_word,
    load_catalog_manifest,
    run,
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

REPO_ROOT = Path(__file__).resolve().parents[1]


def test_version_and_cli() -> None:
    """Verify initial semantic version and clean zero-argument CLI execution."""
    assert __version__ == "0.1.0"
    assert run([]) == 0


def test_cli_help_exits_cleanly() -> None:
    """Verify ``--help`` exits cleanly with code ``0``."""
    with pytest.raises(SystemExit) as exc_info:
        run(["--help"])
    assert exc_info.value.code == 0


def test_phi_algebraic_conjugates_and_float_guard() -> None:
    """Verify ``PHI``, ``PHI_CONJ``, and ``sp.GoldenRatio`` exact identities."""
    assert sp.simplify(PHI - sp.GoldenRatio) == 0
    assert sp.simplify(PHI + PHI_CONJ - 1) == 0
    assert sp.simplify(PHI * PHI_CONJ + 1) == 0
    assert sp.simplify(PHI**2 - PHI - 1) == 0
    assert_no_floats(PHI)
    assert_no_floats(PHI_CONJ)
    with pytest.raises(TypeError):
        assert_no_floats(1.6180339887)
    with pytest.raises(TypeError):
        assert_no_floats(sp.Float("1.618"))


def test_appendices_and_chapter_theorems_exact() -> None:
    """Verify Appendices 1–9 and Chapters 2–9 mathematical theorems symbolically."""
    assert verify_pythagorean_triple_identity() == 0
    inner_ratio, descent_scale = verify_pentagram_descent_step()
    assert sp.simplify(inner_ratio - PHI) == 0
    assert sp.simplify(descent_scale - (2 - PHI)) == 0

    assert sp.simplify(verify_recreational_666_identity() + PHI) == 0

    susa = verify_susa_pentagon_area()
    assert susa["susa_area"] == sp.Rational(5, 3)

    pyramid = verify_pyramid_herodotus_and_seked()
    assert pyramid["seked_h_over_a"] == sp.Rational(14, 11)
    assert pyramid["seked_perim_over_h"] == sp.Rational(44, 7)
    assert pyramid["rhind_pi"] == sp.Rational(256, 81)

    solids = verify_platonic_icosa_dodec_metrics()
    assert sp.simplify(solids["vol_icosa"] - 5 * PHI**2 / 6) == 0

    cos36, cos72 = verify_golden_triangle_similarity()
    assert sp.simplify(cos36 - cos72 - sp.Rational(1, 2)) == 0

    assert sp.simplify(verify_alkhwarizmi_ten_division() - (15 - 5 * sp.sqrt(5))) == 0

    fib = verify_fibonacci_identities()
    assert fib["bezant_estate"] == 36
    assert fib["bezant_share"] == 6

    piero_ratio = verify_piero_five_circle_packing()
    assert_no_floats(piero_ratio)

    kepler = verify_kepler_triangle()
    assert sp.simplify(kepler["hypotenuse"] - PHI**2) == 0
    assert sp.simplify(kepler["altitude"] - sp.sqrt(PHI)) == 0
    assert kepler["pythag_residual"] == 0

    comp = verify_major_to_whole_compression(317, 160)
    assert comp["minor_to_major"] == sp.Rational(160, 317)
    assert comp["major_to_whole"] == sp.Rational(317, 477)
    assert sp.simplify(comp["compression_factor"] - sp.Rational(477, 317) * PHI) == 0
    assert comp["identity_residual"] == 0
    assert bool(comp["compressed_err"] < comp["direct_err"])
    with pytest.raises(ValueError, match="0 < minor < major"):
        verify_major_to_whole_compression(10, 20)

    penrose = verify_penrose_kite_and_dart()
    assert sp.simplify(penrose["kite_to_dart_ratio"] - PHI) == 0

    word = golden_sequence_word(6)
    assert word == "1011010110110"
    assert word.count("1") == 8
    assert word.count("0") == 5

    f_contact, dim = verify_golden_fractal_tree_contact()
    assert sp.simplify(f_contact - (PHI - 1)) == 0
    assert dim == sp.log(2) / sp.log(PHI)

    assert verify_benford_exact_identities() == 1


def test_catalog_manifest_and_concordance_integrity() -> None:
    """Verify 48-entry catalog manifest, 1-to-1 concordance parity, and apparatus JSON."""
    entries = load_catalog_manifest()
    assert len(entries) == 48
    ids = [item.id for item in entries]
    assert len(ids) == len(set(ids))
    for item in entries:
        assert isinstance(item, CatalogEntrySpec)
        assert item.id.startswith("LIV-")
        assert item.title
        assert item.source_locus

    app_ids = [eid for eid in ids if eid.startswith("LIV-APP.")]
    assert len(app_ids) == 10

    concordance_path = REPO_ROOT / "resources" / "concordance.json"
    payload = json.loads(concordance_path.read_text(encoding="utf-8"))
    assert payload.get("catalog") == "livio"
    mapped_ids = [row["livio_id"] for row in payload["mappings"]]
    assert mapped_ids == ids

    for resource_name, top_key in (
        ("persons.json", "persons"),
        ("citations.json", "citations"),
        ("glossary.json", "terms"),
    ):
        data = json.loads((REPO_ROOT / "resources" / resource_name).read_text(encoding="utf-8"))
        assert len(data[top_key]) >= 8
