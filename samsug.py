# matplotlib.pyplot : 그래프 그리기용 라이브러리.
# Investar.Analyzer : 네이버 금융에서 주식 데이터를 가져오는 사용자 정의 라이브러리
# Analyzer.MarketDB() : MarketDB 클래스 - 주가 클래스모음
# plt.legend(loc=""), plt.title(""), plt.grid(color="", linestyle="--")
# plt.yticks([]), plt.xticks([]), plt.show()

# 인터넷에서 이미지를 받아와 저장하고, 복사한 후, 두 파일이 같은지 해시값으로 검증하고, 마지막으로 이미지 두 개를 시각화해 보여줌

# stream = True => 바이트 형태
# Image.open(r) => 바이트형태 => 이미지 객체로 변환, img.show() => 이미지 미리보기 창 띄움
# 이미지는 .jpg , .png 와 같은 이진데이터임
# 그래서 .text 또는 .json()처럼 읽으면 깨지거나 에러가 남.
# 그래서 .raw로 바이트 스트림으로 직접 접근하는것
# 그리고 Image.open("")을 통해 이진데이터를 이미지 객체로 파싱
from PIL import Image
import hashlib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

r = './Pak_choi.png'
img = Image.open(r)
img.show()
img.save('src.png')

BUF_SIZE = 1024
with open('src.png', 'rb') as sf, open('dst.png', 'wb') as df:
    while True:
        data = sf.read(BUF_SIZE)
        if not data:
            break
        df.write(data)
        
sha_src = hashlib.sha256()
sha_dst = hashlib.sha256()

with open('src.png', 'rb') as sf, open('dst.png', 'rb') as df:
    sha_src.update(sf.read())
    sha_dst.update(df.read())

print("src.png's hash: {}".format(sha_src.hexdigest()))
print(f"dst.png's hash: {sha_dst.hexdigest()}")

plt.suptitle('Image Processing', fontsize = 18)
plt.subplot(1,2,1)
plt.title('Original Image')
plt.imshow(mpimg.imread('src.png'))

plt.subplot(1,2,2)
plt.title('Pseudocolor Image')
dst_img = mpimg.imread('dst.png')
pseudo_img = dst_img[:,:,0]
plt.imshow(pseudo_img)
plt.savefig('result.png')
plt.show()
