#!/bin/bash

# 오래된 우분투를 사용하여 파이썬을 받을 수 없는 경우 사용자 레포지토리 추가하기
if ! apt-cache show python3.10 > /dev/null 2>&1; then
  echo '패키지 관리자에 Python 3.10 이 존재하지 않습니다, 사용자 레포지토리를 추가합니다'
  apt update && apt upgrade -y
  add-apt-repository ppa:deadsnakes/ppa -y
fi

# 파이썬 설치하기
if ! which python3.10 > /dev/null 2>&1; then
  echo 'Python 3.10 이 존재하지 않습니다, 새로 설치합니다'

  apt install -yq python3.10 python3.10-dev

  # 환경에 따라 PATH 값이 다르기 때문에 심볼릭을 바꾸는 편이 update-alternative 보다 간단함
  # TODO: 더 나은 방법이 있는지?
  ln -sf $(which python3.10) $(which python)
fi

# PIP 설치하기
if ! python -m pip > /dev/null 2>&1; then
  echo 'PIP 이 존재하지 않습니다, 새로 설치합니다'
  python <(curl -s 'https://bootstrap.pypa.io/get-pip.py')
fi

# WebUI 설치하기
git clone 'https://github.com/AUTOMATIC1111/stable-diffusion-webui'
apt install -y build-essential libgl1
pip install -r stable-diffusion-webui/requirements.txt

# 맵핑 위치 VRAM으로 설정
sed -i 's/map_location="cpu"/map_location=torch.device("cuda")/g' ./stable-diffusion-webui/modules/sd_models.py

# 추가 스크립트 설치하기
cd 'stable-diffusion-webui/scripts'

for i in \
  'https://raw.githubusercontent.com/jtkelm2/stable-diffusion-webui-1/master/scripts/wildcards.py' \
  'https://raw.githubusercontent.com/memes-forever/Stable-diffusion-webui-video/main/videos.py' \
  'https://raw.githubusercontent.com/yownas/seed_travel/main/scripts/seed_travel.py' \
  'https://gist.githubusercontent.com/camenduru/9ec5f8141db9902e375967e93250860f/raw/c1a03eb447548adbef1858c0e69d3567a390d2f4/run_n_times.py'
do
  echo $i
  curl -sO $i
done

pip install --upgrade setuptools # TODO: ...?
pip install moviepy

# 추가 패키지 설치하기
apt install -y aria2
mkdir -p ~/.aria2

# aria2 설정파일 저장하기
ariacfg="allow-overwrite=true
always-resume=true
disk-cache=64M
continue=true
min-split-size=8M
max-concurrent-downloads=16
max-connection-per-server=16
max-overall-download-limit=0
max-download-limit=0
split=32
seed-time=0"

echo "$ariacfg" > ~/.aria2/aria2.conf

