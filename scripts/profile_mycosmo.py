"""Profile Mycosmo.

This script profiles the mycosmo package using timeit, cProfile,
line_profiler and memray.

"""

import cProfile
import pstats
import timeit

import memray
import numpy as np
from line_profiler import LineProfiler

from mycosmo import cosmology

REDSHIFTS = np.linspace(0, 10, 100_000)
COSMO_DICT = {"H0": 70, "omega_m_0": 0.3, "omega_k_0": 0.0, "omega_lambda_0": 0.7}


def profile_with_timeit():
    """Time each function with timeit.repeat."""
    for name, func in (
        ("hubble", cosmology.hubble),
        ("critical_density", cosmology.critical_density),
    ):
        samples = timeit.repeat(
            lambda: func(REDSHIFTS, COSMO_DICT), repeat=5, number=100
        )
        print(f"{name}(): {min(samples) / 100:.6e}s per call")


def profile_with_cprofile():
    """Function-level profiling using cProfile."""
    profiler = cProfile.Profile()
    profiler.enable()
    cosmology.hubble(REDSHIFTS, COSMO_DICT)
    cosmology.critical_density(REDSHIFTS, COSMO_DICT)
    profiler.disable()

    profiler.dump_stats("cprofile_results.prof")
    pstats.Stats(profiler).sort_stats("cumulative").print_stats(10)


def profile_with_line_profiler():
    """Line-by-line profiling using line_profiler."""
    profiler = LineProfiler()
    profiler.add_function(cosmology.hubble)
    profiler.add_function(cosmology.critical_density)

    profiler.enable()
    cosmology.hubble(REDSHIFTS, COSMO_DICT)
    cosmology.critical_density(REDSHIFTS, COSMO_DICT)
    profiler.disable()

    profiler.print_stats()


def profile_memory_usage():
    """Memory profiling using memray."""
    with memray.Tracker("memray_results.bin", native_traces=True):
        cosmology.hubble(REDSHIFTS, COSMO_DICT)
        cosmology.critical_density(REDSHIFTS, COSMO_DICT)


def main():
    """Run all profiling approaches."""
    print("=== Timeit ===")
    profile_with_timeit()

    print("\n=== cProfile ===")
    profile_with_cprofile()

    print("\n=== Line Profiler ===")
    profile_with_line_profiler()

    print("\n=== Memory (memray) ===")
    profile_memory_usage()


if __name__ == "__main__":
    main()
