# cd.model_viewer

Django web interface to visualize cd.model structure

![screen shot](./k3d_viewer_example1.png?raw=true "k3d_viewer screen shot")


## Getting Started

These instructions will get you a copy of the project up and running on your linux machine for development.

### Prerequisites

What things you need to install the software and how to install them
1. Install Anaconda (optional)

Please check https://www.continuum.io/downloads

2. Install Django (version 1.11) with conda

```
conda install -c anaconda django-1.11.3
```

3. Copy KYRA's SMT repository
```
git clone https://github.com/KohYoungResearchAmerica/SMT.git
```

4. Set PYTHONPATH to detect_part subdirectory
```
export PYTHONPATH "<your_SMT_ROOT>/detect_part"
```

### Installing
A step by step series of examples that tell you have to get a development env running

1. Copy this repository
```
git clone https://github.com/KohYoungResearchAmerica/model_viewer 
```
2. Change access permission of run.sh

```
chmod +x run.sh
```
3. Open model_viewer/viewer.py and change DP_ROOT (Detect_Part ROOT)

4. Run run.sh
```
./run.sh
```
5. Open http://127.0.0.1:8000/main/


