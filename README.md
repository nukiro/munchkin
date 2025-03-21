# Munchkin

## Setup

### Project

```shell
# install python if it is not installed yet
python3 --version
# create a virtual environment
python3 -m venv venv
# activate the virtual environment
source venv/bin/activate
# install pip-tools library
pip install pip-tools
# install project dependencies
pip install -r requirements.txt
# lastly install our package
pip install -e .
```

### Database

```shell
# run migrations
```

## Development

### Main branch = develoment branch

Latest releases branch merged. It is the branch that will be deployed into dev environment.

### Starting a new release

```shell
# from main create a new branch
git co -b release/vX.Y.Z
```

### Creating a new feature

```shell
# from the release branch
# create a new branch to build the new feature
# which later will be merge into the release branch
git co -b feature/name-of-the-feature
# to split it in small PRs/MRs, create small new branches
# without any branch/comming naming requirements
git co -b small-feat-into-the-feature-dev
git commit
# once all the small changes are done squash commit into the feature branch
git co feature/name-of-the-feature
git merge --squash small-feat-into-the-feature-dev
# once all the feature job is done, merge feature branch into the release branch
git co release
```

### Repository Branch Name Convention

Good branch names following the above conventions:

```txt
feature/T-456-user-authentication
bugfix/T-789-fix-header-styling
hotfix/T-321-security-patch
release/v2.0.1
docs/T-654-update-readme
```

### Adding a new library to the project

Add library in `requirements.in` file.

```shell
# compile requirements via pip-tools
pip-compile requirements.in
# this will add all required dependencies to the requirements.txt file
pip install -r requirements.txt
```

### `pre-commit`

[Documentation](https://pre-commit.com/)

```shell
pre-commit install
# pre-commit installed at .git/hooks/pre-commit
pre-commit run --all-files
# [INFO] Initializing environment for https://github.com/pre-commit/pre-commit-hooks.
# [INFO] Initializing environment for https://github.com/psf/black.
# [INFO] Installing environment for https://github.com/pre-commit/pre-commit-hooks.
# [INFO] Once installed this environment will be reused.
# [INFO] This may take a few minutes...
# [INFO] Installing environment for https://github.com/psf/black.
# [INFO] Once installed this environment will be reused.
# [INFO] This may take a few minutes...
# check yaml...........................................(no files to check)Skipped
# fix end of files.........................................................Passed
# trim trailing whitespace.................................................Passed
# don't commit to branch...................................................Passed
# black....................................................................Passed
```

## Database Modeling

- Private field (PKs and FKs) names with underscore: `_uuid`, `_organization`.
- FK fields without `uuid` sufix, just the name.
- External IDs as `id`. For primary and unique system keys `uuid`.
- Shadow tables for audit purpose: `_action` (INSERT/UPDATE/DELETE) and `_at` (integer unix timestamp)
