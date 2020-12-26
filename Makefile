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


# -------------------------------------
# https://backdoor-collective.org/docs/
# -------------------------------------

# Setup Python virtualenv
setup-virtualenv:
	@test -e $(python) || python3 -m venv $(venv)

virtualenv-docs: setup-virtualenv
	@test -e $(sphinx) || $(pip) --quiet install --requirement requirements.txt --verbose

docs-html: virtualenv-docs
	touch docs/index.md
	export SPHINXBUILD="`pwd`/$(sphinx)"; cd docs; make html



# ---------------------------------------
# https://ptrace.backdoor-collective.org/
# ---------------------------------------

# Don't commit media assets (screenshots, etc.) to the repository.
# Instead, upload them to https://ptrace.backdoor-collective.org/
ptrace_target := root@ptrace.backdoor-collective.org:/srv/www/organizations/backdoor-collective/ptrace.backdoor-collective.org/htdocs/
ptrace_http   := https://ptrace.backdoor-collective.org/
ptrace: check-ptrace-options
	$(eval prefix := $(shell date --iso-8601))
	$(eval name   := $(shell basename $(source)))
	$(eval id     := $(prefix)_$(name))

	@# debugging
	@#echo "name: $(name)"
	@#echo "id:   $(id)"

	@scp '$(source)' '$(ptrace_target)$(id)'

	$(eval url    := $(ptrace_http)$(id))
	@echo "Access URL: $(url)"

check-ptrace-options:
	@if test "$(source)" = ""; then \
		echo "ERROR: 'source' not set"; \
		exit 1; \
	fi

