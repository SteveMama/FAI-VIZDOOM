import setuptools
from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()
    descr_lines = long_description.split("\n")
    descr_no_gifs = []  # gifs are not supported on PyPI web page
    for dl in descr_lines:
        if not ("<img src=" in dl and "gif" in dl):
            descr_no_gifs.append(dl)

    long_description = "\n".join(descr_no_gifs)


_atari_deps = ["gymnasium[atari, accept-rom-license]"]
_mujoco_deps = ["gymnasium[mujoco]", "mujoco<=2.3.3"]
_envpool_deps = ["envpool"]

_docs_deps = [
    "mkdocs-material",
    "mkdocs-minify-plugin",
    "mkdocs-redirects",
    "mkdocs-git-revision-date-localized-plugin",
    "mkdocs-git-committers-plugin-2",
    "mkdocs-git-authors-plugin",
]

setup(
    # Information
    name="modified Sample Factory for FAI project",
    description="Reinforcement Learning in Action",
    long_description=long_description,
    ,
    install_requires=[
        "numpy>=1.18.1,<2.0",
        "torch>=1.9,<3.0,!=1.13.0",
        "gymnasium>=0.27,<1.0",
        "pyglet",  # gym dependency
        "tensorboard>=1.15.0",
        "tensorboardx>=2.0",
        "psutil>=5.7.0",
        "threadpoolctl>=2.0.0",
        "colorlog",
        "signal-slot-mp>=1.0.3,<2.0",
        "filelock",
        "opencv-python",
        
    ],
    extras_require={
        # some tests require Atari and Mujoco so let's make sure dev environment has that
        "dev": ["black", "isort>=5.12", "pytest<8.0", "flake8", "pre-commit", "twine"]
        + _docs_deps
        + _atari_deps
        + _mujoco_deps,
        "atari": _atari_deps,
        "envpool": _envpool_deps,
        "mujoco": _mujoco_deps,
        "vizdoom": ["vizdoom<2.0", "gymnasium[classic_control]"],
    },
    package_dir={"": "./"},
    packages=setuptools.find_packages(where="./", include=["sample_factory*", "sf_examples*"]),
    include_package_data=True,
    python_requires=">=3.8",
)
