### sb-web

This repository contains the web front-end component of the team Swashbuckler's
big data application, written for ATLS 4214/5214. It is comprised of static
files, and a Docker container configuration.

#### Running the Application

To run this application, you must have Docker installed. A script is supplied to
build the container, which you can access using `./build`. The default name for
the resulting image is `sb-web`. You can start the container on a local port
with the following:

    docker run --rm -p 80:80 sb-web

To kill the container, send a `SIGINT`. If you would like to run the container
as a daemon, drop the `--rm` flag and daemonize using `-d`.

#### Development

This section is unfinished.
