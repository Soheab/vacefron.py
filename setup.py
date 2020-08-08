from setuptools import setup  # type: ignore

with open('README.md') as f:
    readme = f.read()

setup(
    name = 'vacefron.py',
    description = 'A Wrapper for vacefron.nl/api written in Python.',
    long_description = readme,
    long_description_content_type = 'text/markdown',
    version = '1.0.1',
    packages = ['vacefron'],
    url = 'https://github.com/Soheab/vacefron.py',
    download_url = 'https://github.com/Soheab/vacefron.py/archive/v1.0.1.tar.gz',
    license = 'MIT',
    author = 'Soheab_',
    install_requires = ['aiohttp'],
    keywords = ['vacefron', 'discord', 'api'],
    project_urls = {
        "Discord":       "https://discord.gg/TtR32WT",
        "Source":        "https://github.com/Soheab/vacefron.py",
        "Documentation": "https://github.com/Soheab/vacefron.py/blob/master/docs.md",
        "Issue tracker": "https://github.com/Soheab/vacefron.py/issues",
        },

    python_requires = '>=3.6',
    )
