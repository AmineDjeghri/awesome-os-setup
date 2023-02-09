
## 4-Python, Pytorch and Cuda installation: 
#### 4.1.1 Pytorch with Nvidia GPU
- Important : Pytorch 1.10.1 works with CUDA 11.3 and visual studio 2019
- Download [VSCode Community 2019](https://docs.microsoft.com/en-us/visualstudio/releases/2019/release-notes).
- Install it and check `Desktop Development with C++` and `.NET` (size will be 11GB approxiamtly) 
- Download and install [CUDA 11.3](https://developer.nvidia.com/cuda-11.3.0-download-archive?target_os=Windows&target_arch=x86_64&target_version=10&target_type=exe_local)
- Install [Pytorch 1.10.1](https://pytorch.org/get-started/locally/) by running this command `pip install torch==1.10.1+cu113 torchvision==0.11.2+cu113 torchaudio===0.10.1+cu113 -f https://download.pytorch.org/whl/cu113/torch_stable.html`

#### 4.1.2 Pytorch without gpu: 
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

#### 4.2 Python packages:
- Always use `pip` command in Windows Terminal to install python packages 
- there is a requirements.txt that contains the principal data science libraries (without pytorch as you have installed it from the previous line, just do `pip install -r https://raw.githubusercontent.com/AmineDjeghri/BetterWindowsUX/master/requirements.txt`
