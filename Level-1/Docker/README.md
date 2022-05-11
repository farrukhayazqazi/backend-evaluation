 ## Docker

 ###### 1. Compare different kinds of docker image families. Alpine, Slim, Stretch, Buster, Jessie, Bullseye. What does this mean? How are they different? What advantage do they provide over the others?
 ---

The difference b/w all the docker image families are the underlying operating system.

**Stretch, Buster and Jessie:**

    These are the code names for different debain releases. Debian release (10.4) codename is "Buster". "Stretch" is the  codename for all version 9 releases and "Jessie" is used for all version 8 variations.

**Bullseye:**

    Future version of debian release that is not stable yet.

**Alpine:**

    Alpine images are alpine linux project based. The os that is built specifically for containers use case. They were popular because of their tiny image size. 

**Slim:**

    The slim image is the diminshed version of full docker image. This images installs packages to run your tool.

---

###### 2. Difference between Entrypoint and CMD directive in a Dockerfile?

**CMD:**
    you can override default parameters from the docker command line interface (CLI) when a container is running.

**Entrypoint:**
    you cannot override default parameters here when docker container runs with CLI parameters.

Any Docker image must have an ENTRYPOINT or CMD declaration for a container to start. Though the ENTRYPOINT and CMD instructions may seem similar at first glance, there are fundamental differences in how they build container images.

---

###### 3. Explain this command written inside a Dockerfile:RUN mkdir /app/django/helloworld

This comman makes a directory in called "helloworld" inside /app/django.

---

###### 4. Explain the concept of layering in Docker images/containers?


**image layer:**

    docker image is built up from a series of layers. Each layer represents an instruction in the image’s Dockerfile. Each layer except the very last one is read-only.

**container layer:**

    The layers are stacked on top of each other. When you create a new container, you add a new writable layer on top of the underlying layers. This layer is often called the “container layer”

    The major difference between a container and an image is the top writable layer.

    When the container is deleted, the writable layer is also deleted. The underlying image remains unchanged.
