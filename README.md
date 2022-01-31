# whiterootz
This is the root folder of all things related to White Rootz

## Setup

### Setup static ip address
```
# Get the gateway of the router
sudo route -n

# Open the dhcpcd.conf file
sudo nano /etc/dhcpcd.conf

# Inside the dhcpcd.conf file, type the below command:
interface wlan0
static ip_address=192.168.0.119 # Set it to your static ID 
static routers=192.168.1 # Set it to the gateway of the router
static domain_name_servers=8.8.8.8 8.8.4.4 # Google dns server or any other dns of your choice

# After saving the file reboot the system
sudo reboot
```

This will successfully update the ip address and set it to a static ip address
