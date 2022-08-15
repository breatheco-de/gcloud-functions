<h1 align="center">
  <br>
  <a href="https://breatheco.de/"><img src="https://assets.breatheco.de/apis/img/images.php?blob&random&cat=icon&tags=breathecode,128" alt="BreatheCode" width="128"></a>
  <br>
  Shape of Image
  <br>
</h1>

<h4 align="center">Check the position and shape of the resource.</h4>

<p align="center">
  <a href="https://coveralls.io/github/breatheco-de/gcloud-shape-of-image">
    <img src="https://img.shields.io/coveralls/github/breatheco-de/gcloud-shape-of-image"
         alt="Coveralls">
  </a>

  <a href="https://github.com/breatheco-de/gcloud-shape-of-image/actions/workflows/linter.yml">
    <img src="https://github.com/breatheco-de/gcloud-shape-of-image/actions/workflows/linter.yml/badge.svg"
         alt="Linter">
  </a>

  <a href="https://github.com/breatheco-de/gcloud-shape-of-image/actions/workflows/test.yml">
    <img src="https://github.com/breatheco-de/gcloud-shape-of-image/actions/workflows/test.yml/badge.svg"
         alt="Test">
  </a>
</p>

## Documentation

### `Install dependencies`

```bash
python -m scripts.install
code .env # if your use Visual Studio Code the command is `code-insiders`
```

### `Start dev server`

```bash
pipenv run start
```

### `Run tests`

```bash
# Testing
pipenv run test ./breathecode/activity  # path

# Testing in parallel
pipenv run ptest ./breathecode/activity  # path

# Coverage
pipenv run cov breathecode.activity  # python module path

# Coverage in parallel
pipenv run pcov breathecode.activity  # python module path
```
