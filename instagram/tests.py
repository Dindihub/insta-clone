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
    

class TestImage(TestCase):
    def setUp(self):
        self.profile_test = Profile(name='image', user=User(username='sandra'))
        self.profile_test.save()

        
        self.image_test = Image(image='default.png', name='test', caption='default test',likes='likes' ,user=self.profile_test)

    def test_instance(self):
        self.assertTrue(isinstance(self.image_test, Image))

    def test_save_image(self):
        self.image_test.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_image(self):
        self.image_test.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images)==0)

    def test_update_image(self):
        self.image_test.save_image()
        self.image_test.update_image(self.image_test.id, 'images/test.jpg')
        new_image = Image.objects.filter(image='images/test.jpg')
        self.assertTrue(len(new_image)>0)



    


