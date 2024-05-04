# Automate the task #0 with puppet

exec { 'update-apt':
  command   => 'sudo apt-get update',
  provider  => shell,
  }

package { 'nginx':
  ensure    => present,
}

file_line { 'Add-HTTP-HEADER':
  ensure    => 'present',
  path      => '/etc/nginx/sites-available/default',
  after     => 'listen 80 default_server',
  line      => 'add_header X-Served-By ${hostname}',
  }

exec { 'nginx-service':
  command	=> 'sudo service nginx restart',
  provider => shell,
 }
