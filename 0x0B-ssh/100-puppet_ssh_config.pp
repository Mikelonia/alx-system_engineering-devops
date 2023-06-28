#!/usr/bin/env bash
# using the puppet to make configurations to my file

file { 'ect/ssh/ssh_cofig':
	ensure => present,

content =>"

	#SSH client configuration
	host*
	IdentityFile ~/.ssh/school
	PasswordAuthentication no
	",
}
