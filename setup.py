from setuptools import setup

setup(
    name="pretalx_sphinx_theme",
    version="0.0.0",
    description="Sphinx theme used by pretalx.",
    long_description=open("README.rst").read(),
    author="Tobias Kunze",
    author_email="r@rixx.de",
    url="https://github.com/pretalx/pretalx_sphinx_theme",
    packages=["pretalx_sphinx_theme"],
    include_package_data=True,
    install_requires=["Sphinx>1.3"],
    license="Apache License 2.0",
    classifiers=(
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
    ),
)
