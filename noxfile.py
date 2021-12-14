"""
Configuration for nox testing
"""

import nox


@nox.session(
        reuse_venv=True
)
def tests(session):
    """
    Unit tests
    """
    session.install(
            'coverage'
    )
    session.install(
            '-r',
            'requirements.txt'
    )
    session.run(
            'coverage',
                'run',
                    '--branch',
                    '--source=src',
                    '-m',
                    'unittest',
                    'discover',
                    '-v',
                    '-s',
                    'tests',
            env={
                'PYTHONPATH': 'src'
            }
    )
    session.run(
            'coverage',
                'report'
    )


@nox.session(
        reuse_venv=True
)
def docs(session):
    """
    Documentation
    """
    session.install(
            'sphinx'
    )
    session.run(
            'sphinx-build',
                '-T',
                '-b',
                'html',
                'docs',
                'docs/_build'
    )


@nox.session(
        reuse_venv=True
)
def lint(session):
    """
    Static code analysis/style analysis
    """
    session.install(
        'pylint'
    )
    session.run(
        'pylint',
            'src',
            'tests'
    )
