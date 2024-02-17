from rest_framework import serializers
from estacionamento.models import Dono
from estacionamento.models import Veiculo
from estacionamento.models import Patio
from estacionamento.models import Pagamento

class DonoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dono
        fields = '__all__'

class VeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veiculo
        fields ='__all__' 

class PatioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patio
        fields = '__all__'

class PagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagamento
        fields = '__all__'
