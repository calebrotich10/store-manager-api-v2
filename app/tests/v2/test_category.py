"""Module defines test cases for product category"""

from . import base_test
from app.api.v2 import database
from . import common_functions


class TestCategory(base_test.TestBaseClass):
    """Class defines CRUD methods for product category"""


    def test_post_category(self):
        """POST /category"""

        self.register_test_admin_account()
        token = self.login_test_admin()

        response = self.app_test_client.post('{}/category'.format(
            self.BASE_URL), json=self.CATEGORY, headers=dict(Authorization=token),
            content_type='application/json')

        self.assertEqual(response.status_code, 201)
        self.assertEqual(common_functions.convert_response_to_json(
            response)["message"], "Category created successfully")


    def test_get_all_categories(self):
        self.register_test_admin_account()
        token = self.login_test_admin()
        query = """INSERT INTO category(category_name) VALUES('Tools')"""
        
        database.insert_to_db(query)
        response = self.app_test_client.get("{}/category".format(
            self.BASE_URL), headers=dict(Authorization=token),
            content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(common_functions.convert_response_to_json(
            response)["message"], "Categories fetched successfully")
            