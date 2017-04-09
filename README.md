### sb-web [![Build Status](https://travis-ci.com/CUBigDataClass/sb-web.svg?token=to3Uk4kQPXFNMbsHvZRp&branch=master)](https://travis-ci.com/CUBigDataClass/sb-web)

This repository contains the web front-end component of the team Swashbuckler's
big data application, written to fulfill requirements of the ATLS 4214/5214 term
project. It is comprised of a Flask application and NGINX server, which is
deployed using WSGI for scaling in production.

#### Running the Application

To run this application, you must have Docker installed, and the daemon must be
running. A script has been supplied with this repository to build the image,
which can be accessed with `./build`. The default name for the image that is
generated is `sb-web`. The container can then be launched on a local port using
the following:

    docker run --name sb-web --rm -it -p 80:80 sb-web

To kill the container, send a `SIGINT`. If you would like to run the container
as a daemon, drop the `--rm` flag and daemonize using `-d`.

#### Development

For the time being, development for the container can be done by mounting the
application within the container, overwriting the standard mount point where
files are placed when the production container is built. This can be done with
the following:

    docker run --rm -it -v "$PWD"/app:/app -p 80:80 sb-web

If you already have a container named `sb-web`, you will have to remove it. That
is achievable using `docker rm sb-web`. To view the logs of a container, use
`docker logs sb-web`. To view the logs live, use `docker logs -f sb-web`.
Otherwise, don't start the container as a daemon.
