#!/usr/bin/env bash
# using the puppet to make configurations to my file

file { 'etc/ssh/ssh_config':
	ensure => present,

content =>"

	#SSH client configuration
	host*
	IdentityFile ~/.ssh/school
	PasswordAuthentication no
	",
}
