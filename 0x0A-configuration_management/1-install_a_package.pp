#!/usr/bin/pup
# Using Puppet, install flask from pip3.
package {
    'flask':
    command => '/usr/bin/pip3 install -q flask==2.1.0 --break-system-packages'
  }
