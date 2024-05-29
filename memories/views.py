from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Memory
from .forms import MemoryForm


def home(request):
    if request.user.is_authenticated:
        memories = Memory.objects.filter(user=request.user)
        return render(request, 'memories/home.html', {'memories': memories})
    return render(request, 'memories/welcome.html')


@login_required
def add_memory(request):
    if request.method == 'POST':
        form = MemoryForm(request.POST)
        if form.is_valid():
            memory = form.save(commit=False)
            memory.user = request.user
            memory.save()
            return redirect('home')
    else:
        form = MemoryForm()
    return render(request, 'memories/memory.html', {'form': form})


@login_required
def edit_memory(request, pk):
    memory = Memory.objects.get(pk=pk, user=request.user)
    if request.method == 'POST':
        form = MemoryForm(request.POST, instance=memory)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MemoryForm(instance=memory)
    return render(request, 'memories/memory.html', {'form': form})
