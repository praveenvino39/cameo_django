from rest_framework.response import Response
def send_response(code, isSuccess,message="",is_object=True,data=None):
    if is_object:
        if data:
            return Response({"response": data, "message": message, "success": isSuccess}, status=code)
        else:
            return Response({"response": {}, "message": message, "success": isSuccess}, status=code)
    else:
        if data:
            return Response({"response": data, "message": message, "success": isSuccess}, status=code)
        else:
            return Response({"response": [], "message": message, "success": isSuccess}, status=code)