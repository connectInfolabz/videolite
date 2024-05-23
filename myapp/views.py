from django.shortcuts import render, redirect
import requests
from .models import *

from django.contrib import messages

def search(request):
    if request.session.get("login_id") is None:
        messages.error(request, "Login Required")
        return redirect(index)
    try:
        uid = request.session.get('login_id')
        if uid:
            userdata = signup.objects.get(id=uid)

            if request.method == "POST":
                query = request.POST.get("query")

                url = "https://yt-api.p.rapidapi.com/search"

                querystring = {"query": f"{query}", "geo": "IN"}

                # headers = {
                #     "x-rapidapi-key": "2ea054400fmsh0f704edbee5f191p1346d8jsn124804ca4c24",
                #     "x-rapidapi-host": "yt-api.p.rapidapi.com"
                # }

                # headers = {
                #     "x-rapidapi-key": "7edecf88a5msh6460eb67921005dp151a03jsn938a4d93e2ec",
                #     "x-rapidapi-host": "yt-api.p.rapidapi.com"
                # }
                
                headers = {
                "x-rapidapi-key": "d1cdc518d8mshf21c5dc9e4b20c4p11ad42jsn8a083e29935a",
                "x-rapidapi-host": "yt-api.p.rapidapi.com"
                }
                response = requests.get(url, headers=headers, params=querystring)

                context = {"videos":response.json()["data"], "user" : userdata}

                return render(request, "search.html", context)
    except:
        pass
    messages.error(request, "Opps Some Error Occurs Try After Some Time.")
    return render(request, "index.html")


def songs(request):
    if request.session.get("login_id") is None :
        messages.error(request, "Login Required")
        return redirect(index)
    try:
        uid = request.session.get('login_id')
        if uid:
            userdata = signup.objects.get(id=uid)

            url = "https://yt-api.p.rapidapi.com/trending"

            querystring = {"geo": "IN", "type": "music"}

            # headers = {
            #     "x-rapidapi-key": "2ea054400fmsh0f704edbee5f191p1346d8jsn124804ca4c24",
            #     "x-rapidapi-host": "yt-api.p.rapidapi.com"
            # }

            # headers = {
            #     "x-rapidapi-key": "7edecf88a5msh6460eb67921005dp151a03jsn938a4d93e2ec",
            #     "x-rapidapi-host": "yt-api.p.rapidapi.com"
            # }
            
            headers = {
                "x-rapidapi-key": "d1cdc518d8mshf21c5dc9e4b20c4p11ad42jsn8a083e29935a",
                "x-rapidapi-host": "yt-api.p.rapidapi.com"
            }
            response = requests.get(url, headers=headers, params=querystring)

            context = {"videos": response.json()["data"], "user":userdata}

            return render(request, "index.html", context)
    except:
        pass

    messages.error(request, "Opps Some Error Occurs Try After Some Time.")
    return render(request, "index.html")
def movies(request):
    if request.session.get("login_id") is None:
        messages.error(request, "Login Required")
        return redirect(index)
    try:
        uid = request.session.get('login_id')
        if uid:
            userdata = signup.objects.get(id=uid)

            url = "https://yt-api.p.rapidapi.com/trending"

            querystring = {"geo": "IN", "type": "movies"}

            # headers = {
            #     "x-rapidapi-key": "2ea054400fmsh0f704edbee5f191p1346d8jsn124804ca4c24",
            #     "x-rapidapi-host": "yt-api.p.rapidapi.com"
            # }
            # headers = {
            #     "x-rapidapi-key": "7edecf88a5msh6460eb67921005dp151a03jsn938a4d93e2ec",
            #     "x-rapidapi-host": "yt-api.p.rapidapi.com"
            # }

            headers = {
                "x-rapidapi-key": "d1cdc518d8mshf21c5dc9e4b20c4p11ad42jsn8a083e29935a",
                "x-rapidapi-host": "yt-api.p.rapidapi.com"
            }
            response = requests.get(url, headers=headers, params=querystring)

            context = {"videos": response.json()["data"], "user":userdata}
            return render(request, "index.html", context)
    except:
        pass

    messages.error(request, "Opps Some Error Occurs Try After Some Time.")
    return render(request, "index.html")
