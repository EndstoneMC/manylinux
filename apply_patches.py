import glob
import patch_ng

for patch_file in glob.glob("patches/*.patch"):
    patchset = patch_ng.fromfile(patch_file)
    if not patchset:
        raise RuntimeError(f"Failed to parse patch: {patch_file}")

    if not patchset.apply():
        raise RuntimeError(f"Failed to apply patch: {patch_file}")
