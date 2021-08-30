def select_stations_area(area, list_stations, buffer=0):
    """
    Seleciona as estações que estão dentro de uma área de interesse.
    :param area: Área de interesse como um objeto GeoPandas
    :param list_stations: Lista de estações como objeto geopandas
    :param buffer: Float, Opcional, Padrão = 0 - Buffer na área de interesse
    :return: Retorna um objeto Geopandas com as estações selecionadas
    """
    #Converte o formato das colunas Latitude e Longitude
    if list_stations.Longitude.dtype != float:
        list_stations.Longitude = list_stations.Longitude.astype(float)
    if list_stations.Latitude.dtype != float:
        list_stations.Latitude = list_stations.Latitude.astype(float)   
    
    # Cria uma Geometria de Pontos
    pontos=[Point(x) for x in zip(list_stations.Longitude,list_stations.Latitude)]
    crs={'proj':'latlong','ellps':'WGS84','datum':'WGS84','no_def':True} #SC WGS 84
    
    # Define o sistema de coordenadas como WGS 84
    list_stations=gpd.GeoDataFrame(list_stations,crs=crs,geometry=pontos)
    
    # Seleciona as estações que estão dentro da bacia
    list_stations = list_stations[list_stations.geometry.within(area.geometry[0].buffer(buffer))]
    return list_stations