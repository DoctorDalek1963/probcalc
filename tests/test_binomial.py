# probcalc - Calculate probabilities for distributions
# Copyright (C) 2022 D. Dyson (DoctorDalek1963)

# This program is licensed under GNU GPLv3, available here:
# <https://www.gnu.org/licenses/gpl-3.0.html>

"""A simple test module to test the :class:`probcalc.distributions.BinomialDistribution`.

All test values calculated with a Casio fx-991EX Classwiz.
"""

import pytest
from pytest import approx

from probcalc import P, B, NonsenseError


def test_pmf() -> None:
    """Test the binomial distribution PMF."""
    X = B(20, 0.25)
    Y = B(14, 0.36)
    Z = B(50, 0.782)
    W = B(1000, 0.9)

    assert X.pmf(0) == approx(3.171211939e-3)
    assert X.pmf(1) == approx(0.02114141293)
    assert X.pmf(2) == approx(0.0669478076)
    assert X.pmf(3) == approx(0.1338956152)
    assert X.pmf(4) == approx(0.1896854549)
    assert X.pmf(5) == approx(0.2023311519)
    assert X.pmf(6) == approx(0.1686092932)
    assert X.pmf(7) == approx(0.1124061955)
    assert X.pmf(8) == approx(0.06088668922)
    assert X.pmf(9) == approx(0.02706075076)
    assert X.pmf(10) == approx(9.92227528e-3)
    assert X.pmf(11) == approx(3.006750085e-3)
    assert X.pmf(12) == approx(7.516875212e-4)
    assert X.pmf(13) == approx(1.54192312e-4)
    assert X.pmf(14) == approx(2.569871867e-5)
    assert X.pmf(15) == approx(3.426495823e-6)
    assert X.pmf(16) == approx(3.569266482e-7)
    assert X.pmf(17) == approx(2.799424692e-8)
    assert X.pmf(18) == approx(1.55523594e-9)
    assert X.pmf(19) == approx(5.456968211e-11)
    assert X.pmf(20) == approx(9.094947018e-13)

    assert Y.pmf(4) == approx(0.1938401871)
    assert Y.pmf(8) == approx(0.05821771856)
    assert Y.pmf(13) == approx(1.528412284e-5)

    assert Z.pmf(12) == approx(4.613656329e-16)
    assert Z.pmf(21) == approx(2.516357132e-8)
    assert Z.pmf(36) == approx(0.0734455353)
    assert Z.pmf(45) == approx(0.01631804512)

    assert W.pmf(100) < 1e-100
    assert W.pmf(200) < 1e-100
    assert W.pmf(300) < 1e-100
    assert W.pmf(400) < 1e-100
    assert W.pmf(500) < 1e-100
    assert W.pmf(600) < 1e-100
    assert W.pmf(700) == approx(5.063099384e-69)
    assert W.pmf(800) == approx(1.639377219e-21)
    assert W.pmf(900) == approx(0.04201679075)
    assert W.pmf(1000) == approx(1.747871252e-46)

    for num in [-1, -3, 21, 30, 12.5, 22.3]:
        with pytest.raises(NonsenseError):
            X.pmf(num, strict=True)  # type: ignore[arg-type]

    assert X.pmf(-1, strict=False) < 1e-100
    assert X.pmf(-3, strict=False) < 1e-100
    assert X.pmf(21, strict=False) < 1e-100
    assert X.pmf(30, strict=False) < 1e-100

    assert X.pmf(12.5, strict=False) < 1e-100  # type: ignore[arg-type]
    assert X.pmf(22.3, strict=False) < 1e-100  # type: ignore[arg-type]


