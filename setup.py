from setuptools import setup
import setuptools

setup(name='haven-ai',
      version='0.3.9',
      description='Manage large-scale experiments',
      url='https://github.com/haven-ai/haven-ai',
      maintainer='Issam Laradji',
      maintainer_email='issam.laradji@gmail.com',
      license='MIT',
      scripts=['./scripts/haven'],
      packages=setuptools.find_packages(),
      zip_safe=False,
      python_requires='>=3.5',
      install_requires=[
        'requests>=0.0',
        'ipywidgets>=0.0',
        'tqdm>=0.0',
        'matplotlib>=0.0',
        'numpy>=0.0',
        'opencv-python-headless>=0.0',
        'pandas>=0.0',
        'Pillow>=0.0',
        'scikit-image>=0.0',
        'scikit-learn>=0.0',
        'scipy>=0.0',
        'sklearn>=0.0',
        'torch>=0.0',
        'torchvision>=0.0',
        'notebook >= 4.0',
        'jupyter>=0.0',
      ]),
