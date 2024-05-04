# Automate the task #0 with puppet

exec { 'all in one':
	command => 'sudo apt-get -y update;
	sudo apt-get -y install nginx;
	sudo sed -i "/server_name _/a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default;
	sudo service nginx restart',
	provider => shell,
}