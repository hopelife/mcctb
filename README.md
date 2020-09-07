# mcctb
moon crypto-currency trading bot


# reference

## book
- [혼자서 만드는 가상화폐 자동거래 시스템](https://wikidocs.net/book/1436)
- [비트코인 개발자 가이드](https://wikidocs.net/book/1699)
- [파이썬을 이용한 비트코인 자동매매](https://wikidocs.net/book/1665)
- [bitcoin developer-guide](https://bitcoin.org/en/developer-guide)

## git
- [혼자서 만드는 가상화폐 자동거래 시스템](https://gitlab.com/hyunny88/auto-trading/)
- [파이썬을 이용한 비트코인 자동매매](https://github.com/sharebook-kr/book-cryptocurrency)

## site


# dev environment
- OS: windows10 / OSX
- language: python, nodejs, react
- DB: mongoDB
- editor: visual studio code
- vcs: git, github


# git
## remote
### create repository
- url: https://github.com/hopelife/mcctb.git


## local
### set config(user/password)
- 
### clone
```
\projects> git clone https://github.com/hopelife/mcctb.git
```

### .gitignore
```
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
pip-wheel-metadata/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt


# Sphinx documentation
docs/_build/

# PyBuilder
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
.python-version

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/
_ve/
```

# install dev environments

## install python

## create virtual environment
- create 
```
\projects\mcctb> python -m venv _ve
```
- activate
```
\projects\mcctb> _ve\Scripts\activate
```
- deactivate
```
\projects\mcctb> _ve\Scripts\deactivate
```

# directory structure
- 
```
_docs
_ev
conf
autotrding
  api
  db
  machine
  pusher
  scheduler
  strategy
logs
notebooks
scripts
tests
```

# pusher

## telegram
### ref
- [나만의 텔레그램 봇 만들기](https://junesker.tistory.com/6?category=899615)

## slack
### ref
- [슬랙봇을 만들어봅시다](https://story.pxd.co.kr/1262)
- [슬랙봇 만들기: API를 통해 정보 얻기 및 표시하기](https://brunch.co.kr/@sungi-kim/71)
- [슬랙(Slack) API 완벽 정리하기](https://13akstjq.github.io/api/2019/09/07/Slack-API-%EC%A0%95%EB%A6%AC%ED%95%98%EA%B8%B0.html)
- [Node 서버로 Slack 메신저 자동화하기](http://labs.brandi.co.kr/2019/01/30/kwakjs.html)