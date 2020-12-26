### About
This is the documentation about the activities of the Backdoor Collective.

When submitting updates to this repository, they will automatically get published
to [https://backdoor-collective.org/docs/](https://backdoor-collective.org/docs/).

### How to build locally
```
git clone https://github.com/backdoor-collective/documentation backdoor-collective-documentation
cd backdoor-collective-documentation
make docs-html
open docs/_build/html/index.html
```

### How to publish assets
Larger items like images, videos etc. should not be submitted to the Git repository.
Instead, upload them to [https://ptrace.backdoor-collective.org/](https://ptrace.backdoor-collective.org/).

Synopsis:
```
make ptrace source=tmp/koilelab-signalk-tolino.png
```

That will respond with the absolute URL for your convenience:
```
Access URL: https://ptrace.backdoor-collective.org/2020-12-26_koilelab-signalk-tolino.png
```
