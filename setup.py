from setuptools import setup, find_packages

setup(
    name='medical-diagnosis-system',
    version='0.1',
    packages=find_packages(),
    description='A simple rule-based medical diagnosis system that assists in diagnosing common diseases based on symptoms.',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/medical-diagnosis-system',  # Replace with your GitHub URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)