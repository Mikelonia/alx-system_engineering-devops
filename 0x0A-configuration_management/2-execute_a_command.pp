# Using a Puppet, create a manifest that kill a process named killmenow.

exec { 'conditions':
command => '/usr/bin/pkill killmenow',
}
