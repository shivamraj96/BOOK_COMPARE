from flask import request, json, Response, Blueprint, g
import datetime

books_api = Blueprint('books_api', __name__)

@books_api.route('/compare', methods=['POST'])
def books_compare():
    """
    books_compare
    """
    req_data = request.get_json()
    book1 = req_data["book1"]
    book2 = req_data["book2"]
    p1=0
    p2=0
    p3=0
    l_name=0
    p5=0
    k=book1.get('first_name')
    h=book2.get('first_name')
    d1=book1.get('date')
    d2=book2.get('date')
    if k in h:
        p3=15
    if d1==d2:
        p5=20
    for key in book1:
        if (book1[key]) in book2[key]:  #fn =n fn =n key-fn
            print(key)
            if key=='ISBN':
                p2=100
                break
            else:
                if key=='last_name':l_name=25
                elif key=='first_name':p3=20
                elif key== 'tittle':p1=35
                elif key=='date':p5=20
        

                
                

    sum = p1+p2+p3+l_name+p5        


    res={"message":sum}
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=200
    )
