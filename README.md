**Mininet Network Emulation and TCP Congestion Control Evaluation**
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Authors:
**Sahil Nayak - 20110119
Chhavi Gautam - 20110046**
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
**Overview**
This project demonstrates the implementation of custom network topologies using Mininet and evaluates TCP congestion control schemes' performance under various conditions. The experiments involve modifying network routes, capturing and analyzing packets with Wireshark, and running TCP client-server programs to measure throughput. The results provide insights into the impact of congestion control schemes on network performance.

_____________________________________________________________________________________________________________________________________________________________________________
**Prerequisites**
Before running the provided scripts, ensure that you have Mininet and OpenVSwitch installed on your Ubuntu system.

**Mininet Installation**
To install Mininet, follow these steps:

**Run the following commands after opening the terminal:**

<pre><code>
sudo apt-get update
sudo apt-get install mininet
This will install Mininet and its dependencies on your system.
</code></pre>

**Verify the installation by running:**
<pre><code>
sudo mn --version
You should see the Mininet version information.
</code></pre>
OpenVSwitch Controller Setup
For the provided scripts to work, you also need to set up the OpenVSwitch controller. Here are the steps:

**Install OpenVSwitch:**
<pre><code>
sudo apt-get install openvswitch-switch
</code></pre>
Start the OpenVSwitch service:
<pre><code>
sudo service openvswitch-switch start
</code></pre>
Verify the installation:
<pre><code>
sudo ovs-vsctl show
</code></pre>
You should see information about the OpenVSwitch bridges.

**Running the Scripts**
Now that Mininet and OpenVSwitch are set up, you can proceed to run the provided scripts:
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
**Part 1: Custom Topology with Mininet
Implementation**
Code: The Mininet topology is defined in the Python script Pythonscript_a.py & Pythonscript_c.py.
Usage: 
Execute the following script:
<pre><code>
1. open the terminal in the directory where the file is saved
2. chmod +x pythonfilename.py (make the file executable)
3. sudo ./pythonfilename.py
</code></pre>

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
**Part 2: TCP Client-Server Program and Throughput Analysis
Implementation**
Code: The Mininet topology and TCP client-server program are implemented in the Pythonscript Pythonscript_2.py.
Usage: Run the script using 
<pre><code>
sudo python file_name.py --config a/b/c/d --congestion cubic/bbr/reno/vegas --loss 3/1.
</code></pre>

**How to Use
Clone the repository: **
<pre><code>
git clone https://github.com/ChhaviGautam/Mininet_computer_networks.git
</code></pre>
**Navigate to the project directory: **
<pre><code>
cd Mininet_computer_networks
</code></pre>
