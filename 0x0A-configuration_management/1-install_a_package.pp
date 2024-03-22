#!/usr/bin/pup
# Using Puppet, install flask from pip3.
package { 'flask':
    ensure  => 'installed',
    command => '/usr/bin/pip3 install flask==2.1.0 --break-system-packages'
  }
