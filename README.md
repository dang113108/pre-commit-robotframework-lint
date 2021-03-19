pre-commit Robot Framework Lint wrapper
==============================

This is a [pre-commit](https://github.com/pre-commit) hook that will run
the [Robot Framework Lint tool](https://github.com/dang113108/robotframework-lint) on all of your robot files.

* [pre-commit](https://github.com/pre-commit)
* [Robot Framework](https://robotframework.org)


Add this to your ``.pre-commit-config.yaml`` file

    -   repo: git://github.com/dang113108/pre-commit-robotframework-lint
        rev: <commit_id or tag>
        hooks:
        -   id: robotframework-lint
            args:
            - -i=RequireKeywordDocumentation
