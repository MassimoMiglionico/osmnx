def pre_mutation(context):
    if context.filename not in 'geocoder.py':
        context.skip = True