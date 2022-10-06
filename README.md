# AltDiffusion for EasyStableDiffusion

이 레포지토리는 EasyStableDiffusion을 코랩 이외의 GPU호스팅 및 로컬 환경에서 쉬운 실행을 돕도록 만들어졌습니다.

유지보수가 될지는 몰?루

버그나면 바로바로 처리가 어렵기 때문에, 리눅스 및 파이썬에 대한 기초적인 지식은 있어야 합니다.

만든놈: [PantaFive](https://arca.live/u/@PantaFive)

## 간단 가이드

> 당연한 소리지만 그래픽카드 드라이버는 알아서 설치해야함

선택사항\. 기존에 쓰던 지우고 파이썬 3.10 설치 먼저 하는게 좋음

(스크립트 내에 있긴한데 가끔 설치 안되고 그냥 넘어가는경우가 있어서)

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

## 작동확인

설치할때 오류 한두개씩 튀어나오긴 하는데 대부분 GPU호스팅에서 돌아가는거 확인함.

## 알려진 이슈

|  #  | 이슈 | 진행상황 |
| :-: | :--: | :------: |
|  1  | 없음 |   없음   |

## TODO

1. 윈도우버전 제작
2. setup.sh 대부분 환경에서 버그 안나게 수정
3. 기존 파이썬 제거 및 3.10버전 설치 지원하기

## 기여

리포지토리 포크 한 후 Pull Request 보내주시면 됩니당.

## 코드 출처

아카라이브 AI그림 채널: [바로가기](https://arca.live/b/aiart/59955768)

## 게시중단요청

깃허브 이슈남겨주시면 검토 후 처리하겠습니다.
