FROM python:3.9

LABEL org.opencontainers.image.source https://github.com/permafrostdiscoverygateway/viz-workflow

WORKDIR /usr/local/share/app

COPY requirements.txt .
RUN pip install -r requirements.txt

# All we should need to do is copy the following three files. However, at the
# moment there are several in-flight PRs to the parsl library that I want to
# include, so using the more complicated setup below instead so I can run with
# a local version of parsl that contains the patched changes.
#COPY workflow_config.py .
#COPY parsl_workflow.py .
#COPY parsl_config.py .

# TODO(shishi): Temporary workaround to use local parsl - remove and replace
# with above once an official parsl release contains all the changes.
COPY parsl/requirements.txt parsl-requirements.txt
RUN pip install -r parsl-requirements.txt

COPY workflow_config.py leader/workflow_config.py
COPY parsl_workflow.py leader/parsl_workflow.py
COPY parsl_config.py leader/parsl_config.py
COPY parsl/parsl/ leader/parsl/

COPY parsl/parsl/executors/high_throughput/ worker/
COPY parsl/parsl/ worker/parsl/
