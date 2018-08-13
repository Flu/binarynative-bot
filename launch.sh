echo "Started script source.py with python3.5 at `date`"
while ! python3.5 src/source.py
do
    sleep 5
    echo "Restarting...\n"
done
