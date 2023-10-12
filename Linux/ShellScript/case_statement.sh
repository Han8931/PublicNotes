#!/bin/bash 

case ${1,,} in 
	herbert | administrator)
		echo "Hello, you are the boss here"
		;;
	help)
		echo "Just enter your name"
		;;
	*)
		echo "Hello there, you are not the boss of me."
esac
