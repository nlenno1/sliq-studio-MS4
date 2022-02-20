from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import ClassCategory, SingleExerciseClass


def view_class_categories(request):
    """ A view to return all the categories"""

    categories = ClassCategory.objects.all()

    context = {
        'class_categories': categories
    }

    return render(request, 'classes/our_classes.html', context)


def view_single_class_category(request, category_id):
    """ A view to return details about an individual class category"""

    category = get_object_or_404(ClassCategory, pk=category_id)

    context = {
        'category': category
    }

    return render(request, 'classes/class_category_details.html', context)


def view_all_single_classes(request):
    """ A view to return all the single exercise classes"""

    classes = SingleExerciseClass.objects.all()
    categories = ClassCategory.objects.all()

    context = {
        'classes': classes,
        'class_categories': categories,
    }

    return render(request, 'classes/class_booking.html', context)


def filter_single_classes(request, category_id):
    """ A view to return all the single exercise classes"""

    classes = SingleExerciseClass.objects.all()
    categories = ClassCategory.objects.all()

    selected_filter_name = [item.friendly_name for item in categories if str(item.id) == str(category_id)]

    filtered_classes = [item for item in classes if str(item.category.id) == str(category_id)]

    context = {
        'classes': filtered_classes,
        'class_categories': categories,
        'selected_filter': selected_filter_name[0],
    }

    return render(request, 'classes/class_booking.html', context)
