from rest_framework import serializers
from .models import stock_market as DataModel


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataModel
        fields = ["id","trade_code","high","low","open","close","volume","date"]
