### Dependency confusion attack for PyPI (proof of concept)

As of version 21 `pip` package management tool ignores the package
indices priorities. That means if you've got a package `X` both on
PyPI global index and on your private index, `pip` installs what fits
best to your system based on package version, Python version tag,
Platform tag, etc.

It doesn't matter if you use `--index-url` or `--extra-index-url` for
the private index url, PyPI global index is used anyway if no package
version is specified upon installation. E.g. if PyPI has `X==3.14.15`
and your private index `X=0.1.1`, both versions support the same Python
versions, OS, etc, then:

```
pip install --index-url=http://your.private.pip.index X
```

ends up in `X` being installed from the global PyPI and private index
being ignored.

That may be used as an attack, so-called dependency confusion. Since
PyPI doesn't support namespaces as Maven or Clojars do, you cannot
simply squat a namespace matching your private package namespace (or
prefix) to prevent someone else hijacking it and use for the
dependency confusion.

See more details here:
https://github.com/pypa/pip/issues/8606

What you can do is probably the following:

1. Set up private index policies not to proxy requests to PyPI for
your private package namespace/prefix.

E.g. see the solution for Sonatype Nexus registry:
https://blog.sonatype.com/namespace-confusion-minimizing-risk-with-nexus-repository

2. You more sophisticated naming convention for the private packages
to minimize possible clashes with the global index (security through
obscurity isn't a great idea though)

3. Check for naming clashes between the private package
namespace/prefix and the global ones automatically, report if the
clash is found

4. Squat private package name in the global PyPI with the
package-placeholder of the minimal version like `0.0.0`

5. When installing private packages always use exact matching,
i.e. `pip install X==0.1.1`

Remember though, that some private registries may update the package
with the same version from the global index, if the global one is
uploaded more recently!
