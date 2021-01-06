# Dark Society Makefile

# Complete the installation (placeholder)
.PHONY: finish
finish: install_deps
	@echo "Completed installation of dependencies."
	@echo "Completed the Meatball Installation."


# Install the project dependencies
install_deps: init_env requirements.txt
	@echo "Installation of project dependencies."
	@venv/bin/pip install --upgrade pip
	@venv/bin/pip install wheel
	@venv/bin/pip install -r requirements.txt --upgrade


# Install/create the Python virtual environment
install_venv: init
	@echo "Installation started."
	@echo "Installation of virtual environment."
	@test -d venv || python3 -m venv venv


# Add venv activate to clipboard
.PHONY: init_env
init_env: install_venv
	@echo "Initiating environment."
	@echo "source venv/bin/activate" | xclip -sel clip


# Initiate project creation (placeholder)
.PHONY: init
init:
	@echo "Starting the Python Meatball Installation."


# Remove the virtual environment
clean:
	@rm -rf venv
	@echo "Removed the project dependencies."
