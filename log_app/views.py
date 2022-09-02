from rest_framework.response import Response
from rest_framework.views import APIView
import logging
logger = logging.getLogger(__name__)

class Example_API(APIView):

    def get(self, request):
        msg = "GET method for the api"
        logger.error("-------------------------------this is a get method")
        logger.debug("-------------------------------this is a get method")
        logger.info("-------------------------------this is a get method")
        logger.warning("-------------------------------this is a get method")
        return Response(msg)
    def  post(self, request):
        logger.error("this is a post method")
        return Response("POST method from the api")