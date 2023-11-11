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
_____________________________________________________________________________________________________________________________________________________________________________
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

_____________________________________________________________________________________________________________________________________________________________________________
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

________________________________________________________________________________________________________________________________________________________________________________________________________________
**Throughput Analysis**
Throughput, measured in bits per second (bps), represents the amount of data transferable over a network within a specified time frame. Various tools, such as Wireshark and iPerf, can be employed to measure throughput.

**Observations**
Several key observations can be drawn from the experiments:

1. Congestion Control Scheme Impact:
BBR outperforms the other congestion control schemes, consistently delivering higher throughput. Reno exhibits the lowest throughput.

2. Link Loss Influence:
Introducing link loss notably reduces throughput, with the impact more pronounced at higher link loss rates.

3. Multiple Client Effects:
With multiple clients, throughput diminishes compared to a single-client scenario. This is attributed to increased network congestion.

**Conclusion**
The congestion control scheme and the presence of link loss significantly influence network throughput. BBR emerges as the most efficient congestion control scheme, while Reno demonstrates the lowest throughput. Link loss, even at low rates, can substantially degrade network performance.

**Enhancements
Potential enhancements include:**

1. Evaluation of Additional Congestion Control Schemes:
Investigating the performance of other congestion control schemes could provide further insights into their effectiveness.

2. Analysis of Different Network Topologies:
Exploring the impact of congestion control schemes and link loss on various network topologies would broaden the scope of understanding.

3. Implementation of Traffic Shaping:
Incorporating traffic shaping techniques could further optimize network performance and resource utilization.

References

[Mininet GitHub Repository](https://github.com/mininet/mininet)

[Iperf - The TCP, UDP, and SCTP Network Bandwidth Measurement Tool](https://iperf.fr/)

Feel free to explore the code and results in the provided GitHub repository for detailed insights into the implementation and experimental outcomes.
