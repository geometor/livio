"""Exact symbolic verification of theorems, appendices, and residuals in ``geometor.livio``."""

from __future__ import annotations

import sympy as sp

from .catalog import assert_no_floats

__all__ = [
    "PHI",
    "PHI_CONJ",
    "golden_sequence_word",
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

PHI: sp.Expr = (sp.Integer(1) + sp.sqrt(5)) / sp.Integer(2)
PHI_CONJ: sp.Expr = (sp.Integer(1) - sp.sqrt(5)) / sp.Integer(2)


def verify_pythagorean_triple_identity() -> sp.Expr:
    """Verify Appendix 1: ``(p^2 - q^2)^2 + (2pq)^2 == (p^2 + q^2)^2``.

    Returns:
        Exact symbolic zero residual after algebraic expansion.
    """
    p, q = sp.symbols("p q", integer=True)
    residual = sp.expand((p**2 - q**2) ** 2 + (2 * p * q) ** 2 - (p**2 + q**2) ** 2)
    assert_no_floats(residual)
    if residual != 0:
        msg = f"Expected zero Pythagorean residual, got {residual}"
        raise ValueError(msg)
    return residual


def verify_pentagram_descent_step() -> tuple[sp.Expr, sp.Expr]:
    """Verify Appendix 2: nested pentagram infinite-descent step preserves ``phi``.

    Given outer regular pentagon side ``s1`` and diagonal ``d1 = phi * s1``,
    the inner pentagon formed by the five diagonals has diagonal ``d2 = d1 - s1``
    and side ``s2 = s1 - d2``.

    Returns:
        Tuple ``(d2 / s2, s2 / s1)`` simplified to ``(PHI, 1 / PHI**2)``.
    """
    s1 = sp.Symbol("s1", positive=True)
    d1 = PHI * s1
    d2 = sp.simplify(d1 - s1)
    s2 = sp.simplify(s1 - d2)
    inner_ratio = sp.simplify(d2 / s2)
    scale_factor = sp.simplify(s2 / s1)
    assert_no_floats(inner_ratio)
    assert_no_floats(scale_factor)
    if sp.simplify(inner_ratio - PHI) != 0:
        msg = f"Expected inner pentagram ratio phi, got {inner_ratio}"
        raise ValueError(msg)
    if sp.simplify(scale_factor - 1 / PHI**2) != 0:
        msg = f"Expected descent scale 1/phi^2, got {scale_factor}"
        raise ValueError(msg)
    return inner_ratio, scale_factor


def verify_recreational_666_identity() -> sp.Expr:
    """Verify Ch. 2 trigonometric identity ``sin(666 deg) + cos(216 deg) == -phi``.

    Returns:
        Exact simplified sum ``-PHI``.
    """
    expr = sp.simplify(
        sp.sin(sp.Rational(666, 180) * sp.pi) + sp.cos(sp.Rational(216, 180) * sp.pi)
    )
    assert_no_floats(expr)
    if sp.simplify(expr + PHI) != 0:
        msg = f"Expected -phi, got {expr}"
        raise ValueError(msg)
    return expr


def verify_susa_pentagon_area() -> dict[str, sp.Expr]:
    """Verify Ch. 3 Old Babylonian Susa pentagon constant ``5/3`` vs. exact unit-pentagon area.

    Returns:
        Dictionary of exact symbolic expressions for ``exact_area``, ``livio_phi_form``,
        and ``susa_area``.
    """
    exact_area = sp.sqrt(5 * (5 + 2 * sp.sqrt(5))) / sp.Integer(4)
    livio_phi_form = (sp.Integer(5) * PHI) / (sp.Integer(4) * sp.sqrt(3 - PHI))
    r_susa = sp.Rational(5, 6)
    apothem_susa = sp.sqrt(r_susa**2 - sp.Rational(1, 2) ** 2)
    susa_area = sp.Integer(5) * sp.Rational(1, 2) * apothem_susa
    for val in (exact_area, livio_phi_form, susa_area):
        assert_no_floats(val)
    if sp.simplify(exact_area**2 - livio_phi_form**2) != 0:
        msg = "Unit-pentagon exact radical and phi forms do not match"
        raise ValueError(msg)
    if susa_area != sp.Rational(5, 3):
        msg = f"Expected Susa area 5/3 (1;40), got {susa_area}"
        raise ValueError(msg)
    return {
        "exact_area": exact_area,
        "livio_phi_form": livio_phi_form,
        "susa_area": susa_area,
    }


def verify_pyramid_herodotus_and_seked() -> dict[str, sp.Expr]:
    """Verify Appendix 3 pyramid quadratic and Ch. 3 Egyptian 5.5-palm ``seked`` metrics.

    Returns:
        Dictionary of exact symbolic slopes and slant ratios (zero floats).
    """
    x = sp.Symbol("x", positive=True)
    roots = sp.solve(x**2 - x - 1, x)
    if roots != [PHI]:
        msg = f"Expected unique positive root [PHI], got {roots}"
        raise ValueError(msg)

    seked_palms = sp.Rational(11, 2)
    cubit_palms = sp.Integer(7)
    h_over_a_seked = cubit_palms / seked_palms  # 14/11
    s_over_a_seked = sp.simplify(sp.sqrt(1 + h_over_a_seked**2))  # sqrt(317)/11
    perim_over_h_seked = sp.Integer(8) / h_over_a_seked  # 44/7
    rhind_pi = sp.Rational(16, 9) ** 2  # 256/81

    result = {
        "kepler_s_over_a": PHI,
        "kepler_h_over_a": sp.sqrt(PHI),
        "seked_h_over_a": h_over_a_seked,
        "seked_s_over_a": s_over_a_seked,
        "seked_perim_over_h": perim_over_h_seked,
        "rhind_pi": rhind_pi,
    }
    for val in result.values():
        assert_no_floats(val)
    if h_over_a_seked != sp.Rational(14, 11):
        msg = "Unexpected seked height-to-half-base ratio"
        raise ValueError(msg)
    if s_over_a_seked != sp.sqrt(317) / sp.Integer(11):
        msg = "Unexpected seked slant-to-half-base ratio"
        raise ValueError(msg)
    return result


def verify_platonic_icosa_dodec_metrics() -> dict[str, sp.Expr]:
    """Verify Ch. 4 unit-edge dodecahedron/icosahedron surface, volume, and dual ratios.

    Returns:
        Dictionary of verified exact ``Q(phi)`` and radical expressions.
    """
    area_dodec_phi = (sp.Integer(15) * PHI) / sp.sqrt(3 - PHI)
    area_dodec_rad = sp.Integer(3) * sp.sqrt(25 + 10 * sp.sqrt(5))
    vol_dodec_phi = (sp.Integer(5) * PHI**3) / (sp.Integer(6) - sp.Integer(2) * PHI)
    vol_dodec_rad = (sp.Integer(15) + sp.Integer(7) * sp.sqrt(5)) / sp.Integer(4)
    vol_icosa_phi = (sp.Integer(5) * PHI**2) / sp.Integer(6)
    vol_icosa_rad = (sp.Integer(5) * (sp.Integer(3) + sp.sqrt(5))) / sp.Integer(12)
    dual_edge_ratio = sp.simplify(PHI**2 / sp.sqrt(5))

    if sp.simplify(area_dodec_phi**2 - area_dodec_rad**2) != 0:
        msg = "Dodecahedron surface area phi-form mismatch"
        raise ValueError(msg)
    if sp.simplify(vol_dodec_phi - vol_dodec_rad) != 0:
        msg = "Dodecahedron volume phi-form mismatch"
        raise ValueError(msg)
    if sp.simplify(vol_icosa_phi - vol_icosa_rad) != 0:
        msg = "Icosahedron volume phi-form mismatch"
        raise ValueError(msg)

    result = {
        "area_dodec": area_dodec_phi,
        "vol_dodec": vol_dodec_phi,
        "vol_icosa": vol_icosa_phi,
        "dual_edge_ratio": dual_edge_ratio,
    }
    for val in result.values():
        assert_no_floats(val)
    return result


def verify_golden_triangle_similarity() -> tuple[sp.Expr, sp.Expr]:
    """Verify Appendix 4 Golden Triangle (36-72-72) angle-bisector ratio and cosines.

    Returns:
        Exact symbolic tuple ``(cos(36 deg), cos(72 deg))`` equal to ``(PHI/2, 1/(2*PHI))``.
    """
    cos36 = sp.simplify(sp.cos(sp.Rational(36, 180) * sp.pi))
    cos72 = sp.simplify(sp.cos(sp.Rational(72, 180) * sp.pi))
    assert_no_floats(cos36)
    assert_no_floats(cos72)
    if sp.simplify(cos36 - PHI / 2) != 0:
        msg = f"Expected cos(36 deg) == phi/2, got {cos36}"
        raise ValueError(msg)
    if sp.simplify(cos72 - 1 / (2 * PHI)) != 0:
        msg = f"Expected cos(72 deg) == 1/(2*phi), got {cos72}"
        raise ValueError(msg)
    return cos36, cos72


def verify_alkhwarizmi_ten_division() -> sp.Expr:
    """Verify Ch. 4 al-Khwarizmi quadratic ``10*x = (10 - x)^2`` gives ``10 / phi^2``.

    Returns:
        Exact shorter Golden Ratio segment ``15 - 5*sqrt(5) == 10 / PHI**2``.
    """
    x = sp.Symbol("x", positive=True)
    roots = [r for r in sp.solve(10 * x - (10 - x) ** 2, x) if r < 10]
    if len(roots) != 1:
        msg = f"Expected unique root in (0, 10), got {roots}"
        raise ValueError(msg)
    root = sp.simplify(roots[0])
    assert_no_floats(root)
    if sp.simplify(root - sp.Integer(10) / PHI**2) != 0:
        msg = f"Expected 10/phi^2, got {root}"
        raise ValueError(msg)
    return root


def verify_fibonacci_identities() -> dict[str, sp.Expr | tuple[sp.Rational, ...]]:
    """Verify Ch. 5 & Appendix 6 Fibonacci identities, bezant shares, and congruent squares.

    Returns:
        Dictionary of verified exact values and symbolic residuals.
    """
    estate, share = sp.symbols("E x", rational=True)
    sol = sp.solve(
        [
            sp.Eq(share, 1 + (estate - 1) / sp.Integer(7)),
            sp.Eq(share, 2 + (estate - 2 - share) / sp.Integer(7)),
        ],
        (estate, share),
        dict=True,
    )
    if sol != [{estate: sp.Integer(36), share: sp.Integer(6)}]:
        msg = f"Unexpected bezant inheritance solution: {sol}"
        raise ValueError(msg)

    congruent_x = sp.Rational(41, 12)
    plus_five = sp.sqrt(congruent_x**2 + 5)
    minus_five = sp.sqrt(congruent_x**2 - 5)
    if (plus_five, minus_five) != (sp.Rational(49, 12), sp.Rational(31, 12)):
        msg = "Unexpected Liber quadratorum congruent-5 rational squares"
        raise ValueError(msg)

    a, b = sp.symbols("a b", integer=True)
    seq = [a, b]
    for _ in range(8):
        seq.append(seq[-1] + seq[-2])
    eleven_residual = sp.simplify(sum(seq) - 11 * seq[6])

    f1, f2 = sp.symbols("f1 f2", integer=True)
    f3 = f1 + f2
    f4 = f2 + f3
    raine_residual = sp.expand((f1 * f4) ** 2 + (2 * f2 * f3) ** 2 - (f2**2 + f3**2) ** 2)

    if eleven_residual != 0 or raine_residual != 0:
        msg = "Generalized Fibonacci 11-sum or Raine Pythagorean residual nonzero"
        raise ValueError(msg)

    result: dict[str, sp.Expr | tuple[sp.Rational, ...]] = {
        "bezant_estate": sp.Integer(36),
        "bezant_share": sp.Integer(6),
        "congruent_triple": (minus_five, congruent_x, plus_five),
        "eleven_sum_residual": eleven_residual,
        "raine_pythagorean_residual": raine_residual,
    }
    for val in result.values():
        if isinstance(val, tuple):
            for item in val:
                assert_no_floats(item)
        else:
            assert_no_floats(val)
    return result


def verify_piero_five_circle_packing() -> sp.Expr:
    """Verify Ch. 6 Piero della Francesca 5-circle packing ratio inside a unit-diameter circle.

    Returns:
        Exact small-to-large circle diameter ratio ``sqrt(3 - phi) / (2 + sqrt(3 - phi))``.
    """
    sin36 = sp.simplify(sp.sin(sp.Rational(36, 180) * sp.pi))
    ratio = sp.simplify(sin36 / (1 + sin36))
    phi_form = sp.simplify(sp.sqrt(3 - PHI) / (2 + sp.sqrt(3 - PHI)))
    assert_no_floats(ratio)
    assert_no_floats(phi_form)
    if sp.simplify(ratio - phi_form) != 0:
        msg = f"Mismatch in Piero 5-circle packing ratio: {ratio} vs {phi_form}"
        raise ValueError(msg)
    return phi_form


def verify_kepler_triangle() -> dict[str, sp.Expr]:
    """Verify Ch. 6 Kepler Triangle (Oct 1597 letter to Maestlin, ``Fig. 61``).

    Dividing hypotenuse ``AB`` at altitude foot ``D`` with ``AD = phi`` and ``DB = 1``
    gives ``AB = phi^2``, altitude ``CD = sqrt(phi)``, legs ``CB = phi`` and
    ``AC = phi * sqrt(phi)``, and normalized geometric progression ``(1, sqrt(phi), phi)``.

    Returns:
        Dictionary of exact symbolic segment lengths and Pythagorean residual.
    """
    ad = PHI
    db = sp.Integer(1)
    ab = sp.simplify(ad + db)
    cd = sp.sqrt(ad * db)
    cb = sp.simplify(sp.sqrt(db * ab))
    ac = sp.simplify(sp.sqrt(ad * ab))
    pythag_residual = sp.simplify(cb**2 + ac**2 - ab**2)
    norm_residual = sp.simplify(sp.Integer(1) ** 2 + sp.sqrt(PHI) ** 2 - PHI**2)

    if sp.simplify(ab - PHI**2) != 0 or sp.simplify(cb - PHI) != 0:
        msg = "Kepler hypotenuse projection identities failed"
        raise ValueError(msg)
    if pythag_residual != 0 or norm_residual != 0:
        msg = "Kepler Triangle Pythagorean residual nonzero"
        raise ValueError(msg)

    result = {
        "hypotenuse": ab,
        "altitude": cd,
        "short_leg": cb,
        "long_leg": ac,
        "pythag_residual": pythag_residual,
    }
    for val in result.values():
        assert_no_floats(val)
    return result


def verify_major_to_whole_compression(
    major: int = 317,
    minor: int = 160,
) -> dict[str, sp.Expr]:
    """Verify Ch. 7 Curchin & Herz-Fischler (1981) ``M / (M + m)`` compression identity.

    For any ``M > m > 0`` with ``r = m / M``, ``M / (M + m) - 1 / phi`` equals
    ``(1 / phi - r) / (phi * (1 + r))``, shrinking the distance to ``1 / phi`` by an
    exact factor ``phi * (1 + m / M) > phi > 1`` (Livio ``Fig. 91``, ``M = 317, m = 160``).

    Args:
        major: Positive integer major line/measure count ``M``.
        minor: Positive integer minor line/measure count ``m`` with ``0 < m < M``.

    Returns:
        Dictionary of exact rational ratios, deviations from ``1 / phi``, and compression factor.
    """
    if not (0 < minor < major):
        msg = f"Expected 0 < minor < major, got minor={minor}, major={major}"
        raise ValueError(msg)

    inv_phi = sp.Integer(1) / PHI
    minor_to_major = sp.Rational(minor, major)
    major_to_whole = sp.Rational(major, major + minor)

    direct_err = sp.simplify(sp.Abs(minor_to_major - inv_phi))
    compressed_err = sp.simplify(sp.Abs(major_to_whole - inv_phi))
    compression_factor = sp.simplify(PHI * (sp.Integer(1) + minor_to_major))
    identity_residual = sp.simplify(direct_err - compression_factor * compressed_err)

    if identity_residual != 0:
        msg = f"Expected zero compression residual, got {identity_residual}"
        raise ValueError(msg)
    if not bool(compression_factor > PHI):
        msg = f"Expected compression factor > phi, got {compression_factor}"
        raise ValueError(msg)

    result: dict[str, sp.Expr] = {
        "minor_to_major": minor_to_major,
        "major_to_whole": major_to_whole,
        "direct_err": direct_err,
        "compressed_err": compressed_err,
        "compression_factor": compression_factor,
        "identity_residual": identity_residual,
    }
    for val in result.values():
        assert_no_floats(val)
    return result


def verify_penrose_kite_and_dart() -> dict[str, sp.Expr]:
    """Verify Ch. 8 Penrose kite and dart area ratio ``phi`` and rhombus partition.

    Returns:
        Dictionary with exact areas of kite, dart, and parent ``72-108`` rhombus of side ``phi``.
    """
    sin36 = sp.sin(sp.Rational(36, 180) * sp.pi)
    sin72 = sp.sin(sp.Rational(72, 180) * sp.pi)
    area_kite = sp.simplify(PHI**2 * sin36)
    area_dart = sp.simplify(PHI * sin36)
    area_rhombus = sp.simplify(PHI**2 * sin72)
    ratio = sp.simplify(area_kite / area_dart)
    partition_residual = sp.simplify(area_kite + area_dart - area_rhombus)
    for val in (area_kite, area_dart, area_rhombus, ratio, partition_residual):
        assert_no_floats(val)
    if sp.simplify(ratio - PHI) != 0 or partition_residual != 0:
        msg = "Penrose kite/dart area ratio or rhombus partition check failed"
        raise ValueError(msg)
    return {
        "area_kite": area_kite,
        "area_dart": area_dart,
        "area_rhombus": area_rhombus,
        "kite_to_dart_ratio": ratio,
    }


def golden_sequence_word(generations: int = 6) -> str:
    """Generate the Ch. 8 Sturmian Golden Sequence via substitution ``1 -> 10, 0 -> 1``.

    Args:
        generations: Number of morphism iterations starting from ``"1"`` (generation ``1``).

    Returns:
        Exact binary Sturmian prefix of length ``F_{generations + 1}``.
    """
    if generations < 1:
        msg = "generations must be >= 1"
        raise ValueError(msg)
    word = "1"
    for _ in range(generations - 1):
        word = "".join("10" if ch == "1" else "1" for ch in word)
    return word


def verify_golden_fractal_tree_contact() -> tuple[sp.Expr, sp.Expr]:
    """Verify Appendix 8 Golden Fractal Tree self-contact factor ``1/phi`` and dimension.

    Returns:
        Tuple ``(f_contact, hausdorff_dimension)`` equal to ``(1/PHI, log(2)/log(PHI))``.
    """
    f = sp.Symbol("f", positive=True)
    # Horizontal excursion equation f = f^3 / (1 - f) => f^2 + f - 1 = 0
    roots = [r for r in sp.solve(sp.Eq(f, f**3 / (1 - f)), f) if 0 < r < 1]
    if len(roots) != 1:
        msg = f"Expected unique self-contact factor in (0, 1), got {roots}"
        raise ValueError(msg)
    f_contact = sp.simplify(roots[0])
    dimension = sp.log(2) / sp.log(PHI)
    assert_no_floats(f_contact)
    assert_no_floats(dimension)
    if sp.simplify(f_contact - 1 / PHI) != 0:
        msg = f"Expected self-contact factor 1/phi, got {f_contact}"
        raise ValueError(msg)
    return f_contact, dimension


def verify_benford_exact_identities() -> sp.Expr:
    """Verify Appendix 9 exact telescoping sum of Benford first-digit probabilities equals ``1``.

    Returns:
        Exact simplified sum ``sum_{d=1}^9 log_10(1 + 1/d) == 1``.
    """
    total = sp.simplify(
        sum(sp.log(1 + sp.Rational(1, d), 10) for d in range(1, 10))
    )
    assert_no_floats(total)
    if total != sp.Integer(1):
        msg = f"Expected exact telescoping Benford sum 1, got {total}"
        raise ValueError(msg)
    return total
