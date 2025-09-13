# Mal-Track
Malware removal tool writen in Python.

This project writed only for learning purposes

USE ONLY ON VIRTUAL MACHINE!

## Overview

This program designed to find and remove malware from a Windows computer. It is intended for use in a virtual machine set up for malware testing. The program finds the malware, stops it from running, removes it from Windows startup, deletes the malware files, and shows the IP address of the attacker.
Managing Startup Programs

The Windows Registry stores information about system and application settings. Programs that automatically start when Windows boots are listed in specific registry locations. There are different locations for Current User and Local Machine.

We can add/remove entries by adding/removing values containing programs name and file path.
Retrieving the Attacker IP

The program reads the contents of the malware file and searches for sequences similar to ip addresses in the file using regex patterns.
How the Program Works

Program starts by finding running processes that match the malware name. Searches for the malware process filepath and reads the file contents to search for an IP address. After that the program stops the malware process, removes the entry from the Windows startup registry and removes any malware files from the system.



## Requirements

psutil Library:

``pip install psutil``

## SHOWCASE

[check video showcase](https://youtu.be/rFd2SdXtMHs)

## Usage

    Launch a Virtual Machine with an official Windows image.
    Download the malware
    Extract the contents of the zip file and move the malware directory to Desktop.
    Run the mal-track.exe file.
    Run the mal_track.py file.
