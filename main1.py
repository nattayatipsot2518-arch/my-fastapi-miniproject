from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():

    return """
<!DOCTYPE html>
<html lang="en,th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>เว็บเด็กน้อย</title>
</head>
<body>
  
    <h1>Hello everyone</h1>
     <h3>คิดถึงที่รักจางเลยยยยยยย</h3>
            <p>รักอ้วมที่สุดดด 🚀</p>
</body>
</html>
    """
@app.get("/main", response_class=HTMLResponse)
def main():
    return """
<!DOCTYPE html>
<html lang="en,th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>เว็บเด็กน้อย</title>
</head>
<body>
  
    <h>HI Tirukkk</h>
     <h2>อยากกอดที่รักจางงง</h2>
        love you kub 🚀
</body>
</html>
    """
