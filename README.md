# python_lod
Obtencion de recursos linked open data.
Restringido a 10 recursos por falta de capacidad de procesamiento , filtrado de la siguiente manera.

## Ejecución del programa
```
## -------------------------------
python main.py -r [sitio] - lectura del sitio
python main.py -d [sitio] - lista de dataset del sitio
python main.py -f [sitio] -l [limite] - obtiene el metadata filtrado de los dataset del sitio, limitado
```

<strong>Datos filtrados:</strong><br/>
Obtiene el metadata filtrado de cada dataset consultado previamente de la lista
```
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
```
<br/>archivo de salida (package_lecture_filter.json)
