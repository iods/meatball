# Iods Python Projects Makefile

linux: init install_venv init_env install_deps finish
osx: init install_venv init_env_mac install_deps finish


# Complete the installation (placeholder)
.PHONY: finish
finish:
	@echo "Completed installation of dependencies."
	@echo "Completed the Meatball Installation."


# Install the project dependencies
install_deps: requirements.txt
	@echo "Installation of project dependencies."
	@venv/bin/pip install --upgrade pip
	@venv/bin/pip install wheel
	@venv/bin/pip install -r requirements.txt --upgrade


# Install/create the Python virtual environment
install_venv:
	@echo "Installation started."
	@echo "Installation of virtual environment."
	@test -d venv || python3 -m venv venv


# Add venv activate to clipboard
init_env:
	@echo "Initiating environment."
	@echo "source venv/bin/activate" | xclip -sel clip

# Install on OSX
init_env_mac:
	@echo "Initiating OSX environment."
	@echo "source venv/bin/activate" | pbcopy


# Initiate project creation (placeholder)
.PHONY: init
init:
	@echo "Starting the Python Meatball Installation."


# Remove the virtual environment
clean:
	@rm -rf venv
	@echo "Removed the project dependencies."
