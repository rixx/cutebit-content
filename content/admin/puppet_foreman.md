Title: Installing Foreman on an existing Puppet Master
Date:   2015-01-31
Category: Administration
Tags: administration,foreman,puppet
Slug: foreman_puppet
Lang: en
Authors: rixx
Summary: Puppet and Foreman documentation tends to be a bit … spread out, so here you'll find a comprehensive guide to installing Foreman on an existing Puppet Master host.
Status:Draft

[Puppet](https://puppetlabs.com/) is an extremely useful, powerful and hyped tool for configuration management. [Foreman](http://www.theforeman.org/) provides a web frontend for Puppet (among other things) and is also capable of interfacing with virtualization tools to create new hosts. Both Puppet and Foreman are extremely useful in modern System Administration, but both of their documentation is kind of wide-spread and not as comprehensive as one might hope. That's why I'll do a writeup on how to install Foreman on top of an existing (and working) Puppet Master.

## Before

In the beginning, Puppet was running on a host called `puppet.shack` and was the Master to about 25 machines in the same network. It had been in use for about a week or two and mostly used to fix vulnerabilities, deploy ssh keys and reasonable configs for both shell and vim.

Since I would be using and extending Foreman for my bachelor thesis a few months later, I decided to set up Foreman to interface with the existing Puppet Master, so that I'd get used to Foreman's front end and way of doing things. (Of course, there were backups of `puppet.shack` standing by).

The system in question was a Debian running Puppet 3.7.4. The Foreman version to be installed was 1.7.


## Pre-Installation

The recommended way to install Foreman is to install the Foreman Installer (yeah.). You do so by calling

    echo "deb http://deb.theforeman.org/ wheezy 1.7" > /etc/apt/sources.list.d/foreman.list
    echo "deb http://deb.theforeman.org/ plugins 1.7" >> /etc/apt/sources.list.d/foreman.list
    wget -q http://deb.theforeman.org/pubkey.gpg -O- | apt-key add -
    apt-get update && apt-get install foreman-installer


## Installation

There are three ways to configure the Foreman Installer: pass command line arguments, edit a config file or run the Installer in interactive mode. While the config file is best for reproducing your results, I recommend choosing the interactive mode for your first try though, because it gives you a good overview over options and features. So, you either call the interactive mode with

    foreman-installer --no-puppet -i

OR you just trust the presets and call

    foreman-installer --no-puppet

After the installation is complete, the Installer will provide you with a login credentials for the admin account. If you're lucky and the Apache installation went right, you can now just browse to your server's URL and log in.


## Configuration

Now, you're far from finished, because you need to set up a lot of things in order to see all interesting and current Puppet data in your Foreman web interface.

### Puppet Reports

To recieve Puppet Reports in Foreman, first ensure that all Puppet clients have the line

    report = true

in their `puppet.conf`. Next up:

    wget https://raw.githubusercontent.com/theforeman/puppet-foreman/master/files/foreman-report_v2.rb
    mv foreman-report_v2.rb /usr/lib/ruby/vendor_ruby/puppet/reports/foreman.rb

Please check [here](http://theforeman.org/manuals/latest/index.html#3.5.4PuppetReports) that this link is correct and that the folder you move the file to contains the `tagmail.rb`. Create `/etc/puppet/foreman.yaml` by copying and adjusting the following:

    ---
    # Update for your Foreman and Puppet master hostname(s)
    :url: "https://foreman.example.com"
    :ssl_ca: "/var/lib/puppet/ssl/certs/ca.pem"
    :ssl_cert: "/var/lib/puppet/ssl/certs/puppet.example.com.pem"
    :ssl_key: "/var/lib/puppet/ssl/private_keys/puppet.example.com.pem"

    # Advanced settings
    :puppetdir: "/var/lib/puppet"
    :puppetuser: "puppet"
    :facts: true
    :timeout: 10
    :threads: null

Lastly, add the following to the `[main]` section of your Puppet Master `puppet.conf` and then restart your Puppet service:

    reports=log, foreman

Now you should see Reports under Monitor -> Reports as soon as your Puppet agents do anything. You can trigger this by calling 

    puppet agent --test

on a Puppet client.
