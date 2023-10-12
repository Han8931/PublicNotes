#!/bin/sh
DATE=$(date)
cat << EOF # <<EOF is the heare document
Date: $DATE

The output above is from the Unix date command.
It's not a very interesting command.
EOF
