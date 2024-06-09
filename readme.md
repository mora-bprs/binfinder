# binfinder

## tracking

- [x] repo directory structure
- [x] setup pre-commit
- [x] select camera stream
- [ ] check and list models and select one for inference
- [ ] port inference from jupyter notebook to python script
- [ ] setup logging
- [ ] proper ruff formatting and lsp setup
- [ ] tests and asserts
- [ ] proper setup instructions for each platform
- [ ] low latency webcam [refer](https://stackoverflow.com/questions/70597020/lower-latency-from-webcam-cv2-videocapture)
- [ ] setup github actions

## backburner

- [ ] docker setup
- [ ] nix enhancement
- [ ] find a way for seamless issue creation

## project files

### directory structure

```
root
├── src
│   ├── binfinder
│   │   ├── __init__.py -- starting point
│   │   ├── __main__.py -- main function
│   │   ├── config -- configuration files
│   │   │   ├── __init__.py
│   │   │   ├── camera.py
│   │   ├── helpers -- helper functions
│   │   │   ├── __init__.py
│   │   │   ├── camera.py
│   ├── tests -- test files wip
│   ├── data
│   │   ├── result -- annotated results, graphs and logs
│   │   ├── test -- test images dataset
│   │   ├── train -- train images dataset
│   │   ├── weights -- model weights

```

### `.commitlintrc.json` and `.releaserc.json`

these files are used by `semantic-release` to determine the type of the next release. the `.commitlintrc.json` file is used to lint the commit messages. the `.releaserc.json` file is used to determine the version of the next release based on the commit messages. to lint commit messages, this project uses the default configuration of `@commitlint/config-conventional`.

### `.python-version` file

the `.python-version` file contains the python version used in this project. this project has been built with using `pyenv` as python version manager.

### `.pre-commit-config.yaml` file

this file is used by `pre-commit` to determine the hooks that will be run before each commit. the hooks are defined in the `hooks` section of the file. the hooks are run in the order they are defined in the file.

### `.github/workflows` folder

this repository uses github actions for ci/cd. ci is composed of `lint` with pre-commit and `test` with pytest. release is composed of `lint`, `test`, `release` with semantic-release.

- lint is done with [pre-commit](https://pre-commit.com/). to run lint locally, run `pre-commit run --all-files`.
- test is done with [pytest](https://docs.pytest.org/en/8.0.x/). to run test locally, run `pytest`. or poetry run `pytest` if you use poetry as package manager.
- release is done with [semantic-release](https://github.com/semantic-release/semantic-release)
