from django.contrib.auth.models import User
from django.urls import reverse
from django.test import RequestFactory, TestCase
from .forms import CommentForm
from .models import Report
from .views import ReportList

class TestFullReportView(TestCase):

    def setUp(self):

        self.user = User.objects.create_superuser(
            username="Innsmouth",
            password="Dunwich",
            email="cthulhu@waitsdreaming.com"
        )
        self.post = Report(title="Test Report Title", 
                           author=self.user,
                           slug="test-report-title", 
                           description="An Automated Test Case",
                           content="Report content", 
                           status=1, 
                           category="3",)
        self.post.save()

    def test_render_full_report_page_with_comment_form(self):
        
        response = self.client.get(reverse(
            'full_report', args=['test-report-title']))
        
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Test Report Title", response.content)
        self.assertIn(b"Report content", response.content)
        self.assertIsInstance(
            response.context['comment_form'], CommentForm)
        
    
    def test_comment_submission(self):
        """Test for posting a comment on a post"""

        self.client.login(
            username="Innsmouth", password="Dunwich")
        
        post_data = {
            'content': 'This is a test comment.'
        }
        response = self.client.post(reverse(
            'full_report', args=['test-report-title']), post_data)
        
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Comment submitted and awaiting approval', response.content)


class TestHomePage(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

        self.user = User.objects.create_superuser(
            username="Innsmouth",
            password="Dunwich",
            email="cthulhu@waitsdreaming.com"
        )
    
    def test_index_page_view(self):
        """
        Test authenticated and unauthenticated view of home page
        """
        # Create an instance of a GET request.
        request = self.factory.get('/')
        # Verify default template used. 
        self.assertTemplateUsed('base.html')
        # get home page view (not logged in)
        home_page = ReportList.as_view()(request)
        # Verify using line of text in nav bar
        self.assertContains(home_page, 'A collection of weird tales and urban legends.')
        # verify has expected unauthenticated navigation
        self.assertContains(home_page, 'Login')
        self.assertContains(home_page, 'Sign-Up')
        self.assertContains(home_page, 'Home')
        self.assertContains(home_page, 'About')
        # Check Admin links are absent
        self.assertNotContains(home_page, 'Admin Home')
        self.assertNotContains(home_page, 'Report List')
        self.assertNotContains(home_page, 'Comment List')
        # Simulate logged-in user by setting request.user
        request.user = self.user
        # get home page view (now logged in)
        home_page = ReportList.as_view()(request)
        self.assertTemplateUsed('index.html')
        # Check 'Login' and 'Sign-Up links are removed.
        self.assertNotContains(home_page, 'Login')
        self.assertNotContains(home_page, 'Sign-Up')
        # Check user has staff status with admin links 
        # (user is superuser so this should be True)
        self.assertContains(home_page, 'Admin Home')
        self.assertContains(home_page, 'Report List')
        self.assertContains(home_page, 'Comment List')

    def test_404_view(self):
        """
        Test 404 page appears
        """
        request = self.factory.get('/thispageisnowhere/')
        self.assertTemplateUsed('404.html')