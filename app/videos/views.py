from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Video
from .serializers import VideoSerializer
from rest_framework.exceptions import NotFound

# 1. VideoList
# api/v1/videos
# - GET: 전체 비디오 목록 조회 => Video.objects.all() => 클라이언트에 전달
# - POST: 새로운 비디오 생성 
# - DELETE, PUT: X
class VideoList(APIView):
    def get(self, request):
        videos = Video.objects.all()
        print('video : ', videos) # 직렬화 (장고객체 -> JSON으로 변환) => SERIALRIZER

        serializer = VideoSerializer(videos, many=True) # 쿼리셋이 2개 이상

        return Response(serializer.data)
    

# 2. VideoDetail
# api/v1/video{video_id}
# - GET: 특정 비디오 상세 조회
# - POST: X
# - PUT: 특정 비디오 정보 업데이트(수정)
# - DELETE: 특정 비디오 삭제
class VideoDetail(APIView):
    def get_object(self, pk):
        try:
            return Video.objects.get(pk=pk)
        except Video.DoesNotExist:
            raise NotFound

    def get(self, request, pk): # pk: Primary Key(ID)
        video = self.get_object(pk)
        serializer = VideoSerializer(video)

        return Response(serializer.data)