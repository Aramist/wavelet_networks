from setuptools import setup

setup(
    name='wavelet_networks',
    version="1.0.0",
    description="Scale Equivariant Learning From Raw Waveforms",
    url="https://github.com/dwromero/wavelet_networks/",
    author="David W. Romero",
    license="MIT",
    packages=[
        "wavelet_networks",
        "wavelet_networks.bsplines",
        "wavelet_networks.groups",
        "wavelet_networks.nn",
        "wavelet_networks.nn.functional",
    ],
    install_requires=[
        "torch",
        "torchaudio",
        "numpy",
        "scipy",
        "matplotlib",
        "jupyter",
    ],
)