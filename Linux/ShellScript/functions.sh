#!/bin/bash 

# showuptime(){
# 	up=$(uptime -p | cut -c4-)
# 	since=$(uptime -s)
# 	cat << EOF
# -----
# This machine has been up for ${up}
# It has been running since ${since}
# -----
# EOF
# }
# showuptime

# up="before"
# since="function"
# echo $up
# echo $since

# showuptime(){
# 	# Define local variables
# 	local up=$(uptime -p | cut -c4-)
# 	local since=$(uptime -s)
# 	cat << EOF
# -----
# This machine has been up for ${up}
# It has been running since ${since}
# -----
# EOF
# }
# showuptime
# echo $up
# echo $since
#

# showname(){
# 	echo hello $1
# }
# showname herbert
# showname name

 showname(){
 	echo hello $1
	if [ ${1,,} = herbert ];then
		return 0
	else
		return 1
	fi
 }
 showname $1
