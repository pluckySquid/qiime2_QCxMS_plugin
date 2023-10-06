from setuptools import setup, find_packages

setup(
    name='qiime2-qcxms-plugin',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'qiime2.plugins':
        ['qcxms-plugin=qcxms_plugin.plugin_setup:plugin']
    },
    install_requires=[
        'qiime2',
    ],
    author='Yunshu Wang',
    author_email='ywang1127@ucr.edu',
    description='A QIIME 2 plugin for QCxMS.',
    url='https://example.com',
)
