import setuptools

setuptools.setup(
    name='runcmd',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
