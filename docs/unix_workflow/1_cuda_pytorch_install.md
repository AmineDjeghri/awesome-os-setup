# Cuda & Pytorch installation inside Linux/WSL using conda

Installing CUDA inside a Conda environment instead of globally on your computer has several advantages:

1. Isolation: When you install CUDA within a Conda environment, it won't interfere with the CUDA installation at the global level or with other Conda environments.

2. Version Control: Different projects may require different versions of CUDA or GPU-related libraries. By creating separate Conda environments for different projects, you can switch between CUDA versions and ensure that each project uses the specific version it needs.

3. Clean Uninstall: If you later decide to remove a project and its associated dependencies, it's straightforward to delete the Conda environment, which ensures a clean uninstallation without leaving traces on your system.

** table of content **


## 1. Install the Nvidia driver
- If you are on Linux and not WSL, download and install the nvidia driver .RUN file inside Linux: [nvidia drivers](https://www.nvidia.fr/Download/index.aspx?lang=fr). Then run `nvidia-smi` on the terminal, it should print you all the information about your GPU
- If you use WSL, install the nvidia driver (.exe) on windows and not WSL from [nvidia drivers](https://www.nvidia.fr/Download/index.aspx?lang=fr). Run `nvidia-smi` on both Windows & WSL Terminal, it should print you all the information about your GPU

Linux example:
```shell
        # Download the NVIDIA driver
        wget https://fr.download.nvidia.com/XFree86/Linux-x86_64/535.129.03/NVIDIA-Linux-x86_64-535.129.03.run
        # Make the downloaded file executable
        chmod +x NVIDIA-Linux-x86_64-535.129.03.run
        # Run the NVIDIA driver installer
        sudo ./NVIDIA-Linux-x86_64-535.129.03.run
        # Clean up the downloaded file (optional)
        rm NVIDIA-Linux-x86_64-535.129.03.run
        # Display GPU information
        nvidia-smi
```
## 2. Installing CUDA Inside a Conda Environment

#### 2.1. Automatic installation :
Create an environment with CUDA support by executing the command. The conda-env-gpu.yml file is used to create a Conda environment for running your project on a GPU. It specifies the Python version, some Conda packages, and references the requirements-cuda.txt file for additional Python packages.
``` bash
cd package_example/requirements;
conda env update -n my-env -f conda-env-gpu.yml; conda activate my-env;
```

#### 2.2 Manual installation
The next commands need to be run inside WSL or Linux and not Windows :
- Install build-essential `sudo apt-get install build-essential` (required by some packages like llama-cpp-python, for example)

- Create a `conda-env-gpu.yaml` file with the content below (you can modify the name of the env and the packages).
  - I usually have two yaml files:
One for GPU containing Pytorch with CUDA named `conda-env-gpu.yml` another one for CPU
  (not containing cuda) named `conda-env-cpu.yml`.
  - I specify the version of pytorch in requirements.txt.
  - If pytorch was installed with cuda,
  running the requirements.txt won't install again pytorch since the same version is installed.
  - Running the conda-env-cpu.yaml that doesn't contain pytorch will install pytorch CPU from requirements.txt

Here is an example of a project containing a conda-env-gpu.yaml and a conda-env-cpu.yaml [link](package_example)
The files you mentioned are used for setting up different environments for your Python project.
  Here's a brief summary of each:

- `requirements-cuda.txt`: This file contains the list of Python packages required for your project when it's running on a GPU. It includes PyTorch with CUDA support, and references the `requirements.txt` file for additional dependencies.

- `requirements-cpu.txt`: This file contains the list of Python packages required for your project when it's running on a CPU. It includes PyTorch without CUDA support, and references the `requirements.txt` file for additional dependencies.

- `requirements.txt`: This file contains the list of Python packages that are common to both the CPU and GPU environments. It's referenced by both `requirements-cuda.txt` and `requirements-cpu.txt`.

- `conda-env-gpu.yaml`: This file is used to create a Conda environment for running your project on a GPU. It specifies the Python version, some Conda packages, and references the `requirements-cuda.txt` file for additional Python packages.

- `conda-env-cpu.yaml`: This file is used to create a Conda environment for running your project on a CPU. It specifies the Python version, some Conda packages, and references the `requirements.txt` file for additional Python packages.

In summary, these files help you manage your project's dependencies and create isolated environments for running your project on different hardware configurations (CPU vs GPU).

Create an environment with CUDA support by executing the command:
``` bash
cd package_example/requirements;
conda env update -n my-env -f conda-env-gpu.yml; conda activate my-env;
```
The `-n my-env` option will supersede the environment name specified within the file. Alternatively, for CPU support only, use the command: `conda env update -n my-env -f conda-env-cpu.yml; conda activate my-env;`.

- Run `nvcc --version; # should be cuda_11.8.r11.8`
- Verify the successful installation of PyTorch by executing the following Python code:

```python
import torch
# setting device on GPU if available, else CPU
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print('Using device:', device)
print()

#Additional Info when using cuda
if device.type == 'cuda':
    print(torch.cuda.get_device_name(0))
    print('Memory Usage:')
    print('Allocated:', round(torch.cuda.memory_allocated(0)/1024**3,1), 'GB')
    print('Cached:   ', round(torch.cuda.memory_reserved(0)/1024**3,1), 'GB')
```

- When utilizing pre-commit hooks, ensure to exclude the file requirements-cuda.txt to prevent sorting the packages.
- Prioritize the installation of applications using pip; if pip is not applicable, resort to conda; and if conda is not an option, utilize apt-get. For instance, when installing Tesseract through conda, it is preferable to install it within the conda environment rather than globally using apt-get.
