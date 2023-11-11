Mininet Network Emulation and TCP Congestion Control Evaluation
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Authors:
Sahil Nayak - 20110119
Chhavi Gautam - 20110046
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Overview
This project demonstrates the implementation of custom network topologies using Mininet and evaluates TCP congestion control schemes' performance under various conditions. The experiments involve modifying network routes, capturing and analyzing packets with Wireshark, and running TCP client-server programs to measure throughput. The results provide insights into the impact of congestion control schemes on network performance.

_____________________________________________________________________________________________________________________________________________________________________________
Prerequisites
Before running the provided scripts, ensure that you have Mininet and OpenVSwitch installed on your Ubuntu system.

Mininet Installation
To install Mininet, follow these steps:

Open a terminal.

Run the following commands:

sudo apt-get update
sudo apt-get install mininet
This will install Mininet and its dependencies on your system.

Verify the installation by running:

sudo mn --version
You should see the Mininet version information.

OpenVSwitch Controller Setup
For the provided scripts to work, you also need to set up the OpenVSwitch controller. Here are the steps:

Install OpenVSwitch:

sudo apt-get install openvswitch-switch

Start the OpenVSwitch service:

sudo service openvswitch-switch start

Verify the installation:

sudo ovs-vsctl show

You should see information about the OpenVSwitch bridges.

Running the Scripts
Now that Mininet and OpenVSwitch are set up, you can proceed to run the provided scripts:
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Part 1: Custom Topology with Mininet
Implementation
Code: The Mininet topology is defined in the Python script Pythonscript_a.py & Pythonscript_c.py.
Usage: 
Execute the script using 
1. chmod +x pythonfilename.py (make the file executable)
2. sudo ./pythonfilename.py

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Part 2: TCP Client-Server Program and Throughput Analysis
Implementation
Code: The Mininet topology and TCP client-server program are implemented in the Pythonscript Pythonscript_2.py.
Usage: Run the script using 

sudo python file_name.py --config a/b/c/d --congestion cubic/bbr/reno/vegas --loss 3/1.


How to Use
Clone the repository: 

git clone https://github.com/ChhaviGautam/Mininet_computer_networks.git

Navigate to the project directory: 

cd Mininet_computer_networks

