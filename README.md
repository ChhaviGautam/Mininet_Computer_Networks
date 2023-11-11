Mininet Network Emulation and TCP Congestion Control Evaluation
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Authors:
Sahil Nayak - 20110119
Chhavi Gautam - 20110046
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Overview
This project demonstrates the implementation of custom network topologies using Mininet and evaluates TCP congestion control schemes' performance under various conditions. The experiments involve modifying network routes, capturing and analyzing packets with Wireshark, and running TCP client-server programs to measure throughput. The results provide insights into the impact of congestion control schemes on network performance.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Part 1: Custom Topology with Mininet
Implementation
Code: The Mininet topology is defined in the Python script pythonfilename.py.
Usage: Execute the script using sudo ./pythonfilename.py after making it executable with chmod +x pythonfilename.py.
Results: Screenshots of successful communication between hosts are available in the Result-Q1-a folder.
Observations
Wireshark: Screenshots and observations of packet capture on router r1 are available in the Result-Q1-b folder.

Latency Difference: Screenshots and latency measurements after varying default routing are available in the Result-Q1-c folder.

Routing Tables
Routing tables for routers r1, r2, and r3 for questions a and c are available in the Routing-Tables folder.
Part 2: TCP Client-Server Program and Throughput Analysis
Implementation
Code: The Mininet topology and TCP client-server program are implemented in the Python script file_name.py.
Usage: Run the script using sudo python file_name.py --config b --congestion cubic --loss 3.
Results: Plots and tables for throughput analysis are available in the Throughput-Analysis folder.
Observations
Single Client-Server Setup: Screenshots and observations of throughput over time for each congestion control scheme are available in the Single-Client-Server folder.

Multiple Clients to One Server: Screenshots and observations of throughput over time for each host and congestion control scheme are available in the Multiple-Clients-to-One-Server folder.

Link Loss Experiment: Screenshots and observations of throughput over time for each congestion control scheme with 1% and 3% link loss are available in the Link-Loss-Experiment folder.

How to Use
Clone the repository: git clone https://github.com/ChhaviGautam/Mininet_computer_networks.git
Navigate to the project directory: cd Mininet_computer_networks
Follow the instructions in each script's comments for specific configurations and usage.
References
Mininet GitHub Repository
Iperf - The TCP, UDP, and SCTP Network Bandwidth Measurement Tool
Feel free to explore the code and results in the provided GitHub repository for detailed insights into the implementation and experimental outcomes.
