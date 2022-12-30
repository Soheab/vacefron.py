from re import MULTILINE as re_MULTILINE, search as re_search

from setuptools import setup  # type: ignore


readme = ""
with open("README.md") as f:
    readme = f.read()

version = ""
with open("vacefron/__init__.py") as f:
    version: str = re_search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re_MULTILINE).group(1)  # type: ignore

if not version:
    raise RuntimeError("version is not set")

requirements = ["aiohttp"]
_GITHUB_URL: str = "https://github.com/Soheab/vacefron.py"
_CLASSIFIERS = [
    "Development Status :: 5 - Production/Stable",
    "Framework :: aiohttp",
    "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Topic :: Internet",
    "Topic :: Software Development :: Libraries",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Utilities",
    "Typing :: Typed",
]
_KEYWORDS = [
    "vacefron",
    "discord",
    "api",
    "wrapper",
    "memes",
    "image",
    "discord.py",
    "rankcard",
    "rank",
    "card",
    "aiohttp",
    "leveling",
]
_URLS = {
    "Discord": "https://discord.gg/xJ2HRxZ",
    "Documentation": f"{_GITHUB_URL}/blob/master/docs.md",
    "Issue tracker": f"{_GITHUB_URL}/issues",
}
_PACKAGES = [
    "vacefron",
    "vacefron.types",
    "vacefron.models",
]
setup(
    author="Soheab",
    name="vacefron.py",
    url=_GITHUB_URL,
    description="A Wrapper for vacefron.nl/api written in Python.",
    license="MPL-2.0",
    long_description=readme,
    long_description_content_type="text/markdown",
    version=version,
    packages=_PACKAGES,
    download_url=f"{_GITHUB_URL}/archive/refs/tags/v{version}.tar.gz",
    install_requires=requirements,
    keywords=_KEYWORDS,
    project_urls=_URLS,
    python_requires=">=3.8",
    classifiers=_CLASSIFIERS,
)
