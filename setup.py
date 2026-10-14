from setuptools import setup

setup(
    name="project-b-utils",
    version="1.0.0",
    # каталог src сам является пакетом, поэтому find_packages(where="src")
    # не находит ничего; пакет project_b_utils явно сопоставляется с каталогом src
    packages=["project_b_utils"],
    package_dir={"project_b_utils": "src"},
    author="Гетьман В. С.",
    description="Утилиты для работы с датами и строками",
    python_requires=">=3.8",
)
