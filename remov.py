from django.contrib.contenttypes.models import ContentType

# List of deleted apps
# List of deleted models (that are not in the app deleted) In lowercase!
DEL_MODELS = ["type", "activity", "comment"]

ct = ContentType.objects.all().order_by("model")

for c in ct:
    if c.model in DEL_MODELS:
        print("Delete", c.model)
        c.delete()