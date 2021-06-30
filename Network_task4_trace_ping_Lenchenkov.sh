#!/bin/bash
echo "------------"
echo "Homework task 4 (c) Lenchenkov Yuriy"
echo "------------"
echo ""
read -p "Enter destination host to check: " host
echo "Ping check..."
echo ""
ping -c 3 $host
sleep 3
echo ""
echo ""
ping_ttl=$(ping -c 1 $host | grep -oh 'ttl=[0-9]*' | grep -oh '[0-9]*')
echo ""
echo ""
echo "Please wait..."
echo "traceroute check without options..."
echo ""
echo ""
sudo traceroute $host
sleep 3
echo ""
echo ""
echo "Trying traceroute with TCP option and ping to identify host OS..."
sleep 3
echo ""
echo ""
trace_hops=$(sudo traceroute -T $host | sed '1d' | wc -l)
ttl=$((trace_hops + ping_ttl))
echo ""
echo ""
#echo "$trace_hops"
#echo "$ping_ttl"
echo "Total TTL is $ttl"

if [ $ttl -gt 60 ] && [ $ttl -lt 70 ]
then
  echo "Highly likely it\`s Linux on destination server"
elif [ $ttl -gt 120 ] && [ $ttl -lt 130 ]
then
  echo "Highly likely it\`s Windows on destination server"
elif [ $ttl -gt 250 ] && [ $ttl -lt 255 ]
then
  echo "Highly likely it\`s CISCO network device"
else
  echo "Cannot identify OS, possibly custom built or tuned"
fi

echo ""
echo ""
echo "Let\`s check OS with NMAP..."
sleep 3
echo "Please wait..."

if ! which nmap > /dev/null
then
  echo "You don\`t have NMAP package installed :("
elif ! sudo nmap -O -v $host | grep -q "Aggressive OS guesses:"
then
echo "Cannot detect OS with NMAP :("
else
sudo nmap -O -v $host | grep "Aggressive OS guesses:" | sed 's/Aggressive OS guesses: //'
fi
