def test_webapp_get_retrieve_contacts(test_client):
    response = test_client.get("/contacts")

    assert response is not None
    assert response.status_code == 200


# @pytest.mark.asyncio
# async def test_webapp_get_show_contact_form():
#     request = Request(scope={"type": "http"})
#     response = await insert_contact(request)

#     assert response is not None
#     assert response.status_code == 200
#     assert isinstance(response.template, Template)
#     assert response.template.name == "new.html"


# TODO: test show contact form
