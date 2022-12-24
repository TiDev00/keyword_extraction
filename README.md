# DITA Keywords Extraction Tool

## Description
Useful tool to extract keyword for multiple dita files. 
It is based on Unsupervised Approach for Automatic 
Keyword Extraction using Text Features. Yake and kwx are 
used for the extracting model.

## Installation
Simply download the image locally by running on your 
terminal :
```
docker pull <link/to/keyword_extractor/image>
```

You can list all the available images on your pc with the command :
```
docker images
```

To delete an existing image just type the command :
```
docker rmi <ImageName>
```

## Usage
To use the docker image of the extractor you have to :
* Create a container from the keyword_extractor image downloaded<br>
* Run the created container in interactive mode and use the extractor<br>

### Container creation
Create a docker container and map the virtual /mnt directory to local 
folder containing dita files with the following command :
```
docker run --name <ContainerName> -v <Absolutepath/to/dita/folder>:/mnt --itd tcisse507/keyword_extractor
```
* \<ContainerName> : Replace by the name we want to give to our container
* \<Absolutepath/to/dita/folder> : Replace by path to a folder with dita 
files

### Container execution
Execute the created docker container with the command :
```
docker exec -it <ContainerName> python ./extractor.py
```

### Stopping container
To stop the container after extraction run command :
```
docker stop <ContainerName>
```

### List all containers
To list all the container in your pc run the command :
```
docker ps -a 
```

### Delete an existing container
To delete a container stop it first then type the command :
```
docker rm <ContainerName> 
```

You have the choice between yake and bert for your
extraction task. 
Depending on which one you choose, you will have specific
parameters to provide.<br>
The program also allows you to generate a file with the
list of extracted keywords from text corpus.

Steps describe with the commands can also be done via the docker GUI.

## Author
Thierno Ibrahima Cisse
