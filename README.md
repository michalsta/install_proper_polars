A shell Python package that checks CPU flags and installs polars or polars-lts-cpu as appropriate.

The primary usecase is so that other modules can depend on that in their `setup.py` scripts instead of on polars - and have the proper version installed automatically.
