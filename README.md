# python_lod
Obtencion de recursos linked open data.
Restringido a 10 recursos por falta de capacidad de procesamiento , filtrado de la siguiente manera.

<strong>Datos filtrados:</strong><br/>
Obtiene el metadata filtrado de cada dataset consultado previamente de la lista
Datos filtrados:
    <br/><t/>title = nombre del dataset
    <br/><t/>revision_id = id con el cual se puede consultar la lista de revision
    <br/><t/>author = creador del dataset
    <br/><t/>license_title = licencia bajo la cual se encuentra el recurso
    <br/><t/>metadata_created = fecha de la creacion del metadata del dataset
    <br/><t/>metadata_modified = fecha de la ultima modificacion del metadata del dataset
    <br/><t/>relationships_as_object = relaciones que tiene el dataset como objeto
    <br/><t/>relationships_as_subject = relaciones que tiene el dataset como sujeto
    <br/><t/>organization_title = nombre de la organizacion
    <br/><t/>organization_description = descripcion proveida por la organizacion
    <br/><t/>resources =
        <br/><t/><t/>name = nombre del recurso
        <br/><t/><t/>last_modified = fecha de ultima modificacion
        <br/><t/><t/>state = estado del recurso, activo o inactivo
        <br/><t/><t/>url = vinculo a donde se encuentra alojado el recurso
        <br/><t/><t/>format = formato del recurso
        <br/><t/><t/>hash = hash cifrado de validacion en md5
    <br/></t>tags =
        <br/><t/><t/>tag_name = nombre del tag
        <br/><t/><t/>tag_id = id perteneciente al tag
<br/>archivo de salida (package_lecture_filter.json)
