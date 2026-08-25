import pytest

from mycosmo.cosmology import hubble

FID_COSMO = {
    "H0": 70,
    "omega_m_0": 0.3,
    "omega_k_0": 0.0,
    "omega_lambda_0": 0.7,
}


@pytest.mark.parametrize(
    "redshift, expected",
    [
        (0.0, 70),
        (0.5, 91.60),
        (1.0, 123.24),
    ],
)
def test_hubble(redshift, expected):
    assert hubble(redshift, FID_COSMO) == pytest.approx(expected, abs=0.01)
