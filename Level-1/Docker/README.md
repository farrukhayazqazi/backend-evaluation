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