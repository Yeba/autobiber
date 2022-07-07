import setuptools
import os

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

about = {}
with open("autobiber/_version.py") as f:
    exec(f.read(), about)
os.environ["PBR_VERSION"] = about["__version__"]

setuptools.setup(
    name="autobiber",
    version=about["__version__"],
    author='yjliu',
    author_email='yjliu045@stu.suda.edu.cn',
    description="A tool for find bibtex via dblp",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Yeba/autobiber",
    py_modules=["autobiber"],
    packages=setuptools.find_packages(),
    install_requires=['argparse',
                      'fake_useragent',
                      'requests',
                      'urllib3',
                    ],
    entry_points = {
        'console_scripts': ['autobiber=autobiber.autobiber:main'],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    package_data={'autobiber': ['autobiber.py', 'utils.py']},
)