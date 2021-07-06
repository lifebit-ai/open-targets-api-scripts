FROM continuumio/miniconda3@sha256:7838d0ce65783b0d944c19d193e2e6232196bada9e5f3762dc7a9f07dc271179
LABEL description="Docker image for using Open Targets APIs" \
      version="1.0.0" \
      maintainer="Eva Gradovich <eva@lifebit.ai>"

ARG ENV_NAME="opentargets-api-env"


RUN conda install -c conda-forge mamba -y
COPY environment.yml /
RUN mamba env create --quiet --name ${ENV_NAME} --file /environment.yml && conda clean -a

# Add conda installation dir to PATH (instead of doing 'conda activate')
ENV PATH /opt/conda/envs/${ENV_NAME}/bin:$PATH
RUN conda env export --name ${ENV_NAME} > ${ENV_NAME}_env.yml

WORKDIR /data/

CMD ["bash"]