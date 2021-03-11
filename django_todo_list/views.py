from django.shortcuts import render, redirect

from .models import ToDoItem, ToDoList


def index(request);
    items = ToDoList.objects.order_by("title")
    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
    form = ToDoListForm()
    data = {
        "forms": form,
        "list": items,
        "title": "To Do Lists"
    }
    return render(request, 'todo_list/index.html', data)

def item(request, item_id):
    item = ToDoList.objects.get(id=item_id);
    form = ToDoItemForm()
    data = {
        "forms":form,
        "item": item,
        "title":"To Do"
    }
    return render(request, 'todo_list/item.html', data)

# def delete (request, item_id):
#     item = ToDoList.objects.get(id = item_id)
#     item.delete()
#     return redirect('')


