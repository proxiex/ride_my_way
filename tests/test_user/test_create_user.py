from tests.base import BaseTestCase
from api.user.model import User
from utils.database import db_session
from fixtures.user.create import (
    empyt_user,
    new_user,
    no_first_name,
    user_first_name_with_special_chars,
    user_last_name_with_special_chars,
    user_username_with_special_chars,
    empty_user_first_name
)

import sys
import os
import json
sys.path.append(os.getcwd())


class TestCreateUser(BaseTestCase):

    def jsondumps(self, data):
        return json.dumps(data)

    def test_empty_user_data(self):
        """
        Testing for empty data passed to create User
        """
        empyt_user_json = self.jsondumps(empyt_user)

        expected_response = self.client.post(
                                '/api/v1/user',
                                content_type='application/json',
                                data=empyt_user_json
                                )

        self.assertEqual(expected_response.status_code, 400)
        self.assertIn('Please pass in data', str(expected_response.data))
        self.assertIn('fail', str(expected_response.data))
        self.assertIn('helpMessage', str(expected_response.data))

    def test_no_frist_name(self):
        """
        Testing for user data with now first name
        """
        empty_user_first_name_json = self.jsondumps(empty_user_first_name)
        expected_response = self.client.post(
                                '/api/v1/user',
                                content_type='application/json',
                                data=empty_user_first_name_json
                                )
        self.assertEqual(expected_response.status_code, 400)
        self.assertIn('All fields must be filled', str(expected_response.data))
        self.assertIn('fail', str(expected_response.data))

    def test_emtpy_frist_name(self):
        """
        Testing ffor user data with emtpy first name
        """
        no_first_name_json = self.jsondumps(no_first_name)
        expected_response = self.client.post(
            '/api/v1/user',
            content_type='application/json',
            data=no_first_name_json
            )
        self.assertEqual(expected_response.status_code, 400)
        self.assertIn('All fields are requried', str(expected_response.data))
        self.assertIn('fail', str(expected_response.data))
        self.assertIn('helpMessage', str(expected_response.data))

    def test_first_name_with_special_characters(self):
        """
        Testing for user data with special characters.
        """
        user_with_special_chars_json = self.jsondumps(user_first_name_with_special_chars)  # noqa: E501
        expected_response = self.client.post(
                                '/api/v1/user',
                                content_type='application/json',
                                data=user_with_special_chars_json
                                )
        self.assertEqual(expected_response.status_code, 400)
        self.assertIn(
            'first_name contains special characters',
            str(expected_response.data)
            )

    def test_last_name_with_special_characters(self):
        """
        Testing for user data with special characters.
        """
        user_with_special_chars_json = self.jsondumps(user_last_name_with_special_chars)  # noqa: E501
        expected_response = self.client.post(
                                '/api/v1/user',
                                content_type='application/json',
                                data=user_with_special_chars_json
                                )
        self.assertEqual(expected_response.status_code, 400)
        self.assertIn(
            'last_name contains special characters',
            str(expected_response.data)
            )

    def test_username_with_special_characters(self):
        """
        Testing for user data with special characters.
        """
        user_with_special_chars_json = self.jsondumps(user_username_with_special_chars)   # noqa: E501
        expected_response = self.client.post(
                                '/api/v1/user',
                                content_type='application/json',
                                data=user_with_special_chars_json
                                )
        self.assertEqual(expected_response.status_code, 400)
        self.assertIn(
            'username contains special characters',
            str(expected_response.data)
            )

    def test_create_user(self):
        """
        Testing for user data with special characters.
        """
        new_user_json = self.jsondumps(new_user)   # noqa: E501
        expected_response = self.client.post(
                                '/api/v1/user',
                                content_type='application/json',
                                data=new_user_json
                                )
        self.assertEqual(expected_response.status_code, 201)
        self.assertIn('Successfully registered', str(expected_response.data))
        self.assertIn('success', str(expected_response.data))

    def test_create_user_exist(self):
        """
        Testing for user data with special characters.
        """
        user = User(
                    first_name="Biskyet",
                    last_name="Nanpit",
                    username="Bis",
                    email="loveme@me.com",
                    password="password"
                )
        user.save()
        db_session.commit()

        new_user_json = self.jsondumps(new_user)   # noqa: E501
        expected_response = self.client.post(
                                '/api/v1/user',
                                content_type='application/json',
                                data=new_user_json
                                )
        self.assertEqual(expected_response.status_code, 409)
        self.assertIn(
            'This email \\\\"loveme@me.com\\\\" is already associated with an account',  # noqa: E501
            str(expected_response.data))
        self.assertIn('fail', str(expected_response.data))
