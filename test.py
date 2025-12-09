from pycuda.compiler import SourceModule

try:
    mod = SourceModule(open("helios_kernels.cu").read(), no_extern_c=True)
    print("Compiled OK")
except Exception as e:
    print("Compilation error:")
    print(e)
