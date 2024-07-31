$Env:PWD="c:\AMD\RyzenAI-SW\example\transformers"

$Env:THIRD_PARTY=$Env:PWD+"\third_party"
$Env:TVM_LIBRARY_PATH=$Env:THIRD_PARTY+"\lib;"+$Env:THIRD_PARTY+"\bin"
$Env:PATH +=";"+$Env:TVM_LIBRARY_PATH+";"+$Env:PWD+"\ops\cpp\;"+$Env:THIRD_PARTY
$Env:PYTORCH_AIE_PATH=$Env:PWD
$Env:PYTHONPATH=";"+$Env:TVM_LIBRARY_PATH+";"+$Env:THIRD_PARTY
$Env:PYTHONPATH+=";"+$Env:PWD+"\ops\python"
$Env:PYTHONPATH+=";"+$Env:PWD+"\onnx-ops\python"
$Env:PYTHONPATH+=";"+$Env:PWD+"\tools"
$Env:PYTHONPATH+=";"+$Env:PWD+"\ext\smoothquant\smoothquant"
$Env:PYTHONPATH+=";"+$Env:PWD+"\ext\smoothquant"
$Env:PYTHONPATH+=";"+$Env:PWD+"\ext\llm-awq"
$Env:PYTHONPATH+=";"+$Env:PWD+"\ext\llm-awq\awq\quantize"
$Env:PYTHONPATH+=";"+$Env:PWD+"\ext\llm-awq\awq\utils"
$Env:PYTHONPATH+=";"+$Env:PWD+"\ext\llm-awq\awq\kernels"
$Env:AWQ_CACHE=$Env:PWD+"\ext\awq_cache\"

$Env:XRT_PATH=$Env:THIRD_PARTY+"\xrt-ipu"

$Env:TARGET_DESIGN=
$Env:DEVICE="phx"
$Env:XLNX_VART_FIRMWARE=$Env:PWD+"\xclbin\phx"
