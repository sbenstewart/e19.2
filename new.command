#!/bin/bash
open -a "Microsoft PowerPoint" $1
number=$(ps aux | pgrep "Microsoft PowerPoint" | wc -l)
while [ 1 ]
do
if [ $number -gt 0 ]
    then
	number=$(ps aux | pgrep "Microsoft PowerPoint" | wc -l)
else
	break;
fi
done
pgrep python | xargs kill
