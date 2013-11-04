grumble
=======

A Small, RESTful API wrapper for Mumble servers.

The aim is to make a simple Flask based RESTful API to reduce the effort and development time needed to interface with Mumble servers for simple administration tasks. The API will cover the majority of the available ICE RPC functions in Mumble, excluding the callback functionality.

This application is still under heavy development and it is suggested you do not use it within a production environment.


Development Environment
-----------------------

Grumble makes use of Vagrant for its development environment and a simple configuration has been provided to bootstrap a Ubuntu VM running a basic Mumble server.

To initialize the VM run `vagrant up` in the project root directory.