import pytest
from astropy.cosmology import WMAP9 as cosmo

from mycosmo.cosmology import critical_density, hubble

REDSHIFTS = [0.0, 0.5, 1.0]

COSMO_DICT = {
    "H0": cosmo.H0.value,
    "omega_m_0": cosmo.Om0,
    "omega_k_0": cosmo.Ok0,
    "omega_lambda_0": cosmo.Ode0,
}


class TestAstropy:
    """Test Astropy.

    Class to test ``mycosmo`` routines with respect to those provided in Astropy.
    """

    @pytest.mark.parametrize("redshift", REDSHIFTS)
    def test_hubble(self, redshift):
        """Test Hubble function."""
        h_mycosmo = hubble(redshift=redshift, cosmo_dict=COSMO_DICT)
        h_astropy = cosmo.H(redshift).value

        assert h_mycosmo == pytest.approx(h_astropy, abs=0.1)

    @pytest.mark.parametrize("redshift", REDSHIFTS)
    def test_critical_density(self, redshift):
        """Test Critical Density function."""
        rho_crit_mycosmo = critical_density(redshift=redshift, cosmo_dict=COSMO_DICT)
        rho_crit_astropy = cosmo.critical_density(redshift).value * 1e3

        assert rho_crit_mycosmo == pytest.approx(rho_crit_astropy, rel=1e-2)
