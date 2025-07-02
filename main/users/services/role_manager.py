from ..models import Role

def assign_executor(user):
    user.role = Role.objects.get(name='executor')
    user.head = None
    user.save()

def assign_assistant(user, supervisor):
    user.role = Role.objects.get(name='assistant')
    user.head = supervisor
    user.save()