"""Check that the study environment is ready.

Run with:  uv run phase-0-setup/check_env.py
"""

import importlib
import platform
import sys

REQUIRED = ["numpy", "matplotlib", "jupyterlab"]
OPTIONAL = ["torch"]


def version_of(name: str) -> str | None:
    try:
        module = importlib.import_module(name)
    except ImportError:
        return None
    return getattr(module, "__version__", "installed")


def main() -> int:
    print(f"Python   {sys.version.split()[0]} on {platform.system()}")
    ok = True

    for name in REQUIRED:
        version = version_of(name)
        print(f"{name:<10} {version or 'MISSING'}")
        ok &= version is not None

    torch_version = version_of("torch")
    if torch_version is None:
        print("torch      MISSING (see phase-0-setup/README.md)")
        ok = False
    else:
        import torch

        print(f"torch      {torch_version}")
        if torch.cuda.is_available():
            props = torch.cuda.get_device_properties(0)
            print(f"GPU        {props.name}, {props.total_memory / 2**30:.1f} GB")
            print(f"CUDA       {torch.version.cuda}")
            x = torch.randn(1024, 1024, device="cuda")
            assert torch.allclose(x @ torch.eye(1024, device="cuda"), x)
            print("GPU test   ok (matmul on the GPU)")
        else:
            print("GPU        not available: torch is CPU-only, or the driver is missing")
            ok = False

    print("\nReady." if ok else "\nNot ready yet: fix the lines above.")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
