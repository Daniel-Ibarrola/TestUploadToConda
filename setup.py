"""
ProjectName
A short description of the project.
"""
import sys
from setuptools import setup, find_packages
import versioneer

short_description = __doc__.split("\n")

# from https://github.com/pytest-dev/pytest-runner#conditional-requirement
needs_pytest = {'pytest', 'test', 'ptr'}.intersection(sys.argv)
pytest_runner = ['pytest-runner'] if needs_pytest else []

try:
    with open("README.md", "r") as handle:
        long_description = handle.read()
except:
    long_description = "\n".join(short_description[2:])


setup(
    name='test_upload_to_conda',
    author='UIBCDF Lab',
    author_email='uibcdf@gmail.com',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    package_dir={'test_upload_to_conda': 'test_upload_to_conda'},
    packages=find_packages(),
    include_package_data=True,
    package_data={'test_upload_to_conda': ['data']},
    scripts=[],
    setup_requires=[] + pytest_runner,
    platforms=['Linux',
                'Mac OS-X',
                'Unix',
                'Windows',
    ],
    python_requires=">=3.7",
    download_url ='https://github.com/Daniel-Ibarrola/TestUploadToConda',
    license='MIT',
    description=short_description[0],
    long_description=long_description,
    long_description_content_type="text/markdown",
)

