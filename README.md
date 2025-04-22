Simple python webservice to call mediainfo and return the results as json

docker build -t mediainfo_ws .

docker run -d -p 8000:8000 -v /data:/data mediainfo_ws

curl 'http://localhost:8000?file=/data/media_file'
