import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
  name = 'blurlab',         # How you named your package folder (MyLib)
  packages = ['blurlab'],   # Chose the same as "name"
  include_package_data=True,
  version = '0.4',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Fix some issues from pyblur',   # Give a short description about your library
  long_description=README,
  long_description_content_type="text/markdown",
  author = 'jayroxis',                   # Type in your name
  author_email = 'bujie314@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/jayroxis/blurlab',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/jayroxis/blurlab/archive/refs/tags/v0.1.0.tar.gz',    # I explain this later on
  keywords = ['blur', 'image', 'cv', 'vision', 'processing', 'convolution'],   # Keywords that define your package best
  install_requires=["scikit-image", "opencv-python", "Pillow"],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
  package_data={"": [".pkl"]},
  python_requires='>=3',
)