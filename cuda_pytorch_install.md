
## Conda, Python, Pytorch installation inside WSL: 

### Pytorch with Nvidia GPU (CUDA)
Installing CUDA inside a Conda environment instead of globally on your computer has several advantages:

1.Isolation: When you install CUDA within a Conda environment, it won't interfere with the CUDA installation at the global level or with other Conda environments.

2.Version Control: Different projects may require different versions of CUDA or GPU-related libraries. By creating separate Conda environments for different projects, you can easily switch between CUDA versions and ensure that each project uses the specific version it needs.

3.Clean Uninstall: If you later decide to remove a project and its associated dependencies, it's straightforward to delete the Conda environment, which ensures a clean uninstallation without leaving traces on your system.

- If you use WSL, install the nvidia driver on windows and not WSL. If you are on Linux and not WSL, install first the nvidia driver which is compatible with your card from the nvidia website. [nvidia drivers](https://www.nvidia.fr/Download/index.aspx?lang=fr)
  
- Install build-essential `sudo apt-get install build-essential` (required by some packages like llama-cpp-python for example)
  
- Create a `env.yaml` file with the content above (you can modify the name of the env and the packages). I usually have to yaml file :
One for GPU containing Pytorch with CUDA and another one for CPU (not containing cuda). I specify the version of pytorch in requirements.txt.
If pytorch was installed with cuda, running the requirements.txt won't install again pytorch since the same version is installed.
Running the env.yaml that doesn't contain pytorch will install pytorch CPU from requirements.txt
```
name: py-env
dependencies:
  - python=3.9
  - git
  - pip
  - conda-forge::ninja
  - nvidia/label/cuda-11.8.0::cuda
  - conda-forge::ffmpeg
  - conda-forge::gxx=11.4
  - conda-forge::tesseract=5.3.2
  - pip:
      - --extra-index-url https://download.pytorch.org/whl/cu118
      - torch==2.0.1+cu118
      - --extra-index-url https://download.pytorch.org/whl/cu118
      - torchvision
      - --extra-index-url https://download.pytorch.org/whl/cu118
      - torchaudio
      - -r requirements.txt
```
Create an environement with : `conda env update -n nmy-env -f conda-env-gpu.yml;conda activate my-env;`.
- Check if you succeeded to install pytorch, run the following python code: 

```
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

#### 3.3 Python packages:
- Always use `pip` command to install python packages.
- (not updated) there is a requirements.txt that contains the principal data science libraries, `https://raw.githubusercontent.com/AmineDjeghri/BetterWindowsUX/master/requirements.txt`
