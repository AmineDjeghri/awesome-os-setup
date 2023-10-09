
# (1st and easiest option) Conda, Pytorch & CUDA installation inside WSL: 

### Pytorch with Nvidia GPU (CUDA)
Installing CUDA inside a Conda environment instead of globally on your computer has several advantages:

1.Isolation: When you install CUDA within a Conda environment, it won't interfere with the CUDA installation at the global level or with other Conda environments.

2.Version Control: Different projects may require different versions of CUDA or GPU-related libraries. By creating separate Conda environments for different projects, you can easily switch between CUDA versions and ensure that each project uses the specific version it needs.

3.Clean Uninstall: If you later decide to remove a project and its associated dependencies, it's straightforward to delete the Conda environment, which ensures a clean uninstallation without leaving traces on your system.

### How to
- If you use WSL, install the nvidia driver (.exe) on windows and not WSL from [nvidia drivers](https://www.nvidia.fr/Download/index.aspx?lang=fr). Run `nvidia-smi` on both windows & WSL Terminal, it should print you all the information about your GPU
- If you are on Linux and not WSL, install the nvidia driver (.RUN) inside Linux  from the nvidia website. [nvidia drivers](https://www.nvidia.fr/Download/index.aspx?lang=fr).Run `nvidia-smi` on the terminal, it should print you all the information about your GPU

The next commands need to be ran inside WSL or Linux and not Windows :
- Install build-essential `sudo apt-get install build-essential` (required by some packages like llama-cpp-python for example)
  
- Create a `conda-env-gpu.yaml` file with the content below (you can modify the name of the env and the packages). I usually have two yaml files :
One for GPU containing Pytorch with CUDA named `conda-env-gpu.yml` another one for CPU (not containing cuda) named `conda-env-cpu.yml`. I specify the version of pytorch in requirements.txt.
If pytorch was installed with cuda, running the requirements.txt won't install again pytorch since the same version is installed.
Running the conda-env-cpu.yaml that doesn't contain pytorch will install pytorch CPU from requirements.txt

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
      # - -e ."[dev]"

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


*requirements.txt*
```
langchain
llama-cpp-python==0.2.6 # CPU Only
nltk==3.8.1
pdfminer.six==20221105
sentence-transformers==2.2.2
sentencepiece==0.1.99
spacy==3.6.1
spacy-transformers==1.2.5
torch==2.0.1
transformers==4.30.*
```

*conda-env-cpu.yaml :"
```
name: env-cpu
dependencies:
  - python=3.9
  - git
  - pip
  - conda-forge::ninja
  - conda-forge::ffmpeg
  - conda-forge::gxx=11.4
  - pip:
      - --extra-index-url https://download.pytorch.org/whl/cpu
      - torch==2.0.1
      - -r requirements.txt
```

Always install apps using pip, if it's not possible use conda, if it's not possible use apt install (pip -> conda -> apt-get). for example tesseract in the conda installation. It's better to install it in our conda env rather than globbaly with apt-get
Create an environement with cuda support using : `conda env update -n my-env -f conda-env-gpu.yml;conda activate my-env;`. the -n my-env will override the env's name inside the file. Or CPU support only `conda env update -n my-env -f conda-env-cpu.yml;conda activate my-env;`

- Run `nvcc --version ; # should be cuda_11.8.r11.8`
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



# (2nd choice, install cuda globally)
* We will install cuda 11.7 for pytorch 2.0.1  (June 2023)    
* Install Nvidia [driver](https://www.nvidia.com/download/index.aspx) on windows
* On windows, run `nvidia-smi`. If you have cuda toolkit installed on windows (not obligatory), run `nvcc --version`. You will see two different CUDA versions shown by nvcc and NVIDIA-smi which is normal if you have cuda toolkit on windows [source](https://stackoverflow.com/a/53504578)

* On linux, run `nvidia-smi`, you will see the same thing as on windows. If you run `nvcc --version`, you will get an error because cuda toolkit is not installed yet on WSL.   

Now, we will install cuda on WSL, the following commands must all be runned inside WSL. [If you want to understand more](https://docs.nvidia.com/cuda/wsl-user-guide/index.html#getting-started-with-cuda-on-wsl):
* Run `sudo apt-key del 7fa2af80`
* The CUDA driver installed on Windows host will be stubbed inside the WSL 2 as libcuda.so, therefore users must not install any NVIDIA GPU Linux driver within WSL 2
* You can only install a cuda toolkit that is compatible with WSL inside wsl : [link](https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=WSL-Ubuntu&target_version=2.0&target_type=deb_local) ny following these instructions. 
Since we we are installing cuda 11.7, follow the commands bellow.    
```
wget https://developer.download.nvidia.com/compute/cuda/repos/wsl-ubuntu/x86_64/cuda-wsl-ubuntu.pin
sudo mv cuda-wsl-ubuntu.pin /etc/apt/preferences.d/cuda-repository-pin-600
wget https://developer.download.nvidia.com/compute/cuda/11.7.0/local_installers/cuda-repo-wsl-ubuntu-11-7-local_11.7.0-1_amd64.deb
sudo dpkg -i cuda-repo-wsl-ubuntu-11-7-local_11.7.0-1_amd64.deb
sudo cp /var/cuda-repo-wsl-ubuntu-11-7-local/cuda-*-keyring.gpg /usr/share/keyrings/
sudo apt-get update
sudo apt-get -y install cuda
```
or
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
   `conda create -n test python=3.10`
   `conda activate test`
   `pip install torch`
   `python`
   ```py
   >>> import torch
   >>> torch.cuda.is_available()
   True
   ```
   
(Optional) Tutorials and sources :   
* [Download cuda 11.7](https://developer.nvidia.com/cuda-11-7-0-download-archive?target_os=Linux&target_arch=x86_64&Distribution=WSL-Ubuntu&target_version=2.0&target_type=deb_local)      
* [Cuda-wsl Nvidia guide](https://docs.nvidia.com/cuda/wsl-user-guide/index.html#getting-started-with-cuda-on-wsl-2](https://docs.nvidia.com/cuda/wsl-user-guide/index.html#getting-started-with-cuda-on-wsl-2))
* [Cuda-wsl Ubuntu guide](https://ubuntu.com/tutorials/enabling-gpu-acceleration-on-ubuntu-on-wsl2-with-the-nvidia-cuda-platform#3-install-nvidia-cuda-on-ubuntu)






