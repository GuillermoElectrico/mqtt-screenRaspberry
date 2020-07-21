import sys
from setuptools import setup

try:
    import pypandoc
    readme = pypandoc.convert('README.md', 'rst')
    readme = readme.replace("\r", "")
except ImportError:
    import io
    with io.open('README.md', encoding="utf-8") as f:
        readme = f.read()

setup(name='mqtt_to_influxdb',
      version=1.1,
      description='Change status screen with mqtt menssages ',
      long_description=readme,
      url='https://github.com/GuillermoElectrico/mqtt_to_influxdb',
      download_url='',
      author='Guillermo Electrico',
      author_email='electrico@outlook.com',
      platforms='Raspberry Pi',
      classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: GNU License v3',
        'Operating System :: Raspbian',
        'Programming Language :: Python :: 3.5'
      ],
      keywords='MQTT screen pi',
      install_requires=[]+(['setuptools', 'pyyaml', 'ez_setup', 'paho-mqtt', 'rpi-backlight'] if "linux" in sys.platform else []),
      license='MIT',
      packages=[],
      include_package_data=True,
      tests_require=[],
      test_suite='',
      zip_safe=True)
