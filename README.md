#  ContentVerse
This repository supports vision engine of DCE.

## Python
In order to run the project,` python 3.10` is required. All the python libraries essential to this repo are included in `requirements.txt`.

It is recommended to use an environment manager such as [conda](https://docs.conda.io/en/latest) in order to control the python environment and use a minimal setup.

## Local Dev Environment
In order to set up local dev environment run `pip3 install -r requirements.dev_local.txt`

Further, specific environment variables would be setup in config `.<env>` file. A draft version of the file is available in the same location for reference

## Pre-commit
We have set up pre-commit configuration to ensure that code is formatted properly and passes flake8 (lint), mypy and other standard checks. To learn more refer [Pre-commit Introduction](https://pre-commit.com/#intro).

## Docker

We use [docker](https://docs.docker.com/get-docker/) for deploying the repository. Docker keeps the code isolated and scalable.

Install docker locally in order to be able to build and run the Dockerfile and container.

Once docker is installed, build image by running `docker build -t <repository-name> . --build-arg BRANCH=<env>`. This would build a docker image on the local machine.

To run the image after building run `docker run -it <repository-name>`.

Contribution to the Project
Contribution must be done via merge requests on `dev` branch. Every merge request must be approved by repository owner.

Commit messages must follow the [conventional_commit_message_format](https://www.conventionalcommits.org/en/v1.0.0/)