def test_cdf() -> None:
    """Test the binomial distribution CDF."""
    X = B(20, 0.25)
    Y = B(14, 0.36)
    Z = B(50, 0.782)
    W = B(1000, 0.90)

    assert X.cdf(0) == approx(3.1712119939e-3)
    assert X.cdf(1) == approx(0.02431262487)
    assert X.cdf(2) == approx(0.09126043246)
    assert X.cdf(3) == approx(0.2251560477)
    assert X.cdf(4) == approx(0.4148415008)
    assert X.cdf(5) == approx(0.6171726621)
    assert X.cdf(6) == approx(0.7857819481)
    assert X.cdf(7) == approx(0.8981881431)
    assert X.cdf(8) == approx(0.9590748321)
    assert X.cdf(9) == approx(0.986135583)
    assert X.cdf(10) == approx(0.9960578583)
    assert X.cdf(11) == approx(0.9990646084)
    assert X.cdf(12) == approx(0.9998162959)
    assert X.cdf(13) == approx(0.9999704883)
    assert X.cdf(14) == approx(0.999996187)
    assert X.cdf(15) == approx(0.9999996135)
    assert X.cdf(16) == approx(0.9999999704)
    assert X.cdf(17) == approx(0.9999999984)
    assert X.cdf(18) == approx(0.9999999999)
    assert X.cdf(19) == approx(1.0)
    assert X.cdf(20) == 1.0

    assert Y.cdf(4) == approx(0.3920114632)
    assert Y.cdf(8) == approx(0.970579751)
    assert Y.cdf(13) == approx(0.9999993859)

    assert Z.cdf(12) == approx(5.041928974e-16)
    assert Z.cdf(21) == approx(3.112911755e-8)
    assert Z.cdf(36) == approx(0.1846045478)
    assert Z.cdf(45) == approx(0.9911912197)

    assert W.cdf(100) < 1e-100
    assert W.cdf(200) < 1e-100
    assert W.cdf(300) < 1e-100
    assert W.cdf(400) < 1e-100
    assert W.cdf(500) < 1e-100
    assert W.cdf(600) < 1e-100
    assert W.cdf(700) == approx(6.823349114e-69)
    assert W.cdf(800) == approx(2.928054793e-21)
    assert W.cdf(900) == approx(0.5154177186)
    assert W.cdf(1000) == 1

    for num in [-1, -3, 21, 30, 12.5, 22.3]:
        with pytest.raises(NonsenseError):
            X.cdf(num, strict=True)  # type: ignore[arg-type]

    assert X.cdf(-1, strict=False) < 1e-100
    assert X.cdf(-3, strict=False) < 1e-100
    assert X.cdf(21, strict=False) < 1e-100
    assert X.cdf(30, strict=False) < 1e-100

    assert X.cdf(12.5, strict=False) < 1e-100  # type: ignore[arg-type]
    assert X.cdf(22.3, strict=False) < 1e-100  # type: ignore[arg-type]


def test_calculate() -> None:
    """Test the use of P() to calculate probabilities of a binomial distribution."""
    X = B(20, 0.25)
    Y = B(14, 0.36)
    Z = B(50, 0.782)

    assert P(X == 2) == approx(X.pmf(2))
    assert P(X == 12) == approx(X.pmf(12))
    assert P(X != 4) == approx(1 - X.pmf(4))
    assert P(X != 17) == approx(1 - X.pmf(17))
    assert P(X < 2) == approx(sum(X.pmf(x) for x in (0, 1)))
    assert P(2 > X) == approx(sum(X.pmf(x) for x in (0, 1)))
    assert P(X < 10) == approx(sum(X.pmf(x) for x in range(10)))
    assert P(X <= 10) == approx(sum(X.pmf(x) for x in range(11)))
    assert P(3 < X <= 12) == approx(sum(X.pmf(x) for x in range(4, 13)))
    assert P(20 >= X) == 1
    assert P(X <= 20) == 1
    assert P(0 <= X <= 20) == 1
    assert P(7 <= X < 15) == approx(sum(X.pmf(x) for x in range(7, 15)))
    assert P(3 < X < 10) == approx(sum(X.pmf(x) for x in range(4, 10)))

    assert P(Y == 10) == approx(Y.pmf(10))
    assert P(Y != 6) == approx(1 - Y.pmf(6))
    assert P(Y < 10) == approx(sum(Y.pmf(x) for x in range(10)))
    assert P(Y > 10) == approx(sum(Y.pmf(x) for x in range(11, 15)))
    assert P(Y < 10) + P(Y > 10) == approx(1 - P(Y == 10))
    assert P(Y <= 4) == approx(Y.cdf(4))

    assert P(Z == 27) == approx(Z.pmf(27))
    assert P(Z != 33) == approx(1 - Z.pmf(33))
    assert P(Z <= 30) == approx(Z.cdf(30))
    assert P(Z > 30) == approx(1 - Z.cdf(30))
    assert P(Z >= 20) == approx(1 - Z.cdf(19))

    with pytest.raises(NonsenseError):
        P(10 < X < 8)

    with pytest.raises(NonsenseError):
        P(4 > X >= 12)

    with pytest.raises(NonsenseError):
        P(10 < X == 3)

    with pytest.raises(NonsenseError):
        P(3 == X > 10)

    with pytest.raises(NonsenseError):
        P(X == 3 > 10)

    with pytest.raises(NonsenseError):
        P(X == 3 < 10)

    with pytest.raises(NonsenseError):
        P(3 != X > 10)

    with pytest.raises(NonsenseError):
        P(X != 3 > 10)

    assert P(X >= 20) == P(X == 20)
    with pytest.raises(NonsenseError):
        P(X > 20)

    assert P(Y >= 14) == P(Y == 14)
    with pytest.raises(NonsenseError):
        P(Y > 14)

    assert P(Z >= 50) == P(Z == 50)
    with pytest.raises(NonsenseError):
        P(Z > 50)
