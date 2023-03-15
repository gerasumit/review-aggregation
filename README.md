# Install brew and pyenv (virtual environment for python projects
```
sh -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install pipx
brew install pyenv
brew install pyenv-virtualenv
```

# Setup project
```
mkdir pyenv_dir/
cd pyenv_dir/
pyenv global 3.9.1
```

# Clone the repo
```
git clone https://github.com/gerasumit/review-aggregation.git
```

# Activate virtual environment
```
pyenv virtualenv review-aggregation
pyenv activate review-aggregation
cd review-aggregation/
```

# Install python dependencies
```
pip3 install -r requirements.txt
python3 relevancy_job.py
```
