import glob

import nox

@nox.session
def tests(session):
    install_package(session)
    session.install("-r", "test-requirements.txt")
    session.run("pytest")


@nox.session
def build_package(session):
    session.run("rm", "-rf", "build", "dist")
    session.install("-r", "dist-requirements.txt")
    session.run("python", "setup.py", "bdist_wheel")


def install_package(session):
    whl_files = glob.glob("dist/*.whl")
    assert len(whl_files) == 1
    installable = whl_files[0]
    session.install(installable)