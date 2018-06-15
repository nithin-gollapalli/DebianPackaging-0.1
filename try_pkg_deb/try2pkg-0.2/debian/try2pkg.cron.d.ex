#
# Regular cron jobs for the try2pkg package
#
0 4	* * *	root	[ -x /usr/bin/try2pkg_maintenance ] && /usr/bin/try2pkg_maintenance
