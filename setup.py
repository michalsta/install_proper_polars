from setuptools import setup


def get_polars():
    try:
        import cpuinfo
    except ModuleNotFoundError:
        return "polars"
    info = cpuinfo.get_cpu_info()
    if info["arch"] != "X86_64":
        return "polars"
    if "avx2" in info["flags"]:
        return "polars"
    else:
        return "polars-lts-cpu"



setup(
    name='install-proper-polars',
    version='0.1',
    packages=[],
    description='Empty package that will check for AVX2 flag, and install polars or polars-lts-cpu as appropriate',
    url="https://github.com/michalsta/install_proper_polars",
    author="Michał Startek",
    install_requires=[get_polars()],
    )
