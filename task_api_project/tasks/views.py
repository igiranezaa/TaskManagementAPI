from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Task
from .serializers import TaskSerializer


# LIST & CREATE TASKS
class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user).order_by("-created_at")

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# RETRIEVE, UPDATE, DELETE A SINGLE TASK
class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


# MARK TASK AS COMPLETE
class TaskCompleteView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, pk):
        task = Task.objects.filter(user=request.user, pk=pk).first()

        if not task:
            return Response(
                {"detail": "Task not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        task.is_completed = True
        task.save()

        return Response(TaskSerializer(task).data, status=status.HTTP_200_OK)


# MARK TASK AS INCOMPLETE
class TaskIncompleteView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, pk):
        task = Task.objects.filter(user=request.user, pk=pk).first()

        if not task:
            return Response(
                {"detail": "Task not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        task.is_completed = False
        task.save()

        return Response(TaskSerializer(task).data, status=status.HTTP_200_OK)
