# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "base"
  config.vm.provision :shell, :path => ".vagrant/provision.sh"
   config.vm.network "forwarded_port", guest: 5000, host: 8080
end
