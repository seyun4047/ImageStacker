# For Image staking
이미지 여러장을 쌓아 올려 노이즈 감소  , 흔들림 보정, 피사체 강조 등의 효과를 얻을 수 있는
알고리즘을 구현해보고자 함.

---------------------
---------------------

## Major Update
29.01.24 added stakingImg.py
<img width="1605" alt="스크린샷 2024-01-29 17 21 56" src="https://github.com/seyun4047/ImageStacker/assets/73819780/4ac5e390-d988-48ce-81f1-0ff97d81d900">
- cal each pix's avg

---------------------
---------------------

## 개선이 요구되는 사항
기존 픽셀을 이탈한 사진이 한장만 있는 경우에도 이미지에 큰 영향을 줌.
- threshold 설정이 필요해보임.
