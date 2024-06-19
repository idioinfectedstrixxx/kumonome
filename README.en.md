# kumonome
Kumonome - simple random YouTube search scanner



![image(8)](https://github.com/idioinfectedstrixxx/kumonome/assets/172582897/b09ca32b-95a0-410e-9387-0eab13984866)


[Russian readme](https://github.com/idioinfectedstrixxx/kumonome/blob/main/README.md)

Rather simple random search script for YouTube(I'd want to research other videohostings and do smthing similar in the future too). Made without Google API, it takes data from the HTML-request. Some count of random symbols for YouTube id are generating, then generates url with search request like inurl:[random generated symbol]. So, it's almost random search by symbols in id. It was made like my script for netstalking, due to this it searches unpopular videos(there is a view count restriction which you can adjust). It's able to search random videos, channels or playlists. It also has fractional date filters for videos and playlists: script will search ones which was uploaded before some year/date only. Loads video's previews and channel's pfps if possible

Run with
```
python3 kumonome.py [--ql int --maxviews int]
```

Where the --ql argument is count of random-generated symbols in query(default = 5), and --maxviews is a max count of views for video search(default = 2000). Both of these arguments aren't strictly reqired, if you don't enter it, the default values will be used

![Screenshot_5](https://github.com/idioinfectedstrixxx/kumonome/assets/172582897/f3d5a322-e567-4084-bf19-cbf066cdf555)
![изображение](https://github.com/idioinfectedstrixxx/kumonome/assets/172582897/6d61777e-7953-4097-b946-5c75fdfcf510)
