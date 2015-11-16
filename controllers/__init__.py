import os
import glob
modules = glob.glob(os.path.dirname(__file__) + "/*.py")
__all__ = [os.path.basename(fname)[:-3] for fname in modules if os.path.isfile(fname)]