# student-ml-api

Student: Rayyan Qamar Hashmi  
Roll number: 23I0815  
Class: CSB

This is a small Flask API for the MLOps assignment.

## Run the project

```bash
pip install -r requirements.txt
pytest
python app.py
```

Open `http://localhost:5000/health` to check the API.

Send this JSON to `/predict`:

```json
{"value": 10}
```

The answer is:

```json
{"input": 10, "prediction": 20}
```

## Run with Docker

```bash
docker build -t student-ml-api:1.0.0 .
docker run -d --name student-ml-api -p 5000:5000 student-ml-api:1.0.0
```

Then check `http://localhost:5000/health`.

## GitHub Actions

The CI workflow runs for pull requests to `main`. It installs the requirements, runs the tests, and checks the Docker build. It does not upload an image.

The release workflow runs when a tag such as `v1.0.0` is pushed. It runs the tests, builds the image, and uploads the version and `latest` tags to GitHub Container Registry. The version is taken from the tag automatically.

## Git workflow

Work should be done on a feature branch. Open a pull request to `main`, wait for CI, get a review, and then merge. Direct pushes to `main` should be blocked with GitHub branch protection.

Suggested branch protection settings:

- Require a pull request.
- Require the CI checks to pass.
- Require one review.
- Do not allow force pushes.

For the assignment, record the real pull request number, merge commit, Git tag, image tag, and image digest after using GitHub.
