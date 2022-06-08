from django.test import TestCase
from .models import Image,Profile,Comment,Follow,User

# Create your tests here.
class ProfileTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.user = User(username='sandra')
        self.user.save()

        self.profile_test = Profile(id=1, user=self.user , profile_photo='default.jpg', bio='this is a test profile',
                                    name='image')

    def test_instance(self):
        self.assertTrue(isinstance(self.profile_test, Profile))

    def test_save_profile(self):
        self.profile_test.save_profile()
        after = Profile.objects.all()
        self.assertTrue(len(after) > 0)

    def test_delete_profile(self):
        self.profile_test.delete_profile()
        after = Profile.objects.all()
        self.assertTrue(len(after) == 0)


