# YOLO-v8

これは YOLO-v8 で画像認識をリアルタイムで行うプログラムです．ただクローンしてきただけです．
調布祭 2023 で面白そうだからという理由でやってみました．

## Usage

このプロジェクトはパッケージを多くインストールする必要があります．
そのため，仮想環境を作成してからインストールすることをおすすめします．

```bash
git clone ssh://git@gitlab.mma.club.uec.ac.jp:2223/gae/yolov8.git
cd yolov8
pip install -r requirements.txt     # install dependencies: recommend to use virtual environment
python detect.py --source 0         # webcam
```

## Virtual Environment

仮想環境(venv)を作成するには，プロジェクトのディレクトリに移動して以下のコマンドを実行します．

```bash
python -m venv .venv            # create virtual environment
source .venv/bin/activate       # activate virtual environment
pip install -r requirements.txt # install dependencies
```

仮想環境を終了するには，以下のコマンドを実行します．

```bash
deactivate
```
