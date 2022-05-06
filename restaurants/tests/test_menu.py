# import pytest
# import json
#
# from datetime import datetime
# from restaurants.models import Subsidary, Menu
#
#
# @pytest.mark.django_db()
# class Test_Menu():
#     """
#         정미정
#     """
#
#     @pytest.fixture
#     def _setup(self, client):
#         sub = Subsidary.objects.create(name='test')
#         menu = Menu.objects.create(subsidary=sub, name='test', price=12000)
#
#         self.delete = {
#             'is_delete': True,
#             'delete_at': datetime.now()
#         }
#
#         return menu.id
#
#     def test_get_menu(self, client, _setup):
#         response = client.get(
#             '/restaurants/subsidary/menu'
#         )
#         assert Menu.objects.count() == 1
#         assert response.status_code == 200
#
#     def test_get_menu_detail(self, client, _setup):
#         response = client.get(
#             f'/restaurants/subsidary/menu/{_setup}'
#         )
#         assert response.status_code == 200
#
#     def test_update_menu(self, client, _setup):
#         data = {
#             'price': 10000
#         }
#         response = client.patch(
#             f'/restaurants/subsidary/menu/{_setup}',
#             json.dumps(data), content_type='application/json'
#         )
#         assert response.status_code == 200
#
#     def test_delete_menu(self, client, _setup):
#         response = client.patch(
#             f'/restaurants/subsidary/menu/{_setup}',
#             self.delete, content_type='application/json'
#         )
#         assert response.status_code == 200
#
#     # def test_post_menu(self, client, _setup):
#     #     sub = Subsidary.objects.last()
#     #     response = client.post(
#     #         '/restaurants/subsidary/menu',
#     #         data={
#     #             'subsidary': sub.id,
#     #             'name': 'test',
#     #             'price': 12000
#     #         }, content_type='application/json'
#     #     )
#     #
#     #     assert response.status_code == 201
