package { 'nginx':
  ensure   => installed,
  provider => 'apt',
}

file_line { 'install':
  ensure  => 'present',
  path	  => 'etc/nginx/sites-enabled/default',
  after	  => 'listen 80 default_server;',
  line 	  => 'rewrite ^/rerdirect_me https://www.github.com/mikelonia permanent;',
}
file { '/var/www/html/index.html':
  content => 'Hello world!',
}
service { 'nginx':
 ensure  => running,
 require => package ['nginx'],
}
