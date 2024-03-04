from django.test import TestCase
from .forms import ReportForm, CommentForm


class TestReportForm(TestCase):

    def test_report_form_is_valid(self):
        """ Tests all required fields """
        report_form = ReportForm({
            'title': 'Test Report',
            'category': '3',
            'content': '"Testing 1, 2, 3", said the audio technician',
            'status': '1'
            })
        self.assertTrue(report_form.is_valid())

    def test_empty_report_form_is_invalid(self):
        """ Tests all required fields """
        report_form = ReportForm({
            'title': '',
            'category': '',
            'content': '',
            'status': ''
            })
        self.assertFalse(report_form.is_valid())


class TestCommentForm(TestCase):

    def test_comment_form_is_valid(self):
        """ Tests all required fields """
        comment_form = CommentForm({
            'content': 'This story tested my patience.'
        })
        self.assertTrue(comment_form.is_valid())

    def test_empty_comment_form_is_valid(self):
        """ Tests all required fields """
        comment_form = CommentForm({
            'content': ''
        })
        self.assertFalse(comment_form.is_valid())
        