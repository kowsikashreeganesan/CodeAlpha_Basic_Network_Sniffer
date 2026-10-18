Basic Network Sniffer

Project Overview
          
The Basic Network Sniffer is a Python-based cybersecurity project developed as part of the CodeAlpha internship. It captures and displays network packets using the Scapy library.

Objective

To develop a basic network sniffer that captures network packets and displays information about them.

Technologies Used

- Python 3.14.7
- Scapy 2.8.0
- Npcap
- Visual Studio Code
- Windows 11

Features

- Captures up to 10 network packets.
- Displays packet summaries.
- Shows source and destination IP addresses   when available.
- Identifies TCP, UDP, and ICMP packets.
- Displays a completion message after  packet capture.

Requirements

- Python installed on your computer.
- Scapy library.
- Npcap installed on Windows.

Installation

Install Scapy using the following command:py -m pip install scapy
Install Npcap from the official website if it is not already installed:https://npcap.com/

How to Run

1. Open the project folder in Visual Studio Code.
2. Open the terminal in the project folder.
3. Run the program using:py network_sniffer.py
4. Allow the program to capture packets on your own device or an authorized network interface.
5. View the captured packet details in the terminal.

(Note: The Python filename in the command must match your actual source-code filename).

Sample Result

The program displays packet information in the terminal and finishes after capturing 10 packets.

Ethical Considerations

Use this tool only on your own device or networks for which you have permission. Do not capture, store, or share other people's network traffic without authorization.

Author

Kowsikashree G

Internship

CodeAlpha — Basic Network Sniffer Project
