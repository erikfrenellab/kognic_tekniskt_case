from setuptools import setup

with open("./requirements.txt", "r") as f:
    requirements = f.readlines()

setup(
    name="annotation_converter",
    version="0.1.0",
    packages=["annotation_converter"],
    package_dir={'': 'src'},
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'run_convert_api=annotation_converter.run_api:main'
        ]
    }
)