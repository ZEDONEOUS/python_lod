#!/usr/bin/python2.7

import os
import json
import time
import sys

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
        data_file.close()
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
        consulta = consulta + " limit=" + str(limit) + " > datasets_package_list.json"
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



"""
    Obtiene una lista de revision de un dataset en especifico
    Variables:
        id_package = id o nombre del dataset(paquete) del cual traer la lista de revision
        query_point = punto de consulta sitio web
"""
def fetch_package_revision_list(id_package, query_point):
    consulta = "http --json --pretty format "
    consulta = consulta + query_point + "api/3/action/package_revision_list"
    consulta = consulta + "?id=" + str(id_package) + " > package_revision_list.json"
    os.system(consulta);



"""
    Obtiene el metadata filtrado de cada dataset consultado previamente de la lista
    Datos filtrados:
        title = nombre del dataset
        revision_id = id con el cual se puede consultar la lista de revision
        author = creador del dataset
        license_title = licencia bajo la cual se encuentra el recurso
        metadata_created = fecha de la creacion del metadata del dataset
        metadata_modified = fecha de la ultima modificacion del metadata del dataset
        relationships_as_object = relaciones que tiene el dataset como objeto
        relationships_as_subject = relaciones que tiene el dataset como sujeto
        organization_title = nombre de la organizacion
        organization_description = descripcion proveida por la organizacion
        resources =
            name = nombre del recurso
            last_modified = fecha de ultima modificacion
            state = estado del recurso, activo o inactivo
            url = vinculo a donde se encuentra alojado el recurso
            format = formato del recurso
            hash = hash cifrado de validacion en md5
        tags =
            tag_name = nombre del tag
            tag_id = id perteneciente al tag
"""
def fetch_all_datasets_package_metadata(query_point = "https://datahub.io/", limit = 0):
    last_time = time.time()
    fetch_datasets_package_list(0, query_point)
    with open("datasets_package_list.json") as data_file_list:
        datasets_list = json.load(data_file_list)
        metadata = {}
        metadata["packages"] = []
        local_limit = len(datasets_list["result"])
        if(int(limit) < len(datasets_list["result"]) and int(limit) > 0):
            local_limit = int(limit)
        for i in xrange(0, local_limit):
            fetch_dataset_package_metadata(datasets_list["result"][i], query_point)
            with open("package_metadata.json") as metadata_file:
                package_metadata = json.load(metadata_file)
                temp_obj = {}
                temp_obj["title"] = package_metadata["result"]["title"]
                temp_obj["revision_id"] = package_metadata["result"]["revision_id"]
                temp_obj["author"] = package_metadata["result"]["author"]
                temp_obj["license_title"] = package_metadata["result"]["license_title"]
                temp_obj["metadata_created"] = package_metadata["result"]["metadata_created"]
                temp_obj["metadata_modified"] = package_metadata["result"]["metadata_modified"]
                temp_obj["relationships_as_object"] = package_metadata["result"]["relationships_as_object"]
                temp_obj["relationships_as_subject"] = package_metadata["result"]["relationships_as_subject"]
                temp_obj["organization_title"] = package_metadata["result"]["organization"]["title"]
                temp_obj["organization_description"] = package_metadata["result"]["organization"]["description"]

                temp_obj["resources"] = []
                for j in xrange(0, len(package_metadata["result"]["resources"])):
                    temp_obj_resources = {}
                    temp_obj_resources["name"] = package_metadata["result"]["resources"][j]["name"]
                    temp_obj_resources["last_modified"] = package_metadata["result"]["resources"][j]["last_modified"]
                    temp_obj_resources["state"] = package_metadata["result"]["resources"][j]["state"]
                    temp_obj_resources["url"] = package_metadata["result"]["resources"][j]["url"]
                    temp_obj_resources["format"] = package_metadata["result"]["resources"][j]["format"]
                    temp_obj_resources["hash"] = package_metadata["result"]["resources"][j]["hash"]
                    temp_obj["resources"].append(temp_obj_resources)

                temp_obj["tags"] = []
                for k in xrange(0, len(package_metadata["result"]["tags"])):
                    temp_obj_tags = {}
                    temp_obj_tags["tag_name"] = package_metadata["result"]["tags"][k]["display_name"]
                    temp_obj_tags["tag_id"] = package_metadata["result"]["tags"][k]["id"]
                    temp_obj["tags"].append(temp_obj_tags)

                metadata["packages"].append(temp_obj)
            metadata_file.close()
    data_file_list.close()
    with open('package_lecture_filter.json', 'w') as outfile:
        json.dump(metadata, outfile, indent=4, sort_keys=True)
    outfile.close()
    print "Tiempo que tardo la recoleccion de datos:", (time.time() - last_time), "segundos"



if __name__ == '__main__':
    control_input = """
        ## -------------------------------
        python main.py -r [sitio] - lectura del sitio
        python main.py -d [sitio] - lista de dataset del sitio
        python main.py -f [sitio] -l [limite] - obtiene el metadata filtrado de los dataset del sitio, limitado
    """
    if(len(sys.argv) == 3):
        if(sys.argv[1] == "-r"):
            site_read(sys.argv[2])
            with open("site_read.json") as output_file:
                json_file = json.load(output_file)
                print json.dumps(json_file, indent=4, sort_keys=True)
            output_file.close()
        elif(sys.argv[1] == "-d"):
            fetch_datasets_package_list(0, sys.argv[2])
            with open("datasets_package_list.json") as output_file:
                json_file = json.load(output_file)
                print json.dumps(json_file, indent=4, sort_keys=True)
            output_file.close();
        else:
            print control_input
    elif(len(sys.argv) == 5):
        if(sys.argv[1] == "-f" and sys.argv[3] == "-l"):
            fetch_all_datasets_package_metadata(sys.argv[2], sys.argv[4])
    else:
        print control_input
