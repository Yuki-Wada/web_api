# Python
以下の順でインストールを行う
1. pyenv をインストール
1. pyenv で Python 3.9 をインストール
1. Poetry をインストール
1. Poetry でパッケージをインストール

## PyEnv
1. インストール
    1. Linux では以下のコマンドを実行
    ```
    git clone https://github.com/pyenv/pyenv.git ~/.pyenv
    echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
    echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
    echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bash_profile
    source ~/.bash_profile
    ```
    1. windows では、`https://github.com/pyenv-win/pyenv-win` でダウンロードできる ZIP ファイルを展開し、Path を追加
1. 各バージョンの Python をインストール
    1. `pyenv install --list` でインストールできる Python のバージョンを確認
    1. `pyenv install [バージョン名]` で [バージョン名] に対応した Python をインストール
    1. `pyenv version` でインストールできる Python のバージョンを確認
    1. `pyenv local [バージョン名]` で利用する Python のバージョンを指定
        - `pyenv global [バージョン名]` で利用する Python のバージョンを指定

## Poetry
1. インストール
    1. https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py から get-poetry.py をダウンロード
    1. `python get-poetry.py` を実行
    1. Poetry が不要になった場合は `python -m pip uninstall poetry` を実行
    1. Poetry があるディレクトリ (~/.poetry/bin) を Path に追加
1. ローカルディレクトリに仮想環境を作成
    1. `poetry config --list` で Poetry の設定を確認
    1. 仮想環境用ディレクトリの作成場所を設定
        - 仮想環境を現ディレクトリ下の .venv ディレクトリに作成するには、`poetry config virtualenvs.in-project true` を実行すればよい
        - 仮想環境を任意のディレクトリに作成するには、以下のコマンドを実行すればよい
        ```
        poetry config virtualenvs.in-project false
        poetry config virtualenvs.path [作成先ディレクトリ]
        ```
    1. `poetry install` を実行し、仮想環境を作成し、パッケージをインストール
1. ルートディレクトリを Python のモジュール検索パスに追加
    1. 以下を記述したテキストファイルを作成し、拡張子 pth で保存
    ```
    [インストールディレクトリ]
    ```
    1. 保存したファイルを [インストールディレクトリ]/.venv/Lib/site-packages ディレクトリ以下にコピー
1. その他、Poetry の使い方に関する Tips
    - パッケージを追加
    ```
    poetry add package
    ```
    - パッケージを追加
    ```
    poetry remove package
    ```

# Heroku
## 設定ファイル
- Procfile
- runtime.txt
- requirements.txt

## デプロイ
1. 以下の URL からダウンロードし、Heroku CLI をインストール
```
https://devcenter.heroku.com/articles/heroku-cli#download-and-install
```
1. 以下のコマンドを実行し、heroku デプロイ用の Git リモートレポジトリを追加
```
heroku git:remote -a [app-name]
```
    - heroku コマンドに Path が通っていない場合は、(一時的でよいので) コマンドがあるディレクトリに Path を通す
1. 以下のコマンドでデプロイ用のリモートレポジトリに push
```
git push heroku master
```
