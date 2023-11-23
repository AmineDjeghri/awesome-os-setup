# Conda, Pytorch & CUDA installation inside Linux/WSL

Installing CUDA inside a Conda environment instead of globally on your computer has several advantages:

1. Isolation: When you install CUDA within a Conda environment, it won't interfere with the CUDA installation at the global level or with other Conda environments.

2. Version Control: Different projects may require different versions of CUDA or GPU-related libraries. By creating separate Conda environments for different projects, you can easily switch between CUDA versions and ensure that each project uses the specific version it needs.

3. Clean Uninstall: If you later decide to remove a project and its associated dependencies, it's straightforward to delete the Conda environment, which ensures a clean uninstallation without leaving traces on your system.


## Summary 
1. [Install the Nvidia driver](#1-install-the-nvidia-driver)

2. [First and Recommended Option: Installing CUDA Inside a Conda Environment](#2-first-and-recommended-option-installing-cuda-inside-a-conda-environment)
    * [Automatic installation](#21-automatic-installation-)
    * [Manual installation ](#22-manual-installation)
2. [Second Option: Install CUDA Globally (Not Recommended)](#3-second-option-install-cuda-globally-not-recommended)


## 1. Install the Nvidia driver
- If you are on Linux and not WSL, download and install the nvidia driver .RUN file inside Linux:  [nvidia drivers](https://www.nvidia.fr/Download/index.aspx?lang=fr). Then run `nvidia-smi` on the terminal, it should print you all the information about your GPU
- If you use WSL, install the nvidia driver (.exe) on windows and not WSL from [nvidia drivers](https://www.nvidia.fr/Download/index.aspx?lang=fr). Run `nvidia-smi` on both windows & WSL Terminal, it should print you all the information about your GPU
  
## 2. First and Recommended Option: Installing CUDA Inside a Conda Environment

#### 2.1. Automatic installation : 

#### 2.2 Manual installation  
The next commands need to be run inside WSL or Linux and not Windows :
- Install build-essential `sudo apt-get install build-essential` (required by some packages like llama-cpp-python for example)

- Create a `conda-env-gpu.yaml` file with the content below (you can modify the name of the env and the packages). I usually have two yaml files :
One for GPU containing Pytorch with CUDA named `conda-env-gpu.yml` another one for CPU (not containing cuda) named `conda-env-cpu.yml`. I specify the version of pytorch in requirements.txt.
If pytorch was installed with cuda, running the requirements.txt won't install again pytorch since the same version is installed.
Running the conda-env-cpu.yaml that doesn't contain pytorch will install pytorch CPU from requirements.txt
Here is an example of project containing a conda-env-gpu.yaml and a conda-env-cpu.yaml [link](package_example)
The files you mentioned are used for setting up different environments for your Python project. Here's a brief summary of each:

- `requirements-cuda.txt`: This file contains the list of Python packages required for your project when it's running on a GPU. It includes PyTorch with CUDA support, and references the `requirements.txt` file for additional dependencies.

- `requirements-cpu.txt`: This file contains the list of Python packages required for your project when it's running on a CPU. It includes PyTorch without CUDA support, and references the `requirements.txt` file for additional dependencies.

- `requirements.txt`: This file contains the list of Python packages that are common to both the CPU and GPU environments. It's referenced by both `requirements-cuda.txt` and `requirements-cpu.txt`.

- `conda-env-gpu.yaml`: This file is used to create a Conda environment for running your project on a GPU. It specifies the Python version, some Conda packages, and references the `requirements-cuda.txt` file for additional Python packages.

- `conda-env-cpu.yaml`: This file is used to create a Conda environment for running your project on a CPU. It specifies the Python version, some Conda packages, and references the `requirements.txt` file for additional Python packages.

In summary, these files help you manage your project's dependencies and create isolated environments for running your project on different hardware configurations (CPU vs GPU).

Create an environment with CUDA support by executing the command:
``` bash
cd package_example;
conda env update -n my-env -f conda-env-gpu.yml; conda activate my-env;
```
The `-n my-env` option will supersede the environment name specified within the file. Alternatively, for CPU support only, use the command: `conda env update -n my-env -f conda-env-cpu.yml; conda activate my-env;`.

- Run `nvcc --version ; # should be cuda_11.8.r11.8`
- Verify the successful installation of PyTorch by executing the following Python code:

```py
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

## 3. Second Option: Install CUDA Globally (Not Recommended)

* Inside linux, run `nvidia-smi`, you should see a table showing information about your GPU. 
* If cuda is not installed and you run `nvcc --version`, you will get an error because cuda toolkit is not installed yet.   
* If you have cuda toolkit installed on windows (for WSL) or Linux, run `nvcc --version`, you should see the version of cuda which means that you already have cuda set up globally. if there are two different CUDA versions shown by nvcc and NVIDIA-smi, it is normal: [source](https://stackoverflow.com/a/53504578)

Now, we will install cuda on WSL, the following commands must all be run inside WSL. [If you want to understand more](https://docs.nvidia.com/cuda/wsl-user-guide/index.html#getting-started-with-cuda-on-wsl):
* Run `sudo apt-key del 7fa2af80`
* The CUDA driver installed on Windows host will be stubbed inside the WSL 2 as libcuda.so, therefore users must not install any NVIDIA GPU Linux driver within WSL 2
* You can only install a cuda toolkit that is compatible with WSL inside wsl : [link](https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=WSL-Ubuntu&target_version=2.0&target_type=deb_local) by following these instructions. 
Since we are installing cuda 11.7, follow the commands below.    

```
wget https://developer.download.nvidia.com/compute/cuda/11.7.0/local_installers/cuda_11.7.0_515.43.04_linux.run
sudo sh cuda_11.7.0_515.43.04_linux.run   
```
* Restart the terminal and run `nvcc --version` to test cuda installation inside wsl. If nvcc is not recognized, and you see something like `Command 'nvcc' not found, but can be installed with:
sudo apt install nvidia-cuda-toolkit`, it may be possible that the path is not inside .bashrc. First, verify that there is `/usr/local/cuda-11.7` inside WSL .Then, open `.bashrc` and add this at the end if it's not there:
```
export CUDA_HOME=/usr/local/cuda-11.7
export PATH=${CUDA_HOME}/bin:${PATH}
export LD_LIBRARY_PATH=${CUDA_HOME}/lib64:$LD_LIBRARY_PATH   
```   
* Restart the terminal and run again the command `nvcc --version`, you should see `Cuda compilation tools, release 11.7, V11.7.64`  
* You may also need to install cudnn from [here](https://developer.nvidia.com/rdp/cudnn-archive) version v8.9.1 (May 5th, 2023) for CUDA 11.x. You need to sign in, download the right version of cdnn for cuda 11.x. directly in wsl using windows explorer and then extract it with windows explorer then run it using `sudo dpkg -i cudnn-local-repo-ubuntu2204-8.9.1.23_1.0-1_amd64.deb` or  `sudo apt install ./cudnn-local-repo-ubuntu2204-8.9.1.23_1.0-1_amd64.deb`. if you install it twice you should see `cudnn-local-repo-ubuntu2204-8.9.1.23 is already the newest version (1.0-1).`

- test pytorch : 
   ```sh
   conda create -n test python=3.10;
   conda activate test;
   pip install torch;
   ```
  
   ```py
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
   
(Optional) Tutorials and sources :   
* [Download cuda 11.7](https://developer.nvidia.com/cuda-11-7-0-download-archive?target_os=Linux&target_arch=x86_64&Distribution=WSL-Ubuntu&target_version=2.0&target_type=deb_local)      
* [Cuda-wsl Nvidia guide](https://docs.nvidia.com/cuda/wsl-user-guide/index.html#getting-started-with-cuda-on-wsl-2](https://docs.nvidia.com/cuda/wsl-user-guide/index.html#getting-started-with-cuda-on-wsl-2))
* [Cuda-wsl Ubuntu guide](https://ubuntu.com/tutorials/enabling-gpu-acceleration-on-ubuntu-on-wsl2-with-the-nvidia-cuda-platform#3-install-nvidia-cuda-on-ubuntu)






