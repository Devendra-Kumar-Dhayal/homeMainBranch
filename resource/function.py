
from .models import MyModel


def display_objects(request, app_id, platform_check, categories):
    
    existing_objects = [obj.id for obj in MyModel.objects.all()]
    new_objects = MyModel.objects.filter(
        app_id=app_id).exclude(id__in=existing_objects)

    if not new_objects:  
        default_object = {'name': 'No objects found',
                          'platform': 'N/A', 'reviews': 'N/A'}
        return render(request, 'myapp/display_objects.html', {'objects': [default_object]})

    
    object_ids = [obj.id for obj in new_objects]
    reviews = {obj.id: obj.reviews for obj in MyModel.objects.filter(
        object_id__in=object_ids)}

    
    new_objects = sorted(
        new_objects, key=lambda obj: reviews.get(obj.id, 0), reverse=True)

    
    if platform_check == 'Windows':
        new_objects = [obj for obj in new_objects if obj.platform == 'Windows']
    elif platform_check == 'MacOS':
        new_objects = [obj for obj in new_objects if obj.platform == 'MacOS']

    
    if categories == 'name':
        new_objects = sorted(new_objects, key=lambda obj: obj.name)
    elif categories == 'platform':
        new_objects = sorted(new_objects, key=lambda obj: obj.platform)
    elif categories == 'reviews':
        new_objects = sorted(
            new_objects, key=lambda obj: reviews.get(obj.id, 0), reverse=True)

    return render(request, 'homepage.html', {'objects': new_objects})
