
#!/bin/bash


cd cruiser
echo "************************************************************************************************************************************************************************"
echo "Opening maps"
sleep 2
echo ""
echo ""
echo "Setting things up for route optimization"
sleep 1
echo ""
echo ""
sudo ./cruiser.sh
echo "Done mapping."
echo ""
echo ""
echo "Alternate routes set up"
echo "************************************************************************************************************************************************************************"

cd ..
sudo scp vasu.gpx pi@10.42.0.53:
echo ""
echo ""
echo "Files loaded to device"
echo ""
echo ""





