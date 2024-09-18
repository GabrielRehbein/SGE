import json
from openai import OpenAI
from django.core.serializers import serialize
from django.conf import settings
from .prompts import SYSTEM_PROMPT, USER_PROMPT
from products.models import Product
from outflows.models import Outflow
from .models import AIResult


class SGEAgent:

    def __init__(self):
        self.__client = OpenAI(
            api_key=settings.OPENAI_API_KEY
        )
        

    def __get_data(self):
        products = Product.objects.all()
        outflows = Outflow.objects.all()
        return json.dumps({
        'products_json': serialize('json', products),
        'outflows_json': serialize('json', outflows)
        })
    

    def invoke(self):
        response = self.__client.chat.completions.create(
            model=settings.OPENAI_MODEL,
            messages=[
                {
                    'role': 'system',
                    'content': SYSTEM_PROMPT
                },
                {
                    'role': 'user',
                    'content': USER_PROMPT.replace(
                        '{{data}}',
                        self.__get_data()
                    )
                }
            ]
        )
        result = response.choices[0].message.content
        
        AIResult.objects.create(
            result=result
        )
        