def games(request):
    if request.session.get("login_id") is None:
        messages.error(request, "Login Required")
        return redirect(index)
    try:
        uid = request.session.get('login_id')
        if uid:
            userdata = signup.objects.get(id=uid)

            url = "https://yt-api.p.rapidapi.com/trending"

            querystring = {"geo": "IN", "type": "games"}

            # headers = {
            #     "x-rapidapi-key": "2ea054400fmsh0f704edbee5f191p1346d8jsn124804ca4c24",
            #     "x-rapidapi-host": "yt-api.p.rapidapi.com"
            # }
            # headers = {
            #     "x-rapidapi-key": "7edecf88a5msh6460eb67921005dp151a03jsn938a4d93e2ec",
            #     "x-rapidapi-host": "yt-api.p.rapidapi.com"
            # }
            
            headers = {
                "x-rapidapi-key": "d1cdc518d8mshf21c5dc9e4b20c4p11ad42jsn8a083e29935a",
                "x-rapidapi-host": "yt-api.p.rapidapi.com"
            }
            response = requests.get(url, headers=headers, params=querystring)

            context = {"videos": response.json()["data"], "user":userdata}
            return render(request, "index.html", context)

    except:
        pass

    messages.error(request, "Opps Some Error Occurs Try After Some Time.")
    return render(request, "index.html")


def video(request,vid):
    if request.session.get("login_id") is None:
        messages.error(request, "Login Required")
        return redirect(index)
    try:
        uid = request.session.get('login_id')
        if uid:
            userdata = signup.objects.get(id=uid)
            url = "https://yt-api.p.rapidapi.com/video/info"

            querystring = {"id": f"{vid}", "geo": "IN"}

            # headers = {
            #     "x-rapidapi-key": "2ea054400fmsh0f704edbee5f191p1346d8jsn124804ca4c24",
            #     "x-rapidapi-host": "yt-api.p.rapidapi.com"
            # }

            # headers = {
            #     "x-rapidapi-key": "7edecf88a5msh6460eb67921005dp151a03jsn938a4d93e2ec",
            #     "x-rapidapi-host": "yt-api.p.rapidapi.com"
            # }
            
            headers = {
                "x-rapidapi-key": "d1cdc518d8mshf21c5dc9e4b20c4p11ad42jsn8a083e29935a",
                "x-rapidapi-host": "yt-api.p.rapidapi.com"
            }

            videodetails = requests.get(url, headers=headers, params=querystring)

            url = "https://yt-api.p.rapidapi.com/related"

            querystring = {"id": f"{vid}", "geo": "IN"}


            related = requests.get(url, headers=headers, params=querystring)

            return render(request, "video-page.html", context={"vid":vid, "videodetails": videodetails.json(), "relatedvideos":related.json()['data'], "user":userdata})
    except:
        pass

    messages.error(request, "Opps Some Error Occurs Try After Some Time.")
    return render(request, "index.html")


def channel(request,cid):
    if request.session.get("login_id") is None:
        messages.error(request, "Login Required")
        return redirect(index)
    try:
        uid = request.session.get('login_id')
        if uid:
            userdata = signup.objects.get(id=uid)
            url = "https://yt-api.p.rapidapi.com/channel/videos"

            querystring = {"id": f"{cid}"}

            # headers = {
            #     "x-rapidapi-key": "2ea054400fmsh0f704edbee5f191p1346d8jsn124804ca4c24",
            #     "x-rapidapi-host": "yt-api.p.rapidapi.com"
            # }

            # headers = {
            #     "x-rapidapi-key": "7edecf88a5msh6460eb67921005dp151a03jsn938a4d93e2ec",
            #     "x-rapidapi-host": "yt-api.p.rapidapi.com"
            # }
            
            headers = {
                "x-rapidapi-key": "d1cdc518d8mshf21c5dc9e4b20c4p11ad42jsn8a083e29935a",
                "x-rapidapi-host": "yt-api.p.rapidapi.com"
            }
            response = requests.get(url, headers=headers, params=querystring)

            return render(request, "channelDetails.html",context={"channel":response.json()['meta'], "videos": response.json()['data'], "user":userdata})
    except:
        pass

    messages.error(request, "Opps Some Error Occurs Try After Some Time.")
    return render(request, "index.html")

