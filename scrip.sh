#!/bin/bash

cd ..
echo "Resolving Tracks and Waypoints"
echo ".."
echo ".."
echo ""
echo "Loading Mapnik Maps of Bengaluru"
echo ""
echo "Integrating GPS data for tracking" 
echo ""

sleep 2
viking vasu.gpx
sleep 2
cd  Desktop
echo  "Enter type of rendering"
read varname
if [ $varname -eq  1 ]
then
	viking b1.vik
else
	viking blore_2.vik
fi
sleep 2



