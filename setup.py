from setuptools import setup

setup(
    name="eflint",
    version="0.2.6",
    entry_points={
        "console_scripts": [
            "eflint=eflint.core:main",
        ]
    },
)
