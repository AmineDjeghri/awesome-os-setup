
## Conda, Python, Pytorch installation inside WSL: 

### Pytorch with Nvidia GPU (CUDA)
Installing CUDA inside a Conda environment instead of globally on your computer has several advantages:

1.Isolation: When you install CUDA within a Conda environment, it won't interfere with the CUDA installation at the global level or with other Conda environments.

2.Version Control: Different projects may require different versions of CUDA or GPU-related libraries. By creating separate Conda environments for different projects, you can easily switch between CUDA versions and ensure that each project uses the specific version it needs.

3.Clean Uninstall: If you later decide to remove a project and its associated dependencies, it's straightforward to delete the Conda environment, which ensures a clean uninstallation without leaving traces on your system.

### How to
- If you use WSL, install the nvidia driver on windows and not WSL. If you are on Linux and not WSL, install first the nvidia driver which is compatible with your card from the nvidia website. [nvidia drivers](https://www.nvidia.fr/Download/index.aspx?lang=fr). 
- Run `nvidia-smi` on the terminal, it should print you all the information about your GPU
  
- Install build-essential `sudo apt-get install build-essential` (required by some packages like llama-cpp-python for example)
  
- Create a `conda-env-gpu.yaml` file with the content below (you can modify the name of the env and the packages). I usually have two yaml files :
One for GPU containing Pytorch with CUDA named `conda-env-gpu.yml` another one for CPU (not containing cuda) named `conda-env-cpu.yml`. I specify the version of pytorch in requirements.txt.
If pytorch was installed with cuda, running the requirements.txt won't install again pytorch since the same version is installed.
Running the env.yaml that doesn't contain pytorch will install pytorch CPU from requirements.txt

*conda-env-gpu.yaml :* 
```
name: cuda-env
dependencies:
  - python=3.9
  - git
  - pip
  - conda-forge::ninja
  - nvidia/label/cuda-11.8.0::cuda
  - conda-forge::ffmpeg
  - conda-forge::gxx=11.4
  - pip:
      - -r requirements-cuda.txt
      - -e ."[dev]"

```

*requirements-cuda.txt :* 
```
# torch with CUDA support
--extra-index-url https://download.pytorch.org/whl/cu118
torch==2.0.1+cu118

# llama-cpp-python with CUDA support
--extra-index-url https://jllllll.github.io/llama-cpp-python-cuBLAS-wheels/AVX2/cu118
--prefer-binary
llama-cpp-python

# Spacy with cuda
spacy[cuda-autodetect]==3.6.1

# requirements
-r requirements.txt

# ExLlama
exllama@ https://github.com/jllllll/exllama/releases/download/0.0.17/exllama-0.0.17+cu118-cp39-cp39-linux_x86_64.whl

# ExLlamaV2
exllamav2==0.0.2
```
As you can see, there is tesseract in the conda installation. It's better to install it in our conda env rather than globbaly with apt-get. Always prefer to install libraries via pip -> conda -> apt-get
Create an environement with : `conda env update -n my-env -f conda-env-gpu.yml;conda activate my-env;`. the -n my-env will override the env's name inside the file.

- Run `    nvcc --version ; # should be cuda_11.8.r11.8`
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
- If you use pre-commit-hooks, exclude the file `requirements-cuda.txt` to not sort the packages.
