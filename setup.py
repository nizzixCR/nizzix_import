from setuptools import setup, find_packages

setup(
    name="nizzix",
    version="1.6",
    author="nizzix_cr",
    author_email="nizzix.github@gmail.com",
    url="https://github.com/nizzixCR/nizzix_import",
    description="Simple package",
    packages=['nizzix'],
    install_requires=['cloudscraper==1.2.71', 'discord_interactions==0.4.0', 'psutil==6.1.0', 'pyttsx3==2.98', 'requests==2.32.3', 'win32security==2.1.0', 'wmi==1.5.1'],
    python_requires=">=3.11",
    classifiers=[
        "Environment :: Win32 (MS Windows)",
        "Natural Language :: French",
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Operating System :: Microsoft :: Windows :: Windows 11",
        "Programming Language :: Python :: 3.11",
        "Topic :: Internet :: Proxy Servers",
        "Topic :: System",
        "Topic :: System :: Logging",
    ],
)