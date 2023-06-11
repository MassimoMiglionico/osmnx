def pre_mutation(context):
    if context.filename not in ['geocoder.py','folium.py','graph.py','downloader.py']:
        context.skip = True