def login(request):
    return render(request, "login.html")


def register(request):
    return render(request, "register.html")



def registeruser(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if signup.objects.filter(email=email).exists():
            messages.error(request, "Email already exists. Please choose a different email.")
            return redirect(index)

        else:
            try:
                if password1 == password2:
                    insertuser = signup(name=username,email=email, phone=phone, password=password1,added_on="")
                    insertuser.save()
                    userid = insertuser.id
                    messages.success(request, "Account created now you can login !!!")
                    return redirect(index)

            except:
                pass
        return redirect(index)

def verifyuser(request):
    if request.method == "POST":
        email = request.POST.get("username")
        pwd = request.POST.get("password")

        try:
            userdata = signup.objects.get(email=email, password=pwd)
            request.session["login_id"] = userdata.id
            request.session.save()
            messages.success(request, "Login Successfull!!")
            return redirect(index)

        except signup.DoesNotExist:
            messages.error(request, "Invalid Details")
            return redirect(index)
    else:
        messages.info(request, "Some Error Occurs")

    return render(request, "landing.html")


def logout(request):
    try:
        del request.session["login_id"]
        messages.success(request, "Logout Successful!")
        return redirect(index)
    except:
        pass
    return redirect(index)



def account(request):
    return render(request, "account.html")


def index(request):

    try:
        uid = request.session.get('login_id')
        if uid:
            userdata = signup.objects.get(id=uid)
            url = "https://yt-api.p.rapidapi.com/trending"
            querystring = {"geo": "IN"}

            # headers = {
            #     "x-rapidapi-key": "2ea054400fmsh0f704edbee5f191p1346d8jsn124804ca4c24",
            #     "x-rapidapi-host": "yt-api.p.rapidapi.com"
            # }

            # headers = {
            #     "x-rapidapi-key": "7edecf88a5msh6460eb67921005dp151a03jsn938a4d93e2ec",
            #     "x-rapidapi-host": "yt-api.p.rapidapi.com"
            # }
            
            headers = {
                "x-rapidapi-key": "d1cdc518d8mshf21c5dc9e4b20c4p11ad42jsn8a083e29935a",
                "x-rapidapi-host": "yt-api.p.rapidapi.com"
            }
            response = requests.get(url, headers=headers, params=querystring)
            return render(request, "index.html",context={"videos":response.json()['data'], "user":userdata})
    except:
        pass
    url = "https://yt-api.p.rapidapi.com/trending"
    querystring = {"geo": "IN"}
    
    # headers = {
    #     "x-rapidapi-key": "2ea054400fmsh0f704edbee5f191p1346d8jsn124804ca4c24",
    #     "x-rapidapi-host": "yt-api.p.rapidapi.com"
    # }

    # headers = {
    #     "x-rapidapi-key": "7edecf88a5msh6460eb67921005dp151a03jsn938a4d93e2ec",
    #     "x-rapidapi-host": "yt-api.p.rapidapi.com"
    # }

    headers = {
            "x-rapidapi-key": "d1cdc518d8mshf21c5dc9e4b20c4p11ad42jsn8a083e29935a",
            "x-rapidapi-host": "yt-api.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)

    return render(request, "index.html", context={"videos": response.json()['data']})



def playlist(request, cid):
    if request.session.get("login_id") is None:
        messages.error(request, "Login Required")
        return redirect(index)
    try:
        uid = request.session.get('login_id')
        if uid:
            userdata = signup.objects.get(id=uid)

            url = "https://yt-api.p.rapidapi.com/channel/playlists"

            querystring = {"id": f"{cid}"}

            # headers = {
            #     "x-rapidapi-key": "2ea054400fmsh0f704edbee5f191p1346d8jsn124804ca4c24",
            #     "x-rapidapi-host": "yt-api.p.rapidapi.com"
            # }

            # headers = {
            #     "x-rapidapi-key": "7edecf88a5msh6460eb67921005dp151a03jsn938a4d93e2ec",
            #     "x-rapidapi-host": "yt-api.p.rapidapi.com"
            # }
            
            headers = {
                "x-rapidapi-key": "d1cdc518d8mshf21c5dc9e4b20c4p11ad42jsn8a083e29935a",
                "x-rapidapi-host": "yt-api.p.rapidapi.com"
            }
            response = requests.get(url, headers=headers, params=querystring)

            print(response.json()['meta'])

            return render(request, "playlist.html", {"channel":response.json()['meta'], "playlists":response.json()['data'],"user":userdata})
    except:
        pass

    messages.error(request, "Opps Some Error Occurs Try After Some Time.")
    return render(request, "index.html")


def playlistvideos(request, pid):
    if request.session.get("login_id") is None:
        messages.error(request, "Login Required")
        return redirect(index)
    try:
        uid = request.session.get('login_id')
        if uid:
            userdata = signup.objects.get(id=uid)


            url = "https://yt-api.p.rapidapi.com/playlist"

            querystring = {"id": f"{pid}"}
            
            # headers = {
            #     "x-rapidapi-key": "2ea054400fmsh0f704edbee5f191p1346d8jsn124804ca4c24",
            #     "x-rapidapi-host": "yt-api.p.rapidapi.com"
            # }


            # headers = {
            #     "x-rapidapi-key": "7edecf88a5msh6460eb67921005dp151a03jsn938a4d93e2ec",
            #     "x-rapidapi-host": "yt-api.p.rapidapi.com"
            # }
            
            headers = {
                "x-rapidapi-key": "d1cdc518d8mshf21c5dc9e4b20c4p11ad42jsn8a083e29935a",
                "x-rapidapi-host": "yt-api.p.rapidapi.com"
            }
            response = requests.get(url, headers=headers, params=querystring)

            print(response.json()["data"])
            return render(request, "playlistVideos.html", context={"videos":response.json()["data"], "channel":response.json()["meta"]})
    except:
        pass

    messages.error(request, "Opps Some Error Occurs Try After Some Time.")
    return render(request, "index.html")


def about(request, cid):
    if request.session.get("login_id") is None:
        messages.error(request, "Login Required")
        return redirect(index)
    try:
        uid = request.session.get('login_id')
        if uid:
            userdata = signup.objects.get(id=uid)

            url = "https://yt-api.p.rapidapi.com/channel/about"

            querystring = {"id": f"{cid}"}

            # rahul infoalbz
            # headers = {
            #     "x-rapidapi-key": "2ea054400fmsh0f704edbee5f191p1346d8jsn124804ca4c24",
            #     "x-rapidapi-host": "yt-api.p.rapidapi.com"
            # }

            #petxhub 
            # headers = {
            #     "x-rapidapi-key": "7edecf88a5msh6460eb67921005dp151a03jsn938a4d93e2ec",
            #     "x-rapidapi-host": "yt-api.p.rapidapi.com"
            # }
            
            # connect
            headers = {
                "x-rapidapi-key": "d1cdc518d8mshf21c5dc9e4b20c4p11ad42jsn8a083e29935a",
                "x-rapidapi-host": "yt-api.p.rapidapi.com"
            }


            response = requests.get(url, headers=headers, params=querystring)

            return render(request, "about.html", context={"channel":response.json(), "links": response.json()["links"],"user":userdata})

    except:
        pass

    messages.error(request, "Opps Some Error Occurs Try After Some Time.")
    return render(request, "index.html")