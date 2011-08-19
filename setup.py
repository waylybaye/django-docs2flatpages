from setuptools import setup, find_packages

setup(
    name="django-docs2flatpages",
    version = "0.1",
    author = "Baye Wayly",
    author_email = "havelove@gmail.com",
    description="Generate django flatpages from rst/textile/markdown docs.",
    packages= find_packages(),
    license = "BSD",
)
