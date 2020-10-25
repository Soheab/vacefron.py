from re import search, MULTILINE

from setuptools import setup  # type: ignore

with open("README.md") as f:
    readme = f.read()

# source: https://github.com/Rapptz/discord.py/blob/master/setup.py#L9-L10
with open("vacefron/__init__.py") as f:
    content = f.read()
    version = search(
            r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', content, MULTILINE
            ).group(1)
    author = search(r'^__author__\s*=\s*[\'"]([^\'"]*)[\'"]', content, MULTILINE).group(
            1
            )
    _license = search(
            r'^__license__\s*=\s*[\'"]([^\'"]*)[\'"]', content, MULTILINE
            ).group(1)

setup(
        name = "vacefron.py",
        description = "A Wrapper for vacefron.nl/api written in Python.",
        long_description = readme,
        long_description_content_type = "text/markdown",
        version = version,
        packages = ["vacefron"],
        url = "https://github.com/Soheab/vacefron.py",
        download_url = f"https://github.com/Soheab/vacefron.py/archive/v{version}.tar.gz",
        license = _license,
        author = author,
        install_requires = ["aiohttp"],
        keywords = ["vacefron", "discord", "api", "wrapper", "memes", "image", "discord.py"],
        project_urls = {
            "Discord": "https://discord.gg/xJ2HRxZ",
            "Source": "https://github.com/Soheab/vacefron.py",
            "Documentation": "https://github.com/Soheab/vacefron.py/blob/master/docs.md",
            "Issue tracker": "https://github.com/Soheab/vacefron.py/issues",
            },
        python_requires = ">=3.6",
        )
