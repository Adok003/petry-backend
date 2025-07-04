from ..models import Role

def assign_executor(user, assigned_by=None):
    user.role = Role.objects.get(name='executor')
    user.head = assigned_by if assigned_by else None
    user.save()

def assign_assistant(user, supervisor):
    user.role = Role.objects.get(name='assistant')
    user.head = supervisor
    user.save()

def assign_accountant(user, supervisor):
    user.role = Role.objects.get(name='accountant')
    user.head = supervisor
    user.save()
