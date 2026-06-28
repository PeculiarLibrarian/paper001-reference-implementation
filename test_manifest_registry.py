from kernel.manifest_registry import ManifestRegistry

for m in ManifestRegistry.discover():
    print(m)
