# This Python file uses the following encoding: utf-8
from ViewsLibraries import *


# Article API Views...
class ArtigoListAPIView(ListAPIView):
    queryset = Artigo.objects.all()
    serializer_class = ArtigoSerializer

class ArtigoDetailAPIView(RetrieveAPIView):
    queryset = Artigo.objects.all()
    serializer_class = ArtigoSerializer


class ArtigoListAPI(APIView):
    def get(self, request):
        artigos = Artigo.objects.all().filter(status='p').order_by('data')
        serializer = ArtigoSerializer(artigos, many=True)
        return Response(serializer.data)

    def post(self):
        pass
#end ArtigoListAPI





# People API Views...
class PessoaListAPIView(ListAPIView):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer

class PessoaListAPI(APIView):
    def get(self, request):
        pessoa = Pessoa.objects.all().filter(status='p').order_by('id')
        serializer = PessoaSerializer(pessoa, many=True)
        return Response(serializer.data)

    def post(self):
        pass






# Projects API Views...
class PortfolioListAPIView(ListAPIView):
    queryset = Projecto.objects.all()
    serializer_class = PortfolioSerializer

class PortfolioListAPI(APIView):
    def get(self, request):
        projecto = Projecto.objects.all().filter(status='p').order_by('data')
        serializer = PortfolioSerializer(projecto, many=True)
        return Response(serializer.data)

    def post(self):
        pass





# Album API Views...
class AlbumListAPIView(ListAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class AlbumListAPI(APIView):
    def get(self, request):
        albums = Album.objects.all().filter(status='p')
        serializer = AlbumSerializer(albums, many=True)
        return Response(serializer.data)

    def post(self):
        pass

