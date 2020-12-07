from setuptools import setup

import versioneer

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as fp:
    # replace == with >= and remove trailing comments and spaces
    reqs = [x.replace("==", ">=").split("#")[0].strip() for x in fp]
    reqs = [x for x in reqs if x]  # remove empty strings

if __name__ == "__main__":
    setup(
        author_email="packages@byte-physics.de",
        author="Thomas Braun",
        classifiers=[
            "Development Status :: 5 - Production/Stable",
            "Environment :: Console",
            "Intended Audience :: Science/Research",
            "License :: Free To Use But Restricted",
            "Operating System :: OS Independent",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Topic :: Scientific/Engineering",
        ],
        cmdclass=versioneer.get_cmdclass(),
        description="Convert various patch-clamp data formats to NWBv2",
        entry_points={"console_scripts": ["x-to-nwb=x_to_nwb:convert_cli"]},
        install_requires=reqs,
        long_description_content_type="text/markdown; charset=UTF-8",
        long_description=long_description,
        name="x-to-nwb",
        package_dir={"": "src"},
        packages=["x_to_nwb"],
        python_requires=">=3.6",
        url="https://github.com/byte-physics/x-to-nwb",
        version=versioneer.get_version(),
    )
