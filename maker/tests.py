from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Contact

class ContactModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        """Test the api can store data in database"""
        test_user = get_user_model().objects.create_user(username='tester',password='pass')
        test_user.save()

        test_contact = Contact.objects.create(
            user = test_user,
            name='Test',
            email = 'test@test.com',
            mobile = 1234567890,
            address='place,at some place',
            image='https://ca.slack-edge.com/TNGRRLUMA-U023D77N874-f4ac72f0f594-512'
        )
        test_contact.save()

    def test_contant_content(self):
        contact = Contact.objects.get(id=1)
        self.assertEqual(str(contact.name),  'Test')
        self.assertEqual(contact.email, 'test@test.com')
        self.assertEqual(contact.mobile, 1234567890)
        self.assertEqual(contact.address, 'place,at some place')
        self.assertEqual(contact.image, 'https://ca.slack-edge.com/TNGRRLUMA-U023D77N874-f4ac72f0f594-512')
class APITest(APITestCase):
    """class of the API tests """
    def test_list(self):
        """Test the api can retrive a Contact list."""
        response = self.client.get(reverse('contacts_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    def test_detail(self):
        """Test the api can retrive a Contact details."""
        test_user = get_user_model().objects.create_user(username='tester',password='pass')
        test_user.save()

        test_maker = Contact.objects.create(
            user = test_user,
            name='Test',
            email = 'test@test.com',
            mobile = 1234567890,
            address='place,at some place',
            image='https://ca.slack-edge.com/TNGRRLUMA-U023D77N874-f4ac72f0f594-512'
        )
        test_maker.save()

        response = self.client.get(reverse('contacts_details', args=[1]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {
            'user':1,
            'name':'Test',
            'email' : 'test@test.com',
            'mobile' : 1234567890,
            'address':'place,at some place',
            'image':'https://ca.slack-edge.com/TNGRRLUMA-U023D77N874-f4ac72f0f594-512'
        })
    def test_delete(self):
        """Test the api can delete a Contact."""

        test_user = get_user_model().objects.create_user(username='tester',password='pass')
        test_user.save()

        test_maker = Contact.objects.create(
            user = test_user,
            name='Test',
            email = 'test@test.com',
            mobile = 1234567890,
            address='place,at some place',
            image='https://ca.slack-edge.com/TNGRRLUMA-U023D77N874-f4ac72f0f594-512'
        )

        test_maker.save()

        contact = Contact.objects.get()

        url = reverse('contacts_details', kwargs={'pk': contact.id})


        response = self.client.delete(url)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT, url)
    def test_update(self):
            """Test the api can update a Contact."""
            test_user = get_user_model().objects.create_user(username='tester',password='pass')
            test_user.save()

            test_maker = Contact.objects.create(
                user = test_user,
                name='Test',
                email = 'test@test.com',
                mobile = 1234567890,
                address='place,at some place',
                image='https://ca.slack-edge.com/TNGRRLUMA-U023D77N874-f4ac72f0f594-512'
            )

            test_maker.save()

            url = reverse('contacts_details',args=[test_maker.id])
            data = {          
                'user':test_maker.id,
                'name':test_maker.name,
                'email' : test_maker.email,
                'mobile' : test_maker.mobile,
                'address':"Testing is Still Fun!!!",
                'image':test_maker.image
            }

            response = self.client.put(url, data, format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK, url)

            self.assertEqual(Contact.objects.count(), test_maker.id)
            self.assertEqual(Contact.objects.get().name, data['name'])
