
# Scheduling Simulation

  

This repository has some scheduling algorithms implemented with the py-batsim library (Python), intended for simulation once connected to the Batsim simulator.

  

# How to run tests?

  

## 01. 🖥️ Check your environment

  

First, make sure if your environment contains the following:
  

| Name | My version | Link | Obs |
| --- | --- | --- | --- |
| Batsim | 4.0.0 | [docs](https://batsim.readthedocs.io/en/latest/tuto-first-simulation/tuto.html), [gitlab](https://gitlab.inria.fr/batsim/batsim) | Make sure that your Batsim is installed and running. You can test it by running some example from their docs. If that's not your case, follow their installation instructions. |
| Python | 3.8.10 | [website](https://www.python.org/) | |
| Pybatsim | 3.2.0 | [gitlab](https://gitlab.inria.fr/batsim/pybatsim) | Using pip: pip install pybatsim |

  

## 02. 📰 Simulation inputs

  

To run Batsim, we need to provide the paths for two files:

  

1. **Platform**: A XML description about the hardware resources used in the simulation (host, clusters, network...). The definition of the platform follows the [SimGrid platform style](https://simgrid.org/doc/latest/Platform.html).

2. **Workload**: A JSON definition about the jobs to be submitted and scheduled, their characteristics and how Batsim should execute them. You can find how to define a workload in the [Batsim docs](https://batsim.readthedocs.io/en/latest/input-workload.html).

  

In this repository we have some platforms and workloads examples. Feel free to use or edit them.

  

## 03. 📅 Choosing a scheduling algorithm

  

We're developing some scheduling algorithms *(in "/algorithms"),* choose one to run your test. Each algorithm have already some tests results.

  

## 04. 🧪 Running your test

  

To finally run your test, first run Batsim with the platform and workload defined.

  

```bash

batsim -p "./path/to/platform.xml" -w "./path/to/workload.json" -e "./path/to/save/results/result_prefix"

```

  

Using a example from our repository:

  

```bash

batsim -p "./platforms/platform01.xml" -w "./workloads/workload01.json" -e "./results/test01"

```

  

With Batsim ready, run your scheduling algorithm:

  

```bash

pybatsim "./path/to/algorithm.py"

```

  

Using a example from our repository:

  

```bash

pybatsim "./algorithms/LPT/LPT.py"

```
