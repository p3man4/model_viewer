# k3d_viewer

Django web interface to visualize k3d file

## Getting Started

These instructions will get you a copy of the project up and running on your linux machine for development.

### Prerequisites

What things you need to install the software and how to install them
1. Install Anaconda (optional)

Please check https://www.continuum.io/downloads

2. Install Django (version 1.11)

```
conda install -c anaconda django-1.11.3
```

### Installing
A step by step series of examples that tell you have to get a development env running

1. Copy this repository
```
git clone https://github.com/KohYoungResearchAmerica/k3d_viewer 
```
2. Change access permission of run.sh

```
chmod +x run.sh
```
3. Open k3d_viewer/viewer.py and change DATA_PATH and DP_ROOT (Detect_Part ROOT)

4. Run run.sh
```
./run.sh
```
5. Open http://127.0.0.1:8000/


