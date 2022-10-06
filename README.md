# AltDiffusion for EasyStableDiffusion

이 레포지토리는 EasyStableDiffusion을 코랩 이외의 GPU호스팅에서 쉽게 실행할 수 있게 돕도록 만들어졌습니다.

## 세 줄 요약

선택사항\. 기존에 쓰던 지우고 파이썬 3.10 설치 먼저 하는게 좋음 (스크립트 내에 있긴한데 가끔 설치 안되고 그냥 넘어가는경우가 있어서)

```bash
# 선택사항, 아래는 3.10버전 설치하는 방법임 지우는건 알아서 해야함.
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt install -yq python3.10 python3.10-dev
sudo rm /usr/bin/python
ln -sf /usr/bin/python3.10 /usr/bin/python
```

1\. 레포지토리 clone 및 실행권한 부여

```bash
git clone https://github.com/panta5/AltDiffusion.git
cd AltDiffusion
sudo chmod +x setup.sh
```

2\. setup\.sh 실행

```bash
sudo ./setup.sh
```

3\. 실행

설치완료 후:

```bash
cd stable-diffusion-webui
python launch.py
```

## 자세한 설명

귀찮아
코드 내꺼 아니니까 궁금하면 원본게이꺼 보셈

## 알려진 이슈

| #   | 이슈 | 진행상황 |
| --- | ---- | -------- |
| 1   |      |          |

## 코드 출처

아카라이브 AI그림 채널: [바로가기](https://arca.live/b/aiart/59406212)

## 게시중단요청

깃허브 이슈남겨주시면 검토 후 처리하겠습니다.
