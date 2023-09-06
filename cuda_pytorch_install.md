
## 3.3 Python, Pytorch and Cuda installation: 
### WSL : 
#### 3.3.1 Pytorch with Nvidia GPU
create a `env.yaml` file with the content above (you can modify the name of the env and the packages). I usually have to yaml file :
One containing Pytorch with CUDA and another one not containing pytorch (for CPU). I specify the version of pytorch in requirements.txt.
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
Create an environement with : `conda env create -f conda-env-gpu.yml;conda activate my-env;`.

#### 3.3.2 Pytorch without gpu: 
`pip install torch torchvision torchaudio`

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
- (not updated) there is a requirements.txt that contains the principal data science libraries (without pytorch as you have installed it from the previous line, just do `pip install -r https://raw.githubusercontent.com/AmineDjeghri/BetterWindowsUX/master/requirements.txt`
