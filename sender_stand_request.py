import configuration
import requests
import data


#Запрос на создание заказа
def post_new_user(body):
    response = requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body,
                         headers=data.headers)

    return response.json()["track"]

#Запрос на получения заказа по треку заказа
def post_new_user1(track):
    response = requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH + str(track))
    print(response.status_code)

    # Проверить, что код ответа равен 200
    assert response.status_code == 200

#Выполнить запрос на создание заказа и сохранение номера трека заказа
track_response = post_new_user(data.user_body)

#Выполнить запрос на получения заказа по треку заказа
post_new_user1(track_response)
