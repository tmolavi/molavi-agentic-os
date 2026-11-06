from setuptools import setup, find_packages

setup(
    name="molavi-agentic-os",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "molavi-agentic-os=molavi_agentic_os.cli:main",
        ],
    },
)
