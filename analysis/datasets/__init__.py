"""Dataset access modules for OpenScience.

Two datasets are available for programmatic use by agents:
  - allen_brain: Allen Brain Atlas Cell Types (electrophysiology + morphology)
  - dandi: DANDI Archive (neurophysiology in NWB format)
"""

from . import allen_brain, dandi

__all__ = ["allen_brain", "dandi"]
