from imghdr import tests
from multiprocessing.connection import answer_challenge

from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from sections.models import Section, SectionContent, Tests
from sections.permissions import IsModerator
from sections.serializers.section_serializers import SectionListSerializer, SectionSerializer
from sections.serializers.section_content_searializers import SectionContentListSerializer, SectionContentSerializer
from sections.serializers.tests_serializers import TestsSerializer, TestsQuestionSerializer
from sections.paginators import SectionPaginator, ContentPaginator, TestsPaginator


class SectionListAPIView(ListAPIView):
    serializer_class = SectionListSerializer
    queryset = Section.objects.all()
    # permission_classes = [IsAuthenticated]
    pagination_class = SectionPaginator


class SectionCreateAPIView(CreateAPIView):
    serializer_class = SectionSerializer
    # permission_classes = [IsAuthenticated, IsAdminUser | IsModerator]


class SectionRetrieveAPIView(RetrieveAPIView):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    # permission_classes = [IsAuthenticated]


class SectionUpdateAPIView(UpdateAPIView):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    # permission_classes = [IsAuthenticated, IsAdminUser | IsModerator]


class SectionDestroyAPIView(DestroyAPIView):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    # permission_classes = [IsAuthenticated, IsAdminUser | IsModerator]


class ContentListAPIView(ListAPIView):
    serializer_class = SectionContentListSerializer
    queryset = SectionContent.objects.all()
    # permission_classes = [IsAuthenticated]
    pagination_class = ContentPaginator


class ContentCreateAPIView(CreateAPIView):
    serializer_class = SectionContentSerializer
    # permission_classes = [IsAuthenticated, IsAdminUser | IsModerator]


class ContentRetrieveAPIView(RetrieveAPIView):
    serializer_class = SectionContentSerializer
    queryset = SectionContent.objects.all()
    # permission_classes = [IsAuthenticated]


class ContentUpdateAPIView(UpdateAPIView):
    serializer_class = SectionContentSerializer
    queryset = SectionContent.objects.all()
    # permission_classes = [IsAuthenticated, IsAdminUser | IsModerator]


class ContentDestroyAPIView(DestroyAPIView):
    serializer_class = SectionContentSerializer
    queryset = SectionContent.objects.all()
    # permission_classes = [IsAuthenticated, IsAdminUser|IsModerator]


class TestListAPIView(ListAPIView):
    serializer_class = TestsSerializer
    queryset = Tests.objects.all()
    # permission_classes = [IsAuthenticated]
    pagination_class = TestsPaginator


class TestQuestionRetrieveAPIView(RetrieveAPIView):
    serializer_class = TestsQuestionSerializer
    queryset = Tests.objects.all()

    # permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        answers = [test.answer for test in Tests.objects.all()]
        answer = answers[self.kwargs.get('pk') - 1].lower()
        user_answer = request.data.get('user_answer').lower()
        is_correct = user_answer == answer
        return Response({'is_correct': is_correct})
