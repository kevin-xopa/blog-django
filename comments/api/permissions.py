from rest_framework.permissions import BasePermission
from comments.models import Comment


class IsOwnerOrReadAndCreateOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET' or request.method == 'POST':
            return False
        else:
            id_comment = view.kwargs['pk']
            comment = Comment.objects.get(pk=id_comment)
            id_user_comment = comment.user_id

            id_user = request.user.pk

            if id_user == id_user_comment:
                return True

            return False