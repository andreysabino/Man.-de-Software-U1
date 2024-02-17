from rest_framework.viewsets import ModelViewSet
from estacionamento.models import Veiculo, Patio, Pagamento, Dono
from estacionamento.api.serializers import DonoSerializer, VeiculoSerializer, PatioSerializer, PagamentoSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

class DonoListCreateView(ModelViewSet):
    serializer_class = DonoSerializer
    queryset = Dono.objects.all()

class VeiculoListCreateView(ModelViewSet):

    serializer_class = VeiculoSerializer
    queryset = Veiculo.objects.all()


class PatioListCreateView(ModelViewSet):

    serializer_class = PatioSerializer
    queryset = Patio.objects.all()

class PagamentoListCreateView(ModelViewSet):

    serializer_class = PagamentoSerializer
    queryset = Pagamento.objects.all()