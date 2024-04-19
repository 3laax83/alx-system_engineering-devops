# Configuration file for clients

include stdlib

File_line { 'Turn off passwd auth':
    ensure    => present,
    path      => '/etc/ssh/ssh_config'
    line      => '    PasswordAuthentication no',
    replace   => true,
  }

File_line { 'Declare identity file':
    ensure    => present,
    path      => '/etc/ssh/sshd_config'
    line      => '    IdentifyFile ~/.ssh/school'
    replace   => true,
  }
