import io
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Women


class WomenModel:

    def __init__(self, title, content) -> None:
        self.title = title
        self.content = content


class WomenSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()


# object -> dict -> json
def encode():
    model = WomenModel(title='Madi', content='Madi Abay')
    model_sr = WomenSerializer(instance=model)
    print(model_sr.data, type(model_sr.data), sep='++++++')
    json = JSONRenderer().render(model_sr.data)
    print(json)

# json -> dict -> object
def decode():
    stream = io.BytesIO(b'{"title":"Madi","content":"Madi Abay"}')
    data = JSONParser().parse(stream=stream)
    serializer = WomenSerializer(data=data)
    serializer.is_valid()
    print(serializer.validated_data)
    return serializer.validated_data