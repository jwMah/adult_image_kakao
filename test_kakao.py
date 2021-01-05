import sys
import argparse
import requests
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

#예제 URL : https://bimage.interpark.com/milti/renewPark/evtboard/20190915174947722.jpg

API_URL = 'https://dapi.kakao.com/v2/vision/adult/detect'

#카카오 developers에 가서 앱 생성 뒤 rest api key 복붙
MYAPP_KEY = 'MYAPP_KEY'

print('hello~')
def detect_adult(image_url):
    print('hello')
    headers = {'Authorization': 'KakaoAK {}'.format(MYAPP_KEY)}

    try:
        data = {'image_url':image_url}
        resp = requests.post(API_URL,headers=headers,data=data)
        resp.raise_for_status()
        result = resp.json()['result']
        if result['adult'] > result['normal'] and result['adult'] > result['soft']:
            print("성인 이미지일 확률이 {}% 입니다.".format(result['adult']*100))
        elif result['soft'] > result['normal'] and result['soft'] > result['adult']:
            print("노출이 포함된 이미지일 확률이 {}% 입니다.".format(result['soft']*100))
        else :
            print("일반적인 이미지일 확률이 {}%입니다".format(result['normal']*100))

    except Exception as e:
        print(str(e))
        sys.exit(0)

#이 파일이 main프로그램으로 사용될때 실행
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Classify adult image')
    parser.add_argument('image_url', type=str, nargs='?',
        default="http://t1.daumcdn.net/alvolo/_vision/openapi/r2/images/10.jpg",
        help='image url to classify')
    args = parser.parse_args()
    print(args)
    detect_adult(args.image_url)
