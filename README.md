# blog-app

<h2>This blog app allows the users to read, create, update,delete and comment on the posted posts</h2>
<hr>

**Only authenticated users can create, update, delete and comment.**

Want to checkout it out? Visit:

```https://korona-blog.herokuapp.com/```


Clone This Project (Make Sure You Have Git Installed)

```
https://github.com/tjeaneric/blog-app.git
```
Install Dependencies 

```
pip install -r requirements.txt
```

Set Database (Make Sure you are in directory same as manage.py)
```
python manage.py makemigrations

python manage.py migrate
```
Create SuperUser 
```
python manage.py createsuperuser
```

After all these steps , you can start testing and developing this project. 
