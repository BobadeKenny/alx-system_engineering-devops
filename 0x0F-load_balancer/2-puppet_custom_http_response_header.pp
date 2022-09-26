# Setup nginx server

package { 'nginx':
  ensure     => 'installed',
}

file { '/etc/nginx/nginx.conf':
  content => "add_header X-Served-By ${HOSTNAME};",
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
