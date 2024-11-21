import sender_stand_request
import data
from sender_stand_request import auth_token

def get_kit_body(name_kit):
    current_body = data.kit_body.copy()
    current_body["name"] = name_kit
    return current_body

def positive_assert(name_kit):
    user_body = get_kit_body(name_kit)
    user_response = sender_stand_request.post_new_client_kit(user_body, auth_token)
    print(user_response.status_code)
    print(user_response.json())
    assert user_response.status_code == 201
    assert user_response.json().get("name") == name_kit

def negative_assert_code_400(name_kit):
    kit_body_negative = get_kit_body(name_kit)
    response_negative = sender_stand_request.post_new_client_kit(kit_body_negative, auth_token)
    print(response_negative.status_code)
    print(response_negative.json())
    assert response_negative.status_code == 400
    assert response_negative.json()["code"] == 400

def test1_create_kit_1_letter_name():
    positive_assert("a")


def test2_create_kit_511_letter_name():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")


def test5_create_kit_special_characters_name():
    positive_assert("\"№%@\",")


def test6_create_kit_with_space_name():
    positive_assert("A Aaa")


def test7_create_kit_with_string_number_name():
    positive_assert("123")



#PRUEBAS NEGATIVAS


def test3_create_kit_without_letter_name():
    negative_assert_code_400("")


def test4_create_kit_512_letter_name():
    negative_assert_code_400("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")


def test8_create_kit_without_name():
    negative_assert_code_400()


def test9_create_kit_with_number_name():
    negative_assert_code_400(123)






