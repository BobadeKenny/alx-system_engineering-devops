#  testing how well our web server setup featuring Nginx is doing under pressure
exec {'Test limit':
  command => 'sed -i "s/15/4098/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}
-> exec {'Restart nginx':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
