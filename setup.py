from setuptools import setup, find_packages # type: ignore

HYPEN_E_DOT = "-e ."
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements=[]

    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace("/n", " ") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
    name="mlproject",
    version="0.0.1",
    author="Ritwiz",
    author_email="ritwizmulay4612@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements("requirements.txt")
)