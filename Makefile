# Define the virtual environment name
VENV_NAME = .venv

# Define the command to create the virtual environment
CREATE_VENV = python3 -m venv .venv

# Define the command to install packages from requirements.txt
INSTALL_PACKAGES = $(CREATE_VENV) && pip install -r requirements.txt

# Target to create the virtual environment and install packages
.PHONY: install
install:
	@echo "Creating virtual environment with Python..."
	@$(CREATE_VENV)
	@echo "Installing packages from requirements.txt..."
	@$(INSTALL_PACKAGES)

# Target to clean the virtual environment
.PHONY: clean
clean:
	@echo "Removing virtual environment..."
	@rm -rf $(VENV_NAME)
