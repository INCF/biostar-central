BioStar Q&A Version 2.0
=======================

BioStar is a [Python][python] and [Django][django] based Q&A software.
Our goal is to create a simple, generic, flexible and extensible Q&A
framework.

This is the software that runs the Biostars Bioinformatics Q&A at: http://www.biostars.org

Requirements: `Python 2.7`

Documentation
-------------

The documentation is maintained at:

http://docs.biostars.org/

The source for the documentation can be found in  the `docs` folder.

Quick Start
------------

From the biostar source directory:

    # Install the requirements.
    pip install --upgrade -r conf/requirements/base.txt

    # Load the environment variables.
    source conf/defaults.env

    # Initialize database, import test data, index for searching and run the server.
    ./biostar.sh init import index run

Visit `http://locahost:8080` to see the site loaded with default settings.

Enjoy.


Hacking
-------

[VirtualBox][virtualbox] and [Vagrant][vagrant] are assumed to be installed beforehand, after that, to 
spawn a local developer instance, copy and paste the following line in your terminal:

	git clone https://github.com/ialbert/biostar-central biostar-central && cd conf && vagrant up

While it is running, you can read [what is going on under the hood][nimiqdeploy].

[django]: http://www.djangoproject.com/
[python]: http://www.python.org/
[nimiqdeploy]: http://nimiq.github.io/my-summer-of-code/deployment-sketch/
[virtualbox]: https://www.virtualbox.org/
[vagrant]: http://www.vagrantup.com/

Production
----------

TODO:
* Integrate django-whitenoise as ialbert pointed out on `https://github.com/nimiq/biostar-central/commit/a10800166d63#commitcomment-6160730`
* Add elasticsearch Dockerfile.
* Basically, devel and production should be as seamless as possible (check marceldegraaf post for inspiration).
