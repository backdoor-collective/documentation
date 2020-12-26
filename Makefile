# ============
# Main targets
# ============


# -------------
# Configuration
# -------------

$(eval venv        := .venv)
$(eval pip         := $(venv)/bin/pip)
$(eval python      := $(venv)/bin/python)
$(eval sphinx      := $(venv)/bin/sphinx-build)


# Setup Python virtualenv
setup-virtualenv:
	@test -e $(python) || python3 -m venv $(venv)

virtualenv-docs: setup-virtualenv
	@test -e $(sphinx) || $(pip) --quiet install --requirement requirements.txt --verbose

docs-html: virtualenv-docs
	touch docs/index.md
	export SPHINXBUILD="`pwd`/$(sphinx)"; cd docs; make html
