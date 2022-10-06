import sys
import os

libr = [
    "Standard Model 1.4",
    "Waifu Diffusion 1.2",
    "Waifu Diffusion 1.3 (epoch 9)",
    "Trinart Stable Diffusion v2 60,000 Steps",
    "Trinart Stable Diffusion v2 95,000 Steps",
    "Trinart Stable Diffusion v2 115,000 Steps",
    "Hiten",
    "WD v1.2 and SD v1.4 Merged",
    "gg1342_testrun1",
    "Hentai Diffusion RD1412",
    "Bare Feet / Full Body b4_t16_noadd",
    "Lewd Diffusion 70k (epoch 2)",
    "Yiffy (epoch 18)",
    "Furry (epoch 4)",
    "Zack3D Kinky v1",
    "R34 (epoch 1)",
    "Pony Diffusion",
    "Pokemon",
]

id = sys.argv[1]


def checkNum(i):
    if i >= 1 and i <= 18:
        return i
    elif i == "":
        return 1
    else:
        return 0


rst = checkNum(int(id))

if rst == 0:
    print("잘못 입력하셨습니다. 기본 모델로 다운로드합니다.")
    rst = 1
else:
    print(libr[rst - 1] + " 모델로 다운로드합니다.")


model = libr[rst - 1]

models = {
    "Standard Model 1.4": {"url": "https://public.vmm.pw/aeon/models/sd-v1-4.ckpt"},
    "Waifu Diffusion 1.2": {
        "url": "https://public.vmm.pw/aeon/models/wd-v1-2-full-ema-pruned.ckpt"
    },
    "Waifu Diffusion 1.3 (epoch 9)": {
        "url": "https://huggingface.co/hakurei/waifu-diffusion-v1-3/resolve/main/model-epoch09-float16.ckpt",
        "args": ["-o", "wd-v1-3-epoch09-float16.ckpt"],
    },
    "Trinart Stable Diffusion v2 60,000 Steps": {
        "url": "https://huggingface.co/naclbit/trinart_stable_diffusion_v2/resolve/main/trinart2_step60000.ckpt"
    },
    "Trinart Stable Diffusion v2 95,000 Steps": {
        "url": "https://huggingface.co/naclbit/trinart_stable_diffusion_v2/resolve/main/trinart2_step95000.ckpt"
    },
    "Trinart Stable Diffusion v2 115,000 Steps": {
        "url": "https://huggingface.co/naclbit/trinart_stable_diffusion_v2/resolve/main/trinart2_step115000.ckpt"
    },
    "Hiten": {
        "url": "https://huggingface.co/BumblingOrange/Hiten/resolve/main/Hiten%20girl_anime_8k_wallpaper_4k.ckpt"
    },
    "gg1342_testrun1": {"url": "https://public.vmm.pw/aeon/models/gg1342_testrun1_pruned.ckpt"},
    "Hentai Diffusion RD1412": {
        "url": "https://public.vmm.pw/aeon/models/RD1412-pruned-fp16.ckpt",
        "args": ["-o", "hentai_diffusion-rd1412-pruned-fp32.ckpt"],
    },
    "Bare Feet / Full Body b4_t16_noadd": {
        "url": "https://public.vmm.pw/aeon/models/bf_fb_v3_t4_b16_noadd-ema-pruned-fp16.ckpt"
    },
    "Lewd Diffusion 70k (epoch 2)": {
        "url": "https://public.vmm.pw/aeon/models/LD-70k-2e-pruned.ckpt"
    },
    "Yiffy (epoch 18)": {"url": "https://public.vmm.pw/aeon/models/yiffy-e18.ckpt"},
    "Furry (epoch 4)": {"url": "https://public.vmm.pw/aeon/models/furry_epoch4.ckpt"},
    "Zack3D Kinky v1": {
        # "url": "https://public.vmm.pw/aeon/models/Zack3D_Kinky-v1.ckpt"
        "url": "https://iwiftp.yerf.org/Furry/Software/Stable%20Diffusion%20Furry%20Finetune%20Models/Finetune%20models/Zack3D_Kinky-v1.ckpt"
    },
    "R34 (epoch 1)": {"url": "https://public.vmm.pw/aeon/models/r34_e1.ckpt"},
    "Pony Diffusion": {
        "url": "https://public.vmm.pw/aeon/models/pony_sfw_80k_safe_and_suggestive_500rating_plus-pruned.ckpt"
    },
    "Pokemon": {
        "url": "https://huggingface.co/justinpinkney/pokemon-stable-diffusion/resolve/main/ema-only-epoch%3D000142.ckpt",
        "args": ["-o", "pokemon-ema-pruned.ckpt"],
    },
}


if model in models:
    model = models[model]

    if model["url"].startswith("https://public.vmm.pw"):
        model[
            "desc"
        ] = """****
\x1b[31m경고: 개인 웹 서버로부터 모델을 받아옵니다!\x1b[0m
서버가 닫혔거나 맛이 간 상태라면 문제가 생길 수 있습니다.
오래 걸리거나 실행 중 오류가 발생한다면 다른 모델을 선택하거나 직접 받아주세요.
https://rentry.org/sdmodels
****
""" + model.get(
            "desc", ""
        )

else:
    model = {
        "url": model,
        "desc": f"""****
\x1b[31m경고: 사용자가 정의한 주소로부터 모델을 받아옵니다!\x1b[0m
오래 걸리거나 실행 중 오류가 발생한다면 다른 모델을 선택해주세요.
{model}
****""",
    }

if "desc" in model:
    print(model["desc"])

# Aria2 에서 사용할 인자 만들기
# args = ["-d", "./stable-diffusion-webui/models/Stable-diffusion"]
args = ["-P", "./stable-diffusion-webui/models/Stable-diffusion"]

if "args" in model:
    args += model["args"]

# args.append(model["url"])
args.insert(0, model["url"])
args = " ".join(args)

# Aria2로 모델 받아오기... 였으나 이상하게 aria2가 작동안해서 wget으로 대체
os.system("wget " + args)
