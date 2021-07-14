from setuptools import setup, find_packages
from uilib.fileIO import appVersionStr

try:
    from pyqt_distutils.build_ui import build_ui
    cmdclass = {'build_ui': build_ui}
except ImportError:
    print('pyqt_distutils not found, build_ui command will be unavailable')
    build_ui = None  # user won't have pyqt_distutils when deploying
    cmdclass = {}

setup(
    name='OpenPep',
    version=appVersionStr,
    license='GPLv3',
    packages=find_packages(),
    url='https://github.com/aushe02/OpenPep',
    description='An open-source propellant evaluation Program for rocket motor experimenters',
    long_description=open('README.md').read(),
    cmdclass=cmdclass
)