from setuptools import setup

with open("requirements.txt") as f:
    requirements = [
        line.strip()
        for line in f
        if line.strip() and not line.startswith("#")
    ]

setup(
    name='roam_to_git',
    packages=['roam_to_git'],
    version='0.2',
    license='MIT',
    description='Automatic RoamResearch backup to Git',
    author='Matthieu Bizien',
    author_email='oao2005@gmail.com',
    url='https://github.com/MatthieuBizien/roam-to-git',
    download_url='https://github.com/MatthieuBizien/roam-to-git/archive/v0.1.tar.gz',
    keywords=['ROAMRESEARCH', 'GIT', 'BACKUP'],
    install_requires=requirements,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Wiki',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    entry_points={
        'console_scripts': ['roam-to-git=roam_to_git.__main__:main'],
    }
)
