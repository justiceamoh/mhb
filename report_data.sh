#!/bin/bash

for i in `seq 1 984`; do
filename="$i.mhb"
	if [ ! -f data/$filename ]; then
		echo $filename >> unfound.txt
	fi	
done	

