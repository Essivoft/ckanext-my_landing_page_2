from setuptools import setup, find_packages

setup(
    name='ckanext-my_landing_page',
    version='0.0.1',
    description='A CKAN extension that modifies the homepage layout',
    author='Your Name',
    author_email='your.email@example.com',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    entry_points=\
    """
    [ckan.plugins]
    my_landing_page=ckanext.my_landing_page.plugin:MyLandingPagePlugin
    """,
)
