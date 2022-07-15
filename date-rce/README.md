Task that implements such vulnerabilities as Rce, Docker Breakout.
	1) The service gets the date by using the "date" shell command. Rce is achieved by substituting a POST request.
	2) The container in which the application is running with high privileges, in order to escape from it, it is enough to mount the necessary disk from the /dev partition to any convenient directory. This way you can interact with the root system by root user
