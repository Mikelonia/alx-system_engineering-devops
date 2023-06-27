# Install Flask version 2.1.0 using pip3

# Ensuring the package resource is installed and up-to-date
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
} 

