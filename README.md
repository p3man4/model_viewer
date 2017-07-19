# k3d_viewer

Django web interface to visualize k3d file

## Getting Started

These instructions will get ypu a copy of the project up and running on yourlinux machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them
1. Install Anaconda (optional)
Please check https://www.continuum.io/downloads

2. Install Django (version 1.11)

'''
conda install -c anaconda django-1.11.3

'''

### Installing
A step by step series of examples that tell you have to get a development env running

1. copy this repository
'''
git clone https://github.com/KohYoungResearchAmerica/k3d_viewer 
'''
2. change access permission of run.sh

'''
chmod 777 run.sh
'''
3. open k3d_viewer/viewer.py and change DATA_PATH and DP_ROOT (Detect_Part ROOT)
4. run run.sh
'''
./run.sh
'''



