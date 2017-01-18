#!/usr/bin/python2.7

import os
import json

"""
    Desarrolla una lectura preeliminar del sitio
    Variables:
        query_point = punto de consulta sitio web (defecto - https://datahub.io/)
"""
def site_read(query_point = "https://datahub.io/"):
    consulta = "http --json --pretty format "
    consulta = consulta + query_point + "api/3/action/site_read > site_read.json"
    flag = False

    try:
        os.system(consulta)
        with open("site_read.json") as data_file:
            data = json.load(data_file)
            flag = data["success"]
    except Exception as e:
        print "EXCEPCION EN LA CONEXION CON EL SITIO - " + str(e)

    return flag



"""
    Trae una lista de los paquetes asociados a un sitio
    Variables:
        limit = limite de paquetes traidos (defecto - todos)
        query_point = punto de consulta sitio web (defecto - https://datahub.io/)
"""
def fetch_datasets_package_list(limit = 0, query_point = "https://datahub.io/"):
    if(site_read(query_point)):
        consulta = "http --json --pretty format "
        consulta = consulta + query_point + "api/3/action/package_list"
        consulta = consulta + " limit=" + str(limit) + " > output.json"
        os.system(consulta);
    else:
        print "ERROR - IMPOSIBLE CONECTAR CON EL SITIO ESPECIFICADO"



"""
    Trae el metadata de un paquete especifico
    Variables:
        id_package = id o nombre del dataset(paquete) del cual traer la metadata
        query_point = punto de consulta sitio web
"""
def fetch_dataset_package_metadata(id_package, query_point):
    consulta = "http --json --pretty format "
    consulta = consulta + query_point + "api/3/action/package_show"
    consulta = consulta + "?id=" + str(id_package) + " > package_metadata.json"
    os.system(consulta);

#fetch_dataset_package_metadata("0000-0003-4469-8298", "https://datahub.io/")
fetch_datasets_package_list()
