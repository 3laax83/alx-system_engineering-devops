# Automate the task #0 with puppet

exec { 'update-apt':
  command   => 'apt-get -y update',
  user      => 'root',
  provider  => 'bash',
  }
->
package { 'nginx':
  ensure    => present,
  provider  => 'apt',
}
->
file_line { 'Add-HTTP-HEADER':
  ensure    => 'present',
  path      => '/etc/nginx/sites-available/default',
  after     => 'listen 80 default_server',
  line      => 'add_header X-Served-By $hostname',
  }
->
service { 'nginx':
  ensure    => 'running',
  enable    => true,
  require   => Package['nginx'],
}
