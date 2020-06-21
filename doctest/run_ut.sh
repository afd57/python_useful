python3 -m doctest -v fib.py

if [ $? -ne 0 ]
then
   echo "Test Failed"
   exit 1
fi