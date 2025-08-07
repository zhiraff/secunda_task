FROM python:3.12

ARG https_proxy
ARG http_proxy
ARG version
ARG commit

ENV PYTHONUNBUFFERED 1
ARG INSTALL_PATH=/srv/rest_api
COPY . $INSTALL_PATH/.


WORKDIR $INSTALL_PATH
RUN pip cache purge
RUN pip --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --default-timeout=1000 install --user --no-cache-dir -r requirements.txt
EXPOSE 8000
ENV PYTHONPATH "${PYTHONPATH}:${INSTALL_PATH}"
CMD ["/root/.local/bin/uvicorn", "--reload", "main:app"